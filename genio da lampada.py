from xml.dom.minidom import Document
from xml.dom.xmlbuilder import DocumentLS
import wikipedia
import re

wikipedia.set_lang("pt")
title = input("Sobre o que voce quer pesquisar? \n")
while True:
    try:
        wiki = wikipedia.page(title)
        break
    except:
        print("Algo deu errado :(")
        title = input("Digite outra pesquisa ou tente \n novamente com outros termos\n")

text = wiki.content
text = re.sub(r'==','', text)
text = re.sub(r'=','',text)
text = re.sub(r'\n','\n', text)
split = text.split('Veja tambem',1)
text = split[0]

print (text)

document = Document()

input()
