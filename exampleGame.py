import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm


# Essas variaveis vão ser para calcular o fps
previousTime = 0
currentTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()  # Inicializa o detector de mãos

while True:

    success, img = cap.read()  # Lê o frame da webcam
    img = detector.findHands(img)

    lmList = detector.findPosition(img)  # Encontra as posições das mãos
    if len(lmList) != 0:
        print(lmList[4])  # Posição do dedo indicador

    # Calculo do FPS
    currentTime = time.time()
    fps = 1/(currentTime - previousTime)
    previousTime = currentTime
    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    cv2.imshow("Image", img)  # Mostra a imagem capturada
    cv2.waitKey(1)  # Espera 1 milissegundo para a próxima iteração
