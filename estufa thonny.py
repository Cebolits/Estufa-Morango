from machine import Pin, ADC,PWM,time_pulse_us
import time
import network
import urequests
import ujson
import dht
import socket

#ultrasom
TRIG = Pin(18, Pin.OUT)
ECHO = Pin(19, Pin.IN)

def get_distance():
    # Dispara pulso
    TRIG.value(0)
    time.sleep_us(5)
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)
    print("pulso enviado")
    
    # Mede tempo em microssegundos
    duracao = time_pulse_us(ECHO, 1, 60000)
    
    
    if duracao < 0:
        return None  # erro na leitura

    # Calcula distância em cm
    return (duracao * 0.0343) / 2 

 
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
 
# Conectar-se ao WiFi

def conectarWifi():

    wlan = network.WLAN(network.STA_IF)

    wlan.active(True)

    if not wlan.isconnected():

        print("Conectando no WiFi...")

        wlan.connect(nome, senha)

        while not wlan.isconnected():

            pass

    print("Wifi conectado... IP: {}".format(wlan.ifconfig()[0]))
 
# Função para obter dados do Firebase

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

# Função para enviar dados para o Firebase

def enviarFire(data):

    response = urequests.put(url + '/' + '.json', data=ujson.dumps(data), headers=headers)

    response.close()
 
# Configura o pino dos acionados

fora = dht.DHT11(Pin(26))
dentro = dht.DHT11(Pin(27))
rele = Pin(25, Pin.OUT, 0)  # Definindo o pino de controle da bomba (pino 25)
comporta = PWM(Pin(12), freq=50)  # Definindo o pino de controle da comporta (pino 26)
luz = Pin(32, Pin.OUT, 0)  # Definindo o pino de controle da luz (pino 32)
bomba=Pin(33, Pin.OUT, 0)
ldr = ADC(Pin(34))  # Definindo o pino de sensor da luz (pino 34)
 
conectarWifi()
 
 
def set_angle(angle):

    # Converte ângulo em ciclo ativo

    min_us = 500   # 0.5ms

    max_us = 2500  # 2.5ms

    us = min_us + (angle / 180) * (max_us - min_us)

    duty = int((us / 20000) * 65535)  # 20ms período

    comporta.duty_u16(duty)

# Loop principal

while True:
    
    # Pegando os valores dos acionadores
    data = getData()

    if getData:

        # Se os dados foram recuperados com sucesso

        estado_bomba = data["Acionadores"]["bomba"]

        estado_comporta = data["Acionadores"]["comporta"]

        estado_cooler = data["Acionadores"]["cooler"]

        estado_luz = data["Acionadores"]["luz"]
 
        # Aciona ou desliga a bomba com base no valor recebido do Firebase

        if estado_bomba:

            bomba.value(0)

        else:

            bomba.value(1)

        # Aciona ou desliga a comporta com base no valor recebido do Firebase

        if estado_comporta:

            set_angle(90)  # Abre

        else:

            set_angle(5)   # Fecha


        if estado_cooler:

            rele.value(0)

        else:

            rele.value(1)
            
        if estado_luz:

            luz.value(0)

        else:

            luz.value(1)
            
        dist = get_distance()
    if dist:
        print("Distancia: {:.2f} cm".format(dist))
    else:
        print("Erro de leitura")


    # Pegando os valores dos sensores
    
    ldr_ = ldr.read()
    try:
        
        fora.measure()
        tempf = fora.temperature()
        humf = fora.humidity()

        
        print("TEMPf:", tempf,"°C")
        print("Humif:", humf, "%")
        
        dentro.measure()
        tempd = dentro.temperature()
        humd = dentro.humidity()

        
        print("TEMPd:", tempd,"°C")
        print("Humid:", humd, "%")

       
       
    except OSError as e:
        print("falha: ", e)

    
    
    print(ldr_)
    
    


    # Aguarda um segundo antes de verificar novamente

    time.sleep_ms(100)

 