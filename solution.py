import os
import requests
from dotenv import load_dotenv
from folium import Map, Marker, Popup

load_dotenv(".env")

s = requests.Session()
res = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)

par = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha=2506"
)
pos = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1//Posicao/Linha?codigoLinha=2506"
)

posicoes = pos.json()
paradas = par.json()

m = Map(location=[paradas["py"], paradas["px"]], zoom_start=14)
for i in paradas:
    Marker(location=[i["py"], i["px"]], popup=i["np"], icon=folium.Icon(color="red")).add_to(m)
for i in posicoes:
    Marker(location=[i["py"], i["px"]], popup=i["np"], icon=folium.Icon(color="purple")).add_to(m)
m.show_in_browser()

print(res.text)