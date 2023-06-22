import random
import pygame


win_width = 1000
win_height = 800
font_px = 15

pygame.init()
winsur = pygame.display.set_mode((win_width, win_height))
font = pygame.font.SysFont('', 23)
bg_surface = pygame.Surface((win_width, win_height), flags=pygame.SRCALPHA)
pygame.Surface.convert(bg_surface)
bg_surface.fill(pygame.Color(0, 0, 0, 28))
winsur.fill((0, 0, 0))

letter = '1234567890!@#$%^&*qwertyuiopasdfghjklzxcvbnm'
texts = [font.render(letter[i], True, (0, 255, 0)) for i in range(44)]

column = int(win_width/font_px)
drops = [0 for i in range(column)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            change = pygame.key.get_pressed()
            if change[32]:
                exit()

    pygame.time.delay(30)

    winsur.blit(bg_surface, (0, 0))
    for i in range(len(drops)):
        text = random.choice(texts)
        winsur.blit(text, (i*font_px, drops[i]*font_px))
        drops[i] += 1
        if drops[i]*10 > win_height or random.random() > 0.95:
            drops[i] = 0
    pygame.display.flip()
