#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=UTF-8 :

# python-symmetricjsonrpc3
# Copyright (C) 2009 Egil Moeller <redhog@redhog.org>
# Copyright (C) 2009 Nicklas Lindgren <nili@gulmohar.se>
# Copyright (C) 2024 Robert "Robikz" Zalewski <zalewapl@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

"""JSON-RPC implementation classes."""
import threading
from logging import getLogger

from . import dispatcher
from . import json
from .io import makefile


logger = getLogger(__name__)


class RPCError(Exception):
    def __init__(self, error):
        if not isinstance(error, dict):
            error = {'message': str(error)}
        super().__init__(error.get('message') or '')
        self.code = error.get('code', 0)
        self.data = error.get('data')


class ClientConnection(dispatcher.Connection):
    """A connection manager for a connected socket (or similar) that
    reads and dispatches JSON values."""

    def _init(self, subject, parent=None, *arg, **kw):
        subject = makefile(subject, "rw")
        self.reader = json.Reader(subject)
        self.writer = json.Writer(subject)
        dispatcher.Connection._init(self, subject=subject, parent=parent, *arg, **kw)

    def shutdown(self):
        self.reader.close()
        self.writer.close()
        dispatcher.Connection.shutdown(self)

    def _exit(self):
        self.subject.close()
        super()._exit()

    def read(self):
        return self.reader.read_values()


class RPCErrorResponse(dict):
    def __init__(self, message, code=0, data=None, for_sending=False):
        if isinstance(message, Exception):
            exc = message
            if data is None:
                data = exc
            message = f"{type(exc).__name__}: {exc}"

        self["message"] = str(message)
        self["code"] = code
        if isinstance(data, Exception):
            self["data"] = {
                "type": type(data).__name__,
                "args": [self._argify(arg) for arg in data.args],
            }
            if not for_sending:
                self["data"]["exception"] = data
        elif hasattr(data, '__to_json__'):
            self["data"] = data.__to_json__()
        else:
            self["data"] = data

    @staticmethod
    def _argify(arg):
        if isinstance(arg, (int, float, str)):
            return arg
        elif hasattr(arg, '__to_json__'):
            return arg.__to_json__()
        else:
            return repr(arg)

    def to_result(self):
        return {"result": None, "error": self}


class RPCClient(ClientConnection):
    """A JSON-RPC client connection manager.

    This class represents a single client-server connection on both
    the connecting and listening side. It provides methods for issuing
    requests and sending notifications, as well as handles incoming
    JSON-RPC request, responses and notifications and dispatches them
    in separate threads.

    The dispatched threads are instances of RPCClient.Dispatch, and
    you must subclass it and override the dispatch_* methods in it to
    handle incoming data.
    """

    class Request(dispatcher.ThreadedClient):
        def dispatch(self, subject):
            if 'method' in subject and 'id' in subject:
                self._dbg("incoming request (%s:%s)",
                          subject['id'], subject['method'])
                try:
                    result = self.dispatch_request(subject)
                    error = None
                except Exception as e:
                    result = None
                    error = RPCErrorResponse(e, for_sending=True)
                self.parent.respond(result, error, subject['id'])
            elif 'id' in subject and ('result' in subject or 'error' in subject):
                self._dbg("incoming %s (%s)",
                          "error" if subject.get("error") else "result",
                          subject['id'])

                recvwait = None
                with self.parent._recvwait_lock:
                    if subject['id'] in self.parent._recv_waiting:
                        recvwait = self.parent._recv_waiting.pop(subject['id'])

                if recvwait:
                    with recvwait['condition']:
                        recvwait['result'] = subject
                        recvwait['condition'].notify_all()
                else:
                    self.dispatch_response(subject)
            elif 'method' in subject:
                self._dbg("incoming notification (%s)", subject['method'])
                try:
                    self.dispatch_notification(subject)
                except Exception:
                    # Notifications have no replies, so logging the error
                    # is the best we can do.
                    logger.exception("%s%s: dispatch_notification error",
                                     self.name, self._remote_address_label())

        def dispatch_request(self, subject):
            pass

        def dispatch_notification(self, subject):
            pass

        def dispatch_response(self, subject):
            """Note: Only used to results for calls that some other thread isn't waiting for"""
            pass

    def _init(self, subject, parent=None, *arg, **kw):
        self._request_id = dispatcher.Count()
        self._recvwait_lock = threading.Lock()
        self._send_lock = threading.Lock()
        self._recv_waiting = {}
        ClientConnection._init(self, subject=subject, parent=parent, *arg, **kw)

    def run_thread(self):
        try:
            super().run_thread()
        except Exception as e:
            self._client_exit(e)
        else:
            self._client_exit(EOFError())

    def request(self, method, params=None, wait_for_response=False, timeout=None):
        if params is not None and not isinstance(params, (list, dict, tuple)):
            raise TypeError("'params' must be a list or dict, or omitted")

        # Prepare the Request ID and the Response awaiter.
        request_id = next(self._request_id)
        if wait_for_response:
            recvwait = {'condition': threading.Condition(), 'result': None}
            with self._recvwait_lock:
                if self._shutdown:
                    recvwait['result'] = RPCErrorResponse(EOFError()).to_result()
                else:
                    self._recv_waiting[request_id] = recvwait

        # Send the Request.
        payload = {'jsonrpc': '2.0', 'method': str(method), 'id': request_id}
        if params:
            payload['params'] = params
        with self._send_lock:
            if not self._shutdown:
                self.writer.write_value(payload)

        # Await the reply (or just return the ID).
        if not wait_for_response:
            return request_id
        else:
            return self._wait_for(recvwait, request_id, timeout, method)

    def _wait_for(self, recvwait, request_id, timeout, method):
        try:
            with recvwait['condition']:
                if not recvwait['result']:
                    recvwait['condition'].wait(timeout)
                if not recvwait['result']:
                    raise TimeoutError(f"RPC timeout on request {request_id}"
                                       f" method '{method}'")

                error = recvwait['result'].get('error')
                if error is not None:
                    exception = error.get('data', {}).get('exception', None)
                    if not isinstance(exception, BaseException):
                        exception = RPCError(error)
                    raise exception

                return recvwait['result']['result']
        finally:
            with self._recvwait_lock:
                if request_id in self._recv_waiting:
                    del self._recv_waiting[request_id]

    def respond(self, result, error, id):
        response = {'jsonrpc': '2.0', 'id': id}
        if error is None:
            response['result'] = result
        else:
            response['error'] = error
        with self._send_lock:
            self.writer.write_value(response)

    def notify(self, method, params=[]):
        with self._send_lock:
            self.writer.write_value({'method': method, 'params': params})

    def _client_exit(self, error):
        """Fail all pending requests."""
        with self._recvwait_lock:
            for recvwait in self._recv_waiting.values():
                with recvwait['condition']:
                    recvwait['result'] = RPCErrorResponse(error).to_result()
                    recvwait['condition'].notify_all()

    def __getattr__(self, name):
        def rpc_wrapper(*arg):
            return self.request(name, list(arg), wait_for_response=True)
        return rpc_wrapper


class RPCServer(dispatcher.ServerConnection):
    """A JSON-RPC server connection manager. This class manages a
    listening sockets and receives and dispatches new inbound
    connections. Each inbound connection is awarded two threads, one
    that can call the other side if there is a need, and one that
    handles incoming requests, responses and notifications.

    RPCServer.Dispatch.Dispatch is an RPCClient subclass that handles
    incoming requests, responses and notifications. Initial calls to
    the remote side can be done from its run_parent() method."""

    class InboundConnection(dispatcher.ThreadedClient):
        class Thread(RPCClient):
            def run_parent(self):
                """Server can call client from here..."""
                pass
