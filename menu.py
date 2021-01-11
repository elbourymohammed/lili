
import pygame
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Selection Mode')
scn = pygame.display.set_mode((500, 500),0,32)
 
font = pygame.font.SysFont(None, 20)
 
def draw_for_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def menu():
    while True:
 
        scn.fill((0,0,0))
        draw_for_text(' ↓ Attack Mode : ↓', font, (255, 255, 255), scn, 100, 80)
        draw_for_text(' ↓ Defense Mode : ↓', font, (255, 255, 255), scn, 100, 180)
        draw_for_text(' ↓ Magic Mode : ↓', font, (255, 255, 255), scn, 100, 280)
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                Opt()
        if button_3.collidepoint((mx, my)):
            if click:
                Magic()
        pygame.draw.rect(scn, (255, 0, 0), button_1)
        pygame.draw.rect(scn, (255, 0, 0), button_2)
        pygame.draw.rect(scn, (255, 0, 0), button_3)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    while running:
        scn.fill((0,0,0))
        draw_for_text(' Mode selected : Attack Mode !' , font, (255, 255, 255), scn, 130, 200)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def Opt():
    running = True
    while running:
        scn.fill((0,0,0))
 
        draw_for_text(' Mode selected : Defense Mode !' , font, (255, 255, 255), scn, 130, 200)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
        



def Magic():
    running = True
    while running:
        scn.fill((0,0,0))
 
        draw_for_text(' Mode selected : Magic Mode !' , font, (255, 255, 255), scn, 130, 200)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
menu()