# Em um terminal Python (python3)
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0) # Usamos 0 para utilizar a webcam padrão do computador

mpHands = mp.solutions.hands # Inicializa o módulo de detecção de mãos
hands = mpHands.Hands() # Inicializa a detecção de mãos

mpDraw = mp.solutions.drawing_utils #Será utilizado para senhar os pontos na mão de acordo com as landmarks

while True:

    success, img = cap.read() # Lê o frame da webcam
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)




    cv2.imshow("Image", img) # Mostra a imagem capturada
    cv2.waitKey(1) # Espera 1 milissegundo para a próxima iteração