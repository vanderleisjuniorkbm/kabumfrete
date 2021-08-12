from flask import Flask
from flask_restx import Api, Resource
from src.server.instance import server
from src.controllers.shipping_methods import *

app = server.app
api = server.api

@api.route("/shipping")
class Shipping(Resource):
    def post(self, ):
        response = api.payload

        #Aqui é validado o payload
        if "dimensao" not in response:
            return {"status": "dimensao is missing"}

        if "altura" not in response['dimensao']:
            return {"status": "altura is missing"}

        if "largura" not in response['dimensao']:
            return {"status": "largura is missing"}

        if "peso" not in response:
            return {"status": "peso is missing"}

        altura = response['dimensao']['altura']
        largura = response['dimensao']['largura']
        peso = response['peso']
        retorno = []

        #Aqui é calculado o frete e adicionado ao retorno
        kabum = calcula_frete_kabum(altura, largura, peso)
        if kabum:
            retorno.append(kabum)
        ninja = calcula_frete_ninja(altura, largura, peso)
        if ninja:
            retorno.append(ninja)
        return retorno