import RPi.GPIO as GPIO
import requests
import time

url = "https://industrial.api.ubidots.com/api/v1.6/devices/raspberrypi/porta/values/"
url2 = "https://industrial.api.ubidots.com/api/v1.6/devices/raspberrypi/porta-fecha/values/"

payload = "{\"value\":0}"
payload2 = "{\"value\":1}"
headers = {
    'X-Auth-Token': 'BBFF-t0Dyyg8VFfbbUuxB7u8Mvn5rp3AbS5'
    'Content-Type': 'application/json'
}
response2 = requests.request("POST", url2, headers=headers, data=payload2)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.LOW)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.LOW)

try:
    while True:
        GPIO.output(16, GPIO.HIGH)
        userInput = raw_input('Digite a senha:\n')
        if userInput == 'admin':
            print('Senha correta, porta aberta =)')
            GPIO.output(16, GPIO.LOW)
            GPIO.output(18, GPIO.HIGH)
            payload2 = "{\"value\":0}"
            response2 = requests.request("POST", url2, headers=headers, data=payload2)
            payload = "{\"value\":1}"
            response = requests.request("POST", url, headers=headers, data=payload)
            print('Voce tem 5 segundos para entrar')
            time.sleep(5)
            print('Fechando porta...')
            time.sleep(1)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(16, GPIO.HIGH)
            payload = "{\"value\":0}"
            response = requests.request("POST", url, headers=headers, data=payload)
            payload2 = "{\"value\":1}"
            response2 = requests.request("POST", url2, headers=headers, data=payload2)
            GPIO.output(16, GPIO.LOW)
            break
        else:
            print('Senha incorreta, tente novamente...\n')
            GPIO.output(18, GPIO.LOW)
            GPIO.output(16, GPIO.HIGH)
except:
    GPIO.cleanup()