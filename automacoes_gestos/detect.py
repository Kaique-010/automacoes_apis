import cv2
import mediapipe as mp
import subprocess
import os
import time

import pyautogui
# Inicializa os módulos do MediaPipe para detecção de mãos
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Cria o detector de mãos
hands = mp_hands.Hands()

# Inicializa a captura de vídeo
camera = cv2.VideoCapture(0)
resolution_x = 1280
resolution_y = 720

# Configura a resolução da câmera
camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolution_x)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution_y)

# Dicionário para armazenar os processos a serem ou nõa abertos
processes = {
    "notepad": None,
    "calc": None,
    "mspaint": None,
    "edge": None,
    "spotify_edge": None,
    "spartacus": None,
}

def find_coord_hands(img, side_inverted=True):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    all_hands = []
    
    if result.multi_hand_landmarks:
        for hand_side, hand_landmarks in zip(result.multi_handedness, result.multi_hand_landmarks):
            hand_info = {"Coordenadas": []}
            
            for mark in hand_landmarks.landmark:
                coord_x = int(mark.x * resolution_x)
                coord_y = int(mark.y * resolution_y)
                coord_z = int(mark.z * resolution_x)
                hand_info["Coordenadas"].append((coord_x, coord_y, coord_z))
                
            if side_inverted:
                hand_info["side"] = "Right" if hand_side.classification[0].label == "Left" else "Left"
            else:
                hand_info["side"] = hand_side.classification[0].label
            
            all_hands.append(hand_info)
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    return img, all_hands

def finger_raised(hand):
    return [
        hand['Coordenadas'][fingertip][1] < hand['Coordenadas'][fingertip - 2][1]
        for fingertip in [8, 12, 16, 20]
    ]

"""função de abertura dos aplicativos"""
def start_program(name, command):
    if processes[name] is None:
        processes[name] = subprocess.Popen(command, shell=True)

"""função para fechar os aplicativos"""
def close_program(name, exe_name):
    if processes[name] is not None:
        os.system(f"TASKKILL /F /IM {exe_name}")
        processes[name] = None  # Reseta a variável para permitir abrir de novo

def soma(a, b):
        time.sleep(2)  
        pyautogui.write(str(a))
        time.sleep(3)
        pyautogui.write('+')
        time.sleep(1)
        pyautogui.write(str(b))
        time.sleep(1)
        pyautogui.press('enter')


        
def login_spartacus(usuario, senha):
    time.sleep(8)
    pyautogui.write(usuario)  
    pyautogui.press('tab')  
    pyautogui.write(senha)  
    pyautogui.press('tab')
    time.sleep(4)
    pyautogui.press('enter', 2)

def escrita(text):
    time.sleep(3)
    pyautogui.write(text, interval=0.3)

"""Loop principal"""
while camera.isOpened():
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    
    if not ret:
        continue
    
    img, all_hands = find_coord_hands(frame, False)

    if len(all_hands) == 1:
        info_finger_hand = finger_raised(all_hands[0])

        if info_finger_hand == [True, False, False, True]:  # dedos das pontas
            break    
        elif info_finger_hand == [True, False, False, False]:  # indicador abre notepad
            start_program("notepad", "notepad")
            escrita("Vai Tomar No Cool kkkkkkkk")
        elif info_finger_hand == [True, True, False, False]:  # indicador e médio calculadora
            start_program("calc", "calc")
            soma(10,85)
        elif info_finger_hand == [True, True, True, False]:  # três primeiros Abreem Paint
            start_program("mspaint", "mspaint")
        elif info_finger_hand == [False, True, False, False]:  # Abrir Microsoft Edge dedo médio
            start_program("edge", "start msedge")
        elif info_finger_hand == [False, True, True, False]:  # Abrir Spotify no Edge com os dois médios
            start_program("spotify_edge", "start msedge https://open.spotify.com")
        elif info_finger_hand == [False, False, True, False]:  # Abrir Spartacus anelas
            start_program("spartacus", r'C:\Spartacus Gestao\rtanfegestao.exe')
            login_spartacus('admin', 'roma3030@')

        elif info_finger_hand == [False, False, False, False]: 
            close_program("notepad", "notepad.exe")
            close_program("calc", "CalculatorApp.exe")
            close_program("mspaint", "mspaint.exe")
            close_program("edge", "msedge.exe")
            close_program("spotify_edge", "msedge.exe")  
            close_program("spartacus", "rtanfegestao.exe") 

    cv2.imshow("camera", img)

    if cv2.waitKey(1) == 27:  # Pressionar ESC para sair
        break

# Finalização do programa
camera.release()
cv2.destroyAllWindows()
