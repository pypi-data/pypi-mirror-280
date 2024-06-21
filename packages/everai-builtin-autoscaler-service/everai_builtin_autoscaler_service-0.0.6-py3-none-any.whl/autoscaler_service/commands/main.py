import sys
from argparse import ArgumentParser, Action, Namespace
import os

from autoscaler_service.requests import Requests
from autoscaler_service.server import Server
from autoscaler_service import __version__
from everai_autoscaler.model import Factors, QueueReason
from everai_autoscaler.builtin import __version__ as builtin_version

COMMAND_ENTRY = 'everai-builtin-autoscaler-service'


class EnvDefault(Action):
    def __init__(self, envvar, required=True, default=None, **kwargs):
        if envvar and envvar in os.environ:
            default = os.environ[envvar]

        if default is not None:
            required = False
        super(EnvDefault, self).__init__(default=default, required=required, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


def show_example(args: Namespace):
    factors = Factors(
        queue_histories={},
        queue={
            QueueReason.QueueDueBusy: 2,
            QueueReason.NotDispatch: 0,
            QueueReason.QueueDueSession: 0,
        },
        workers=[]
    )
    r = Requests(
        name='simple',
        arguments={
            "min_workers": "2",
            "max_workers": "7"
        },
        factors=factors,
    )
    json_str = r.json(exclude_unset=True)
    _ = Requests.from_json(json_str)
    print(json_str)


def start_server(args: Namespace):
    if args.version:
        print(__version__)
        exit(0)

    Server(port=args.port, pid_file=args.pid_file, debug=args.debug).run()


def main():
    command_entry = os.path.basename(sys.argv[0])

    parser = ArgumentParser(
        COMMAND_ENTRY,
        description='everai builtin autoscaler service'
    )
    parser.add_argument('-V', '--version', action='store_true', help='show version and exit')

    parser.add_argument('-p', '--port',
                        action=EnvDefault, type=int, default=80, help='port to listen on', envvar='PORT')
    parser.add_argument('-d', '--debug',
                        action='store_true', default=False, help='enable debug log')
    parser.add_argument('--pid-file', default='/var/run/everai_builtin_autoscaler.pid', help='pid file')
    parser.set_defaults(func=start_server)

    subparser = parser.add_subparsers(help=f'subcommands for {command_entry}')

    example_parser = subparser.add_parser('example', aliases=['e'], help='print json example')
    example_parser.set_defaults(func=show_example)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
