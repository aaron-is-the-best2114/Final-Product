import pygame
import sys
from pygame.locals import *
import os

pygame.init()

YELLOW = (255,255,0)

myFont = pygame.font.SysFont("monospace", 35)

monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((875, 400))

A = pygame.image.load('img/RFID.png')
B = pygame.image.load('img/LEDBarGraph.png')
C = pygame.image.load('img/RF1.png')
D = pygame.image.load('img/RF2.png')
E = pygame.image.load('img/MAX7219.png')
F = pygame.image.load('img/Buzzer.png')
G = pygame.image.load('img/Motor.png')
H = pygame.image.load('img/ServoMotor.png')
I = pygame.image.load('img/Relay.png')
J = pygame.image.load('img/MicroSwitch.png')
K = pygame.image.load('img/TouchSensor.png')
L = pygame.image.load('img/DHT11.png')
M = pygame.image.load('img/TiltSwitch.png')
N = pygame.image.load('img/SpeedSensor.png')
O = pygame.image.load('img/PIR.png')
P = pygame.image.load('img/MPU6050.png')
Q = pygame.image.load('img/Koname.png')
R = pygame.image.load('img/Joystick.png')
S = pygame.image.load('img/RotaryEncoder.png')
T = pygame.image.load('img/RF3.png')
U = pygame.image.load('img/IR.png')
V = pygame.image.load('img/Keypad.png')
W = pygame.image.load('img/LIGHT.jpg')
X = pygame.image.load('img/ReedSwitch.png')
Y = pygame.image.load('img/Thermistor.png')
Z = pygame.image.load('img/Photoresister.png')
a = pygame.image.load('img/RGB.png')
b = pygame.image.load('img/Button.png')

A = pygame.transform.scale(A, (125, 100))
B = pygame.transform.scale(B, (125, 100))
C = pygame.transform.scale(C, (125, 100))
D = pygame.transform.scale(D, (125, 100))
E = pygame.transform.scale(E, (125, 100))
F = pygame.transform.scale(F, (125, 100))
G = pygame.transform.scale(G, (125, 100))
H = pygame.transform.scale(H, (125, 100))
I = pygame.transform.scale(I, (125, 100))
J = pygame.transform.scale(J, (125, 100))
K = pygame.transform.scale(K, (125, 100))
L = pygame.transform.scale(L, (125, 100))
M = pygame.transform.scale(M, (125, 100))
N = pygame.transform.scale(N, (125, 100))
O = pygame.transform.scale(O, (125, 100))
P = pygame.transform.scale(P, (125, 100))
Q = pygame.transform.scale(Q, (125, 100))
R = pygame.transform.scale(R, (125, 100))
S = pygame.transform.scale(S, (125, 100))
T = pygame.transform.scale(T, (125, 100))
U = pygame.transform.scale(U, (125, 100))
V = pygame.transform.scale(V, (125, 100))
W = pygame.transform.scale(W, (125, 100))
X = pygame.transform.scale(X, (125, 100))
Y = pygame.transform.scale(Y, (125, 100))
Z = pygame.transform.scale(Z, (125, 100))
a = pygame.transform.scale(a, (125, 100))
b = pygame.transform.scale(b, (125, 100))


A_rect = A.get_rect(topleft=(0, 0))
B_rect = B.get_rect(topleft=(125, 0))
C_rect = C.get_rect(topleft=(250, 0))
D_rect = D.get_rect(topleft=(375, 0))
E_rect = E.get_rect(topleft=(500, 0))
F_rect = F.get_rect(topleft=(625, 0))
G_rect = G.get_rect(topleft=(750, 0))
H_rect = H.get_rect(topleft=(0, 100))
I_rect = I.get_rect(topleft=(125, 100))
J_rect = J.get_rect(topleft=(250, 100))
K_rect = K.get_rect(topleft=(375, 100))
L_rect = L.get_rect(topleft=(500, 100))
M_rect = M.get_rect(topleft=(625, 100))
N_rect = N.get_rect(topleft=(750, 100))
O_rect = O.get_rect(topleft=(0, 200))
P_rect = P.get_rect(topleft=(125, 200))
Q_rect = Q.get_rect(topleft=(250, 200))
R_rect = R.get_rect(topleft=(375, 200))
S_rect = S.get_rect(topleft=(500, 200))
T_rect = T.get_rect(topleft=(625, 200))
U_rect = U.get_rect(topleft=(750, 200))
V_rect = V.get_rect(topleft=(0, 300))
W_rect = W.get_rect(topleft=(125, 300))
X_rect = X.get_rect(topleft=(250, 300))
Y_rect = Y.get_rect(topleft=(375, 300))
Z_rect = Z.get_rect(topleft=(500, 300))
a_rect = a.get_rect(topleft=(625, 300))
b_rect = b.get_rect(topleft=(750, 300))

clock = pygame.time.Clock()

fullscreen = False

pygame.display.update()

run = True
while run:

    screen.fill((0, 0, 255))

    screen.blit(A, (0, 0))
    screen.blit(B, (125, 0))
    screen.blit(C, (250, 0))
    screen.blit(D, (375, 0))
    screen.blit(E, (500, 0))
    screen.blit(F, (625, 0))
    screen.blit(G, (750, 0))
    screen.blit(H, (0, 100))
    screen.blit(I, (125, 100))
    screen.blit(J, (250, 100))
    screen.blit(K, (375, 100))
    screen.blit(L, (500, 100))
    screen.blit(M, (625, 100))
    screen.blit(N, (750, 100))
    screen.blit(O, (0, 200))
    screen.blit(P, (125, 200))
    screen.blit(Q, (250, 200))
    screen.blit(R, (375, 200))
    screen.blit(S, (500, 200))
    screen.blit(T, (625, 200))
    screen.blit(U, (750, 200))
    screen.blit(V, (0, 300))
    screen.blit(W, (125, 300))
    screen.blit(X, (250, 300))
    screen.blit(Y, (375, 300))
    screen.blit(Z, (500, 300))
    screen.blit(a, (625, 300))
    screen.blit(b, (750, 300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if A_rect.collidepoint(event.pos):
                print("RFID Sensor")
                file_path = '~/Final-Product/Files/RFID/2.2.10_read.py'
                file_path2 = '~/Final-Product/Files/RFID/2.2.10_write.py'
                command2 = "thonny " + file_path2
                command = "thonny " + file_path
                os.system(command)
                os.system(command2)
            if B_rect.collidepoint(event.pos):
                print("LED Bar Graph")
                file_path = '~/Final-Product/Files/1.1.3_LedBarGraph.py'
                command = "thonny " + file_path
                os.system(command)
            if C_rect.collidepoint(event.pos):
                print("7 Segment Display")
                file_path = '~/Final-Product/Files/1.1.4_7-Segment.py'
                command = "thonny " + file_path
                os.system(command)
            if D_rect.collidepoint(event.pos):
                print("4 Digit 7 Segment Display")
                file_path = '~/Final-Product/Files/1.1.5_4-Digit.py'
                command = "thonny " + file_path
                os.system(command)
            if E_rect.collidepoint(event.pos):
                print("MAX7219 8x8 Matrix Display")
                file_path = '~/Final-Product/Files/1.1.6_LedMatrix'
                command = "thonny " + file_path
                os.system(command)
            if F_rect.collidepoint(event.pos):
                print("Buzzer")
                file_path = '~/Final-Product/Files/Buzzers/'
                command = "thonny " + file_path
                os.system(command)
            if G_rect.collidepoint(event.pos):
                print("5v DC Motor")
                file_path = '~/Final-Product/Files/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if H_rect.collidepoint(event.pos):
                print("Servo Motor")
                file_path = '~/Final-Product/Files/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if I_rect.collidepoint(event.pos):
                print("Relay w/ LED")
                file_path = '~/Final-Product/Files/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if J_rect.collidepoint(event.pos):
                print("Micro Switch")
                file_path = '~/Final-Product/Files/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if K_rect.collidepoint(event.pos):
                print("Touch Switch")
                file_path = '~/Final-Product/Files/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if L_rect.collidepoint(event.pos):
                print("DHT-11 Module")
                file_path = '~/Final-Product/Files/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if M_rect.collidepoint(event.pos):
                print("Tilt Switch")
                file_path = '~/Final-Product/Files/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if N_rect.collidepoint(event.pos):
                print("Speed Sensor")
                file_path = '~/Final-Product/Files/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if O_rect.collidepoint(event.pos):
                print("PIR Motion Sensor")
                file_path = '~/Final-Product/Files/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if P_rect.collidepoint(event.pos):
                print("MPU6050 Module")
                file_path = '~/Final-Product/Files/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if Q_rect.collidepoint(event.pos):
                print("Ultrasonic Sensor")
                file_path = '~/Final-Product/Files/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if R_rect.collidepoint(event.pos):
                print("Joystick Module")
                file_path = '~/Final-Product/Files/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if S_rect.collidepoint(event.pos):
                print("Rotary Encoder")
                file_path = '~/Final-Product/Files/RFID/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if T_rect.collidepoint(event.pos):
                print("Potentiometer w/ LED")
                file_path = '~/Final-Product/Files/RFID/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if U_rect.collidepoint(event.pos):
                print("IR Obstacle Avoidance Sensor")
                file_path = '~/Final-Product/Files/RFID/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if V_rect.collidepoint(event.pos):
                print("Keypad Module")
                file_path = '~/Final-Product/Files/RFID/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if W_rect.collidepoint(event.pos):
                print("WS2812 LED Light Ring")
                file_path = '~/Final-Product/Files/RFID/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if X_rect.collidepoint(event.pos):
                print("Reed Switch Module")
                file_path = '~/Final-Product/Files/RFID/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if Y_rect.collidepoint(event.pos):
                print("Thermistor")
                file_path = '~/Final-Product/Files/RFID/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if Z_rect.collidepoint(event.pos):
                print("Photoresister")
                file_path = '~/Final-Product/Files/RFID/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if a_rect.collidepoint(event.pos):
                print("RGB LED")
                file_path = '~/Final-Product/Files/RFID/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)
            if b_rect.collidepoint(event.pos):
                print("Button")
                file_path = '~/Final-Product/Files/RFID/2.2.10_read.py'
                command = "thonny " + file_path
                os.system(command)

        if event.type == VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    pygame.display.update()

pygame.display.update()

pygame.quit()
