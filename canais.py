import json
import requests

class Canal:
    def __init__(self, nome, numero, imagem, idc):
        self.nome = nome
        self.numero = numero
        self.imagem = imagem
        self.idc = idc

def getCanaisArray():
    canaisRequest = requests.get("https://programacao.claro.com.br/gatekeeper/canal/select?q=id_cidade:1&wt=json&rows=30000&start=0&sort=cn_canal+asc&fl=id_canal+st_canal+cn_canal+nome+url_imagem+id_cidade&fq=nome:*&fq=id_categoria:*")
    canaisContent = json.loads(canaisRequest.text)
    canaisArray = {}
    for canal in canaisContent["response"]["docs"]:
        canaisArray[canal["id_canal"]] = Canal(canal["nome"].replace(" ³", ""), canal["cn_canal"], canal["url_imagem"], canal["id_canal"])
    return canaisArray
    



