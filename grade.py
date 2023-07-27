import json
import requests
from datetime import datetime, timedelta


class Programa:
    def __init__(self, inicio, fim, canal, titulo, reprise):
        self.inicio = inicio
        self.fim = fim
        self.canal = canal
        self.titulo = titulo
        self.reprise = reprise

    def reprisar(self):
        self.reprise = True


def parseTime(timeStr):
    gradeTimeParse = datetime.strptime(timeStr, '%Y-%m-%dT%H:%MZ')  # iso8601
    return gradeTimeParse


def formatTime(timeStr):
    tempoFormatado = timeStr.strftime('%Y-%m-%dT%H:%M:%SZ')
    return tempoFormatado


def parseGrade(canais):
    canalStr = ""
    for canal in canais:
        canalStr += f"1_{canal}+"
    inicio = formatTime(datetime.now())
    fim = formatTime(datetime.now() + timedelta(days=1))
    url = f"https://programacao.claro.com.br/gatekeeper/exibicao/select?q=id_revel:({canalStr})+AND+id_cidade:1&wt=json&rows=200000&start=0&sort=id_canal+asc,dh_inicio+asc&fl=dh_fim+dh_inicio+st_titulo+titulo+id_programa+id_canal+id_cidade&fq=dh_inicio:[{inicio}+TO+{fim}]"
    gradeRequest = requests.get(url)
    gradeParse = json.loads(gradeRequest.text)
    gradeContent = {}
    for programa in gradeParse["response"]["docs"]:
        if not (programa['id_canal'] in gradeContent):
            gradeContent[programa['id_canal']] = []
        gradeContent[programa['id_canal']].append(Programa(parseTime(programa['dh_inicio']), parseTime(programa['dh_fim']), programa['id_canal'], programa['titulo'], False))
    return gradeContent
