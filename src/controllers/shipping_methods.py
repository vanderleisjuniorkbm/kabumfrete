def calcula_frete_ninja(altura, largura, peso):
    valida_frete = _valida_dimensoes_ninja(altura, largura, peso)
    if valida_frete:
        constante = 0.3
        prazo = 6
        preco = (peso*constante)/10
        mapping = {"nome": "Ninja", 
                    "preco": preco,
                    "prazo": prazo}            
        return mapping

def _valida_dimensoes_ninja(altura, largura, peso):
    if 10 <= altura <= 200 and 6 <= largura <= 140 and peso > 0:
        return True
    else:
        return False
        
def calcula_frete_kabum(altura, largura, peso):
    valida_frete = _valida_dimensoes_kabum(altura, largura, peso)
    if not valida_frete:
        return {}
    constante = 0.2
    preco = (peso*constante)/10
    prazo = 4
    mapping = {"nome": "KaBuM", 
                "preco": preco,
                "prazo": prazo}

    return mapping

def _valida_dimensoes_kabum(altura, largura, peso):
    if 5 <= altura <= 140 and 13 <= largura <= 125 and peso > 0: 
        return True
    else:
        return False

        
# {
#     "Ninja":{
#         "name":"Ninja",
#         "shipping_factor": 0.3,
#         "min_height": 10,
#         "max_height": 200,
#         "min_width": 6,
#         "max_width": 140,
#         "delivery_time": 6

#     },
#     "KaBuM":
#     {
#         "name":"KaBuM",
#         "shipping_factor": 0.2,
#         "min_height": 5,
#         "max_height": 140,
#         "min_width": 13,
#         "max_width": 125,
#         "delivery_time": 4
#     }
# }