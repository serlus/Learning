import xml.dom.minidom
    """verificar quais
    """

def manipula_XML():
    doc = xml.dom.minidom.parse("/home/serlus/repositorios/Learning/estudos/linkedin/web_scrap/exemplo.xml")

    print("Nome da primeira tag: ", str(doc.firstChild.tagName))

    primeiro_nome = doc.getElementsByTagName("firstname")
    print("O primeiro nome é: ", primeiro_nome[0].firstChild.nodeValue)

    for skill in doc.getElementsByTagName("skill"):
        print("Skill encontrada: ", skill.getAttribute("name"))


manipula_XML()
