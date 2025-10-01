from lib import FireKeeper

url : str = "https://greengarden-fd823-default-rtdb.firebaseio.com"
fireKeeper = FireKeeper(url, "Estufa-Morango/ValoresSensores", "http://localhost:8080/sensores",1)


fireKeeper.AddListener("Temperatura_fora")
fireKeeper.AddListener("Temperatura_dentro")
fireKeeper.AddListener("Luminosidade")
fireKeeper.AddListener("Tanque")
fireKeeper.AddListener("Umidade")
fireKeeper.AddListener("Umidade_solo")

while True:
    fireKeeper.ListenOnChange()