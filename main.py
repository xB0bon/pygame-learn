import random
import pygame
from sys import exit

pygame.init()  # inicjacja biblioteki
pygame.mixer.init()
pygame.mixer.music.load('audio/music.wav')
pygame.mixer.music.set_volume(0.1)
jump_sound = pygame.mixer.Sound('audio/jump.mp3')
jump_sound.set_volume(0.1)
pygame.mixer.music.play()
window = pygame.display.set_mode((800, 400))  # tworzenie okna
pygame.display.set_caption('First game')  # tytuł gry
game_active = True
clock = pygame.time.Clock()

# blok

# test_surface = pygame.Surface((400, 200))
# test_surface.fill('#ff812b')

# zdjęcie
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

font = pygame.font.Font('font/Pixeltype.ttf', 50)
font_end = pygame.font.Font('font/Pixeltype.ttf', 200)
score_surface = font.render('My game', True, (0, 0, 0))
score_rect = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(500, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
gravity = 0
x = 1
speed = 2
snail_speed = 9
while True:
    for event in pygame.event.get():  # Wszystkie wykonane wydarzenia. np. wyjscie z aplikacji
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # bezpieczne zamkniecie
        # PRZYCISKI
        if game_active:
            if event.type == pygame.KEYDOWN:
                print('clicked')

                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    jump_sound.play()
                    gravity = -20

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if player_rect.collidepoint(pos):
                    if pygame.mouse.get_pressed():
                        gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True


        # if event.type == pygame.MOUSEMOTION:  # jeśli ruszasz myszką
        # if event.type == pygame.MOUSEBUTTONDOWN: # gdy klikniemy myszką
        # if event.type == pygame.MOUSEBUTTONUP: # gdy puścimy kliknietą myszkę
        # print('mouse down') # pozycja myszy
        #
        # if player_rect.collidepoint(pos): print('kolizja 1')
    if game_active:
        window.blit(sky_surface, (0, 0))  # cords
        window.blit(ground_surface, (0, 300))
        fps_surface = font.render(f'fps: {round(clock.get_fps())}', True, (0, 0, 0))
        window.blit(fps_surface, (0, 0))
        window.blit(snail_surface, snail_rect)
        snail_rect.left -= snail_speed
        if snail_rect.left < -100:
            snail_rect.left = 800
            snail_speed = random.randint(5,15)

        # PLAYER
        gravity += x
        player_rect.y += gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        window.blit(player_surface, player_rect)

        pygame.draw.rect(window, '#6bffdf', score_rect, 16, 10)
        # pygame.draw.line(window, 'yellow', (0, 0), (300,100), 30) # rysowanie lini
        window.blit(score_surface, score_rect)

        #END GAME
        if snail_rect.colliderect(player_rect):
            game_active = False
        # if player_rect.colliderect(snail_rect):  # True, False
        #   print('kolizja')

        # pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(pos):
        # print('kolizja')
    else:
        snail_rect.x = 500
        pygame.mixer.music.stop()
        window.fill('black')
        END = font_end.render('GAME OVER', True, (255, 0, 0))
        info = font.render('click space to restart', True, (255, 255, 255))
        window.blit(END, (100, 150))
        window.blit(info, (100, 250))
    pygame.display.update()
    clock.tick(60)  # 60fps, pętla nie działa więcej niz 60 fps
