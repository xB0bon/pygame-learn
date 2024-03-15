import pygame
from sys import exit

pygame.init()  # inicjacja biblioteki
window = pygame.display.set_mode((800, 400))  # tworzenie okna
pygame.display.set_caption('First game')  # tytuł gry

clock = pygame.time.Clock()

# blok

# test_surface = pygame.Surface((400, 200))
# test_surface.fill('#ff812b')

# zdjęcie
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = font.render('My Game', True, (0, 0, 0))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(100, 300))


player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
while True:
    for event in pygame.event.get():  # Wszystkie wykonane wydarzenia. np. wyjscie z aplikacji
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # bezpieczne zamkniecie

    window.blit(sky_surface, (0, 0))  # cords
    window.blit(ground_surface, (0, 300))
    window.blit(text_surface, (350, 60))
    fps_surface = font.render(f'fps: {round(clock.get_fps())}', True, (0, 0, 0))
    window.blit(fps_surface, (0, 0))
    window.blit(snail_surface, snail_rect)
    snail_rect.left -= 4
    if snail_rect.left < -100: snail_rect.left = 800
    window.blit(player_surface, player_rect)

    player_rect.right += 2
    pygame.display.update()
    clock.tick(60)  # 60fps, pętla nie działa więcej niz 60 fps
