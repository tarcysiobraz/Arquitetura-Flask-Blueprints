from flask import Blueprint
from flask_restful import Api

from .TarefaResource import TarefaDetail, TarefaList

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(TarefaList, "/tarefas/")
    api.add_resource(TarefaDetail, "/tarefas/<tarefa_id>")
    app.register_blueprint(bp)
