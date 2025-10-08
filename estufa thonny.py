import dht
from machine import Pin, ADC, PWM, time_pulse_us
import time
import network
import urequests
import ujson
# Credenciais do WiFi
nome = "Mi CH"
senha = "sp1k3X!0"
# Endereço do Firebase
firebase = "https://greengarden-fd823-default-rtdb.firebaseio.com/"
user = "Estufa-Morango"
url = firebase + user
headers = {
    "Content-Type": "application/json",
}
def conectarWifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando no WiFi...")
        wlan.connect(nome, senha)
        while not wlan.isconnected():
            pass
    print("Wifi conectado... IP: {}".format(wlan.ifconfig()[0]))
def getData():
    response = urequests.get(url + '.json', headers=headers)
    if response.status_code == 200:
        data = ujson.loads(response.text)
        print("Firebase Response:", data)
        response.close()
        return data
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        response.close()
        return None
def enviarFire(data, c=''):
    # monta o caminho corretamente (c pode ser vazio)
    path = '/' + c + '/' if c else '/'
    response = urequests.put(url + path + '.json', data=ujson.dumps(data), headers=headers)
    response.close()
# Configuração dos pinos
bomba = Pin(4, Pin.OUT)      # Controle relé bomba
rele = Pin(25, Pin.OUT)      # Outro relé (se precisar)
comporta = PWM(Pin(26), freq=50)  # Servo comporta
luz = Pin(32, Pin.OUT)       # Luz
# Sensores
trig = Pin(12, Pin.OUT)
echo = Pin(14, Pin.IN)

 
 
tf=dht.DHT11(Pin(33))
 
td=dht.DHT11(Pin(2))
 
umis=Pin(15, Pin.OUT)
lumi=Pin(13, Pin.OUT)
 

conectarWifi()
def set_angle(angle):
    min_us = 500
    max_us = 2500
    us = min_us + (angle / 180) * (max_us - min_us)
    duty = int((us / 20000) * 65535)
    comporta.duty_u16(duty)
def medir_distancia():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    duracao = time_pulse_us(echo, 1, 30000)
    if duracao > 0:
        distancia = (duracao * 0.0343) / 2
    else:
        distancia = -1
    return distancia
while True:
    data = getData()
    if data:
        estado_bomba = data["Acionadores"]["bomba"]
        estado_comporta = data["Acionadores"]["comporta"]
        estado_cooler = data["Acionadores"]["cooler"]
        estado_luz = data["Acionadores"]["luz"]
        distancia = medir_distancia()
        print("Distância medida: {:.2f} cm".format(distancia))
        
        tf.measure()
        tempf = tf.temperature()
        humf = tf.humidity()
        print("Temperatura: {}°C  Umidade: {}%".format(tempf, humf))
        d = {
            "Temperatura_fora":tempf,
#             "Temperatura_dentro":td.read(),
#             "Umidade_solo":umis.read(),
            "Umidade":humf,
#             "Tanque":distancia.read(),
#             "Luminosidade":lumi.read(),
 
        }
        enviarFire(d, 'ValoresSensores')
        # Controle dos atuadores
        if estado_cooler:
            rele.value(0)
        else:
            if tempf >= 26:
                rele.value(0)
            else:
                rele.value(1)

        if estado_bomba:
            bomba.value(0)
        else:
            bomba.value(1)
        if estado_comporta:
            set_angle(90)
        else:
            set_angle(5)
        if estado_luz:
            luz.value(0)
        else:
            luz.value(1)

    time.sleep(1)  # Espera 1 segundo antes da próxima leitura