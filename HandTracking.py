# Em um terminal Python (python3)
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0) # Usamos 0 para utilizar a webcam padrão do computador

mpHands = mp.solutions.hands # Inicializa o módulo de detecção de mãos
hands = mpHands.Hands() # Inicializa a detecção de mãos

mpDraw = mp.solutions.drawing_utils #Será utilizado para senhar os pontos na mão de acordo com as landmarks


# Essas variaveis vão ser para calcular o fps
previousTime = 0 
currentTime = 0  

while True:

    success, img = cap.read() # Lê o frame da webcam
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            
            #pegando o id e a landmark da mão
            for id, lm in enumerate(handLms.landmark):

                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height) 
                print(id, cx, cy) # Mostra o id e a posição da landmark


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # Calculo do FPS
    #currentTime = time.time() 
    #fps = 1/(currentTime - previousTime)
    #previousTime = currentTime
    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3) 


    cv2.imshow("Image", img) # Mostra a imagem capturada
    cv2.waitKey(1) # Espera 1 milissegundo para a próxima iteração