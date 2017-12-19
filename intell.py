import pygame, sys
from gpiozero import LEDBoard
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from pygame.locals import *


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.init()

BLACK = (0,0,0)
WIDTH = 100
HEIGHT = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

screen.fill(BLACK)

piano_c1 = pygame.mixer.Sound("piano/c1.wav")
piano_d1 = pygame.mixer.Sound("piano/d1.wav")

factory = PiGPIOFactory(host='192.168.1.114')
tree_1 = LEDBoard(*range(2,28,2),pwm=True, pin_factory=factory)
tree_2 = LEDBoard(*range(3,28,2),pwm=True, pin_factory=factory)

note = pygame.font.SysFont("monospace", 36)


def write_note(n):
    label = note.render(n, False, (0,0,0))
    screen.fill(BLACK)
    screen.blit(label, (0,0))

def tree_1_on():
    for l in tree_1:
        l.on()
    sleep(0.5)
    for l in tree_1:
        l.off()

def tree_2_on():
    for l in tree_2:
        l.on()
    sleep(0.5)
    for l in tree_2:
        l.off()

while True:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                piano_c1.play()
                tree_1_on()
                write_note("C1")
            elif event.key == pygame.K_DOWN:
                piano_d1.play()
                tree_2_on()
            elif event.key == pygame.K_UP:
                break
