import xml.dom.minidom
import xml.etree.ElementTree as ET
from canais import getCanaisArray
from grade import parseGrade


def formatTime(timeStr):
    tempoFormatado = timeStr.strftime('%Y%m%d%H%M%S -0300')
    return tempoFormatado


def makeXML(file):
    root = ET.Element('tv')
    canaisDb = getCanaisArray()
    canaisId = []
    for canais in canaisDb:
        canaisId.append(canais)
    grade = parseGrade(canaisId)
    for canalAtual in canaisDb:
        channel = canaisDb[canalAtual]
        canal = ET.SubElement(root, 'channel', id=channel.idc)
        canalSub = ET.SubElement(canal, 'display-name')
        canalSub.text = channel.nome
        canalSub = ET.SubElement(canal, 'display-name')
        canalSub.text = channel.numero
        canalSub = ET.SubElement(canal, 'icon', src=channel.imagem)
        try:
            for programa in grade[canalAtual]:
                canal = ET.SubElement(root, 'programme', start=formatTime(programa.inicio), stop=formatTime(programa.fim), channel=canalAtual)
                canalSub = ET.SubElement(canal, 'title', lang="en")
                canalSub.text = programa.titulo
        except Exception as e:
            print(channel.nome, e)
    string_xml = ET.tostring(root, 'utf-8', method="xml")
    exml = xml.dom.minidom.parseString(string_xml)
    with open(file, "w", encoding="utf-8") as xmlFile:
        xmlFile.write(exml.toprettyxml().replace("@@", "&#"))
