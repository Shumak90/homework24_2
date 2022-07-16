import os
from utils import query
from flask import Flask, request, abort, Response

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query")
def perform_query() -> Response:
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    file_name = request.args.get('file_name')
    cmd1 = request.args.get('cmd1')
    cmd2 = request.args.get('cmd2')
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    if not (cmd1 and value1 and file_name and cmd2 and value2):
        return abort(400, 'cmd1 and value1 and file_name and cmd2 and value2')

    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    file = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file):
        return abort(400, " file_name is not data")

    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат

    with open(file) as f:
        res = query(cmd1, value1, f)
        res = query(cmd2, value2, res)
        res = '\n'.join(res)
    return app.response_class(res, content_type="text/plain")


if __name__ == "__main__":
    app.run(debug=True)