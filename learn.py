import time

import pygame
import random
from sys import exit

game_score = 0


class Player:
    def __init__(self, snail_rect):
        self.player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
        self.player_rect = self.player_surface.get_rect(midbottom=(90, 300))
        self.snail_rect = snail_rect
        self.gravity = 11
        self.skok = False

    def draw(self, screen, snail_rect, run):
        screen.blit(self.player_surface, self.player_rect)

        if self.skok:
            self.player_rect.y -= self.gravity
            self.gravity -= 0.5
            if self.player_rect.y >= 216:
                self.player_rect.y = 216
                self.skok = False
                self.gravity = 11

        if self.player_rect.colliderect(snail_rect):
            run = False

        return run

    def fizyka(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame:
                self.skok = True


class Snail:
    def __init__(self):
        self.snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

        self.snail_rect = self.snail.get_rect(midbottom=(800, 300))

        self.snail_speed = random.randint(6, 12)

    def draw(self, screen):
        if self.snail_rect.x >= -100:
            self.snail_rect.x -= self.snail_speed
        else:
            self.snail_rect.x = 800
            self.snail_speed = random.randint(6, 12)
        screen.blit(self.snail, self.snail_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))
run = False
pygame.display.set_caption('Jump Game')
clock = pygame.time.Clock()
fps = 75

# start menu
font_start = pygame.font.Font('font/Pixeltype.ttf', 80)
title = font_start.render('Alien Game', True, (179, 224, 255))
title_rect = title.get_rect(center=(400, 40))

player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_rotate = pygame.transform.rotozoom(player_stand, 90,1.5)
rotate_rect = player_rotate.get_rect(center=(400, 200))
player_stand_scale = pygame.transform.scale(player_stand, (200, 200))
player_stand_rect = player_stand_scale.get_rect(center=(400, 180))

start_game_surface = pygame.image.load('graphics/start.png').convert_alpha()
start_game_surface_scale = pygame.transform.scale(start_game_surface, (200, 80))
start_game_rect = start_game_surface_scale.get_rect(center=(400, 350))

# game
font = pygame.font.Font('font/Pixeltype.ttf', 60)
font_big = pygame.font.Font('font/Pixeltype.ttf', 40)
Sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

snail_instance = Snail()
player_instance = Player(snail_instance)


def score():
    global game_score, start_time
    game_score = int(pygame.time.get_ticks() / 1000) - start_time

    score_surface = font.render(f'score: {game_score}', True, 'black')
    screen.blit(score_surface, (320, 100))


start_menu = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        if start_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_game_rect.collidepoint(event.pos):
                    start_time = int(pygame.time.get_ticks() / 1000)
                    run = True
                    start_menu = False
        if not run:
            if event.type == pygame.MOUSEBUTTONUP:
                run = True
                snail_instance.snail_rect.x = 810
                start_time = int(pygame.time.get_ticks() / 1000)
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_ESCAPE:
                    time.sleep(0.5)
                    run = True
                    snail_instance.snail_rect.x = 810
                    start_time = int(pygame.time.get_ticks() / 1000)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        player_instance.fizyka(event)

    if start_menu:
        screen.fill((110, 158, 204))
        screen.blit(start_game_surface_scale, start_game_rect)
        screen.blit(title, title_rect)
        screen.blit(player_stand_scale, player_stand_rect)
        pygame.display.update()

    fps_surface = font.render(f'{round(clock.get_fps())} fps', True, 'black')
    if run and not start_menu:
        screen.blit(Sky, (0, 0))
        screen.blit(ground, (0, 300))
        score()
        screen.blit(fps_surface, (0, 10))

        snail_instance.draw(screen)
        run = player_instance.draw(screen, snail_instance.snail_rect, run)

        pygame.display.update()
        clock.tick(fps)

    # Sprawdzamy, czy run jest False i jeśli tak, to wyświetlamy ekran "Game Over"
    if not run and not start_menu:
        screen.fill((153, 206, 255))
        game_over_surface = font.render('Game Over', True, 'red')
        game_over_rect = game_over_surface.get_rect(center=(400, 40))

        new_score = font.render(f'Score: {game_score}', True, 'red')
        new_score_rect = new_score.get_rect(center=(400, 80))

        best_score = font.render(f'Best score: None', True, 'red')
        best_score_rect = best_score.get_rect(center=(400, 120))

        try_again_surface = font_big.render('click any button to continue', True, 'black')
        try_again_surface_rect = try_again_surface.get_rect(center=(400, 320))

        exit_surface = font_big.render('click Escape to exit', True, 'black')
        exit_surface_rect = exit_surface.get_rect(center=(400, 380))

        screen.blit(game_over_surface, game_over_rect)
        screen.blit(new_score, new_score_rect)
        screen.blit(best_score, best_score_rect)
        screen.blit(player_rotate, rotate_rect)
        screen.blit(try_again_surface, try_again_surface_rect)
        screen.blit(exit_surface, exit_surface_rect)

        pygame.display.update()
