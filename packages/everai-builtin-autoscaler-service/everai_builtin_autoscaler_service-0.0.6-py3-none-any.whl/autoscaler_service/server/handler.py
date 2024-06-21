import importlib
import typing

import flask
from autoscaler_service.requests import Requests, Results
import logging
import everai_autoscaler.builtin
from .apply_decorators import apply_decorators

old_version = everai_autoscaler.builtin.__version__


def decide(requests: Requests) -> Results:
    result = apply_decorators(requests)

    try:
        assert requests.name is not None
        assert requests.arguments is not None
        autoscaler = everai_autoscaler.builtin.BuiltinFactory().create(requests.name, requests.arguments or {})
    except Exception as e:
        raise e

    try:
        decide_result = autoscaler.decide(requests.factors)

        if len(decide_result.actions) > 0:
            # do some log for actions
            req_str = requests.json()
            result_str = decide_result.json()
            logging.info(f"request: {req_str}")
            logging.info(f"result: {result_str}")

    except Exception as e:
        raise e

    result.max_workers = decide_result.max_workers or 0
    result.actions = decide_result.actions or []
    return result


def handler():
    global old_version
    curr_version = everai_autoscaler.builtin.__version__
    if old_version != curr_version:
        logging.warning(f"everai_autoscaler.builtin use "
                        f"new version: {curr_version} replace old version: {old_version}")
        old_version = curr_version

    data = flask.request.data

    debug = flask.request.headers.get('X-everai-debug', False)
    if debug:
        logging.info(f"Received request: \n{data}")
    else:
        logging.debug(f"Received request: \n{data}")

    try:
        requests = Requests.from_json(data)
    except Exception as e:
        return f'Bad request, {e}', 400

    try:
        result = decide(requests)
    except Exception as e:
        return f'Bad request, {e}', 400

    return flask.Response(result.json(), mimetype='application/json')
