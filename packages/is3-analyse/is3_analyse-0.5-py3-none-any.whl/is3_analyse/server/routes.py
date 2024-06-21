from flask import request


from . import analyse_app
from .analyse_server import AnalyseServer
from is3_analyse.core import BaseResult


@analyse_app.route('', methods=['POST'])
def analyse() -> BaseResult:
    input_data = request.get_json()
    server = AnalyseServer.create()
    result = server.run(input_data)
    return result


@analyse_app.route('/test', methods=['GET'])
def test() -> str:
    return "test success"
