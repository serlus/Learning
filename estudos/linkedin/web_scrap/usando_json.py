import urllib.request
import json


def manipula_json():
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    web_url = urllib.request.urlopen(endereco)
    if (web_url.getcode() == 200):
        dados = web_url.read()
        oJSON = json.loads(dados)


        contagem = oJSON["metadata"]["count"]
        print("Contagem: " + str(contagem))

        for local in oJSON["features"]:
            if local["properties"]["place"] == "119 km ESE of Alo, Wallis and Futuna":
                print("***encontrado o local***")
            else:
                print(local["properties"]["place"])

manipula_json()