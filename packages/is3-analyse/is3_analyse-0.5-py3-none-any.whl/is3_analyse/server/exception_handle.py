from flask import jsonify


from . import analyse_app
from is3_analyse.core import to_json_serializable, failed, ApiException


@analyse_app.errorhandler(ApiException)
def handle_error(e):
    error_res = to_json_serializable(failed(message=str(e)))
    print(error_res)
    return jsonify(error_res)
