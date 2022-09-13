from flask import Blueprint
from flask_restful import Resource


# rotas sem parâmetros
class TarefaList(Resource):
    def get(self):
        return {"Hello":"World"}
# rotas com parâmetros
class TarefaDetail(Resource):
    ...


