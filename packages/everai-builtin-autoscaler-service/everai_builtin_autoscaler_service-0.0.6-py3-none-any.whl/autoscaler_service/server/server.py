import logging
import os
import subprocess
import sys
from datetime import datetime, timedelta

import flask
from gevent.pywsgi import WSGIServer
import gevent.signal
import signal

from autoscaler_service import __version__
from everai_autoscaler.builtin import __version__ as builtin_version
from timeloop import Timeloop

from .handler import handler
from .update_builtin import update_builtin

tl: Timeloop = Timeloop()


class Server:
    port: int
    app: flask.Flask
    pid_file: str

    def __init__(self, port: int, pid_file: str, debug: bool = False):
        self.port = port
        self.pid_file = pid_file
        self.app = flask.Flask('autoscaler-service')
        self.app.add_url_rule('/-everai-/autoscaler', methods=['POST'], view_func=handler)

        tl.job(interval=timedelta(seconds=60))(update_builtin)

        level = logging.DEBUG if debug else logging.INFO

        logging.basicConfig(
            handlers=[logging.StreamHandler(stream=sys.stdout)],
            format='[%(asctime)s] %(message)s',
            level=level
        )

    def run_debug_server(self):
        self.app.run(port=self.port)

    def create_pid_file(self) -> bool:
        try:
            os.stat(self.pid_file)
            old_pid = open(self.pid_file, 'r').read()
            print(f'other process already started, pid: {old_pid}, pid_file: {self.pid_file}')
            return False
        except FileNotFoundError as e:
            ...

        pid = os.getpid()
        open(self.pid_file, 'w').write(str(pid))
        return True

    def run_server(self):
        if not self.create_pid_file():
            return

        command_entry = os.path.basename(sys.argv[0])
        print(f'{command_entry} {__version__} starting, everai-builtin-autoscaler version is {builtin_version}')

        server = WSGIServer(('0.0.0.0', self.port), self.app)

        def graceful_stop(*args, **kwargs):
            print(f'Got stop signal, worker do final clear')
            os.remove(self.pid_file)
            tl.stop()
            if server.started:
                server.stop()

        gevent.signal.signal(signal.SIGTERM, graceful_stop)
        gevent.signal.signal(signal.SIGINT, graceful_stop)

        # initial update
        update_builtin()

        tl.start()
        server.serve_forever()

    def run(self):
        self.run_server()
