# Em um terminal Python (python3)
import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands  # Inicializa o módulo de detecção de mãos
        # Inicializa a detecção de mãos
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    
    def findPosition(self, img, handNo=0, draw=True):
        lmList = [] #Lista de landmarks que vamos retornar

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            
            for id, lm in enumerate(myHand.landmark):

                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)


        return lmList



def main():

    # Essas variaveis vão ser para calcular o fps
    previousTime = 0
    currentTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()  # Inicializa o detector de mãos

    while True:

        success, img = cap.read()  # Lê o frame da webcam
        img = detector.findHands(img)

        lmList = detector.findPosition(img)  # Encontra as posições das mãos
        if len(lmList) != 0:
            print(lmList[4]) # Posição do dedo indicador

        # Calculo do FPS
        currentTime = time.time()
        fps = 1/(currentTime - previousTime)
        previousTime = currentTime
        cv2.putText(img, str(int(fps)), (10, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)  # Mostra a imagem capturada
        cv2.waitKey(1)  # Espera 1 milissegundo para a próxima iteração


if __name__ == "__main__":
    main()
