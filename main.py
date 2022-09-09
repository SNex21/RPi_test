import RPi.GPIO as GPIO    #импорт библиотеки для работы с GPIO

import time                #импорт библиотеки для ожидания

GPIO.setmode(GPIO.BOARD)   #"запуск" GPIO

GPIO.setup(7, GPIO.OUT)    #объявление порта 7 как выход

while True:                #бесконечный цикл

    GPIO.output(7, 1)      #включение светодиода

    time.sleep(1)          #ожидание 1 секунды

    GPIO.output(7, 0)      #выключение светодиода

    time.sleep(1)  