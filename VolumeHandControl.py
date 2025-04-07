import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
import math
import pulsectl #Tivemos que instalar o pulsectl para controlar o volume do sistema porque o pycaw não funciona no linux
import numpy as np

#Variáveis de fps
previousTime = 0
currentTime = 0

cap = cv2.VideoCapture(0) #Camera padrão

# Inicializa o detector de mãos
detector = htm.handDetector()

# Inicializa o controle de volume
pulse = pulsectl.Pulse('volume-control')
sink = pulse.sink_list()[0]  #Primeiro dispositivo de saída



while True:
    success, img = cap.read()
    img = detector.findHands(img)

    lmList = detector.findPosition(img)

    if len(lmList) != 0:

        #Pegando a posição dos dedos
        x1, y1 = lmList[4][1], lmList[4][2] 
        x2, y2 = lmList[8][1], lmList[8][2]

        #Desenhando um circulo nos dedos
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)

        #Desenhando uma linha entre os dedos
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        #Pegando o centro da linha, desenhando uma bola e calculando a hipotenusa
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        # Mapeia a distância entre os dedos para o volume
        vol = np.interp(length, [30, 200], [0.0, 1.0])
        vol = min(max(vol, 0.0), 1.0)
        pulse.volume_set_all_chans(sink, vol)

        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)

        #Sidebar para ver o volume
        cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
        bar = np.interp(vol, [0.0, 1.0], [400, 150])
        cv2.rectangle(img, (50, int(bar)), (85, 400), (255, 0, 0), cv2.FILLED)


        print(length)


    #Cálculo de fps
    currentTime = time.time()
    fps = 1/(currentTime - previousTime)
    previousTime = currentTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
