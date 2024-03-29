import time
import json
import pygame
import random
from sys import exit

game_score = 0

try:
    with open('score.json', 'r') as json_file:
        score_data = json.load(json_file)
    score_json = score_data["score"]
except:
    score_json = 0


class Player:
    def __init__(self, snail_rect):
        self.player_surface = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
        self.player_walk1 = pygame.image.load("graphics/Player/player_walk_1.png")
        self.player_walk2 = pygame.image.load("graphics/Player/player_walk_2.png")
        self.player_jump = pygame.image.load("graphics/Player/jump.png")
        self.player_list = [self.player_walk1, self.player_walk2]
        self.list_index = 0

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

    def fizyka(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame:
                if self.player_rect.y == 216:
                    skok.play()
                    self.skok = True


class Snail:
    def __init__(self):
        self.snail_speed = random.randint(6, 12)

        self.snail1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
        self.snail2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
        self.snail_list = [self.snail1, self.snail2]
        self.snail_index = 0
        self.snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
        self.snail_rect = self.snail.get_rect(midbottom=(800, 300))

    def draw(self, screen, lista_przeszkod):
        if lista_przeszkod:
            fly_speed = 8
            snail_speed = 7
            for snailx in lista_przeszkod:

                if snailx.y == 160:
                    screen.blit(fly_instance.fly_surface, snailx)
                    snailx.x -= fly_speed

                else:
                    screen.blit(self.snail, snailx)
                    snailx.x -= snail_speed

                lista_przeszkod = [obstacle for obstacle in lista_przeszkod if obstacle.x > -100]
            return lista_przeszkod
        else:
            return []

    def kolize(self, player, obstacles):
        if obstacles:
            for obstacle_rect in obstacles:
                if player.colliderect(obstacle_rect):
                    return False
        return True
    # if self.snail_rect.x >= -100:
    # self.snail_rect.x -= self.snail_speed
    # else:
    # self.snail_rect.x = 800
    # self.snail_speed = random.randint(6, 12)
    # screen.blit(self.snail, self.snail_rect)


class Fly:
    def __init__(self):
        self.fly1 = pygame.image.load("graphics/Fly/Fly1.png")
        self.fly2 = pygame.image.load("graphics/Fly/Fly2.png")
        self.fly_list = [self.fly1, self.fly2]
        self.fly_index = 0
        self.fly_surface = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()


def player_animation():
    if player_instance.player_rect.y >= 216:
        player_instance.list_index += 0.1
        if player_instance.list_index >= len(player_instance.player_list):
            player_instance.list_index = 0
        player_instance.player_surface = player_instance.player_list[int(player_instance.list_index)]
    else:
        player_instance.player_surface = player_instance.player_jump


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('audio/music.wav')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)
skok = pygame.mixer.Sound('audio/jump.mp3')
skok.set_volume(0.05)
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
player_rotate = pygame.transform.rotozoom(player_stand, 90, 1.5)
rotate_rect = player_rotate.get_rect(center=(400, 250))
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
fly_instance = Fly()
# TIMER
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1100)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 100)

fly_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_animation_timer, 100)
# przeszkody

lista_przeszkod = []


def score():
    global game_score, start_time
    game_score = int(pygame.time.get_ticks() / 1000) - start_time

    score_surface = font.render(f'score: {game_score}', True, 'black')
    screen.blit(score_surface, (320, 100))


start_menu = True

while True:
    for event in pygame.event.get():
        if run and not start_menu:
            player_instance.fizyka(event)
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
                player_instance.player_rect.y = 216
                run = True
                data = {"score": game_score}
                with open('score.json', 'w') as new_json:
                    json.dump(data, new_json)

                lista_przeszkod.clear()
                start_time = int(pygame.time.get_ticks() / 1000)
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_ESCAPE:
                    time.sleep(0.5)

                    player_instance.player_rect.y = 216
                    run = True

                    lista_przeszkod.clear()
                    snail_instance.snail_rect.x = 810
                    start_time = int(pygame.time.get_ticks() / 1000)
                    data = {"score": game_score}
                    with open('score.json', 'w') as new_json:
                        json.dump(data, new_json)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        if run:

            if event.type == obstacle_timer:
                if random.randint(0, 1):
                    lista_przeszkod.append(snail_instance.snail.get_rect(bottomright=(random.randint(900, 1100), 300)))
                else:
                    lista_przeszkod.append(
                        fly_instance.fly_surface.get_rect(bottomright=(random.randint(700, 1000), 200)))
            if event.type == snail_animation_timer:
                snail_instance.snail_index += 1
                if int(snail_instance.snail_index) >= len(snail_instance.snail_list):
                    snail_instance.snail_index = 0

                snail_instance.snail = snail_instance.snail_list[snail_instance.snail_index]
            if event.type == fly_animation_timer:
                fly_instance.fly_index += 1
                if int(fly_instance.fly_index) >= len(fly_instance.fly_list):
                    fly_instance.fly_index = 0

                fly_instance.fly_surface = fly_instance.fly_list[fly_instance.fly_index]
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
        player_animation()
        lista_przeszkod = snail_instance.draw(screen, lista_przeszkod)
        player_instance.draw(screen, snail_instance.snail_rect, run)

        run = snail_instance.kolize(player_instance.player_rect, lista_przeszkod)
        pygame.display.update()

        clock.tick(fps)

    # Sprawdzamy, czy run jest False i jeśli tak, to wyświetlamy ekran "Game Over"
    if not run and not start_menu:
        try:
            with open('score.json', 'r') as json_file:
                score_data = json.load(json_file)
            score_json = score_data["score"]
        except:
            score_json = 0

        screen.fill((153, 206, 255))
        game_over_surface = font.render('Game Over', True, 'red')
        game_over_rect = game_over_surface.get_rect(center=(400, 80))
        new_score = font.render(f'Score: {game_score}', True, 'red')
        new_score_rect = new_score.get_rect(center=(400, 120))
        best_score = font.render(f'Best score: {score_json}', True, 'red')
        best_score_rect = best_score.get_rect(center=(400, 160))
        try_again_surface = font_big.render('click any button to continue', True, 'black')
        try_again_surface_rect = try_again_surface.get_rect(center=(400, 350))
        exit_surface = font_big.render('click Escape to exit', True, 'black')
        exit_surface_rect = exit_surface.get_rect(center=(400, 380))
        print(game_score)
        print(score_json)
        if game_score >= score_json:

                new_best_score = font.render('NEW BEST SCORE!', True, 'green')
                new_best_score_rect = new_best_score.get_rect(center=(400, 30))
                if game_score != score_json:
                    screen.blit(new_best_score, new_best_score_rect)


        screen.blit(game_over_surface, game_over_rect)
        screen.blit(new_score, new_score_rect)
        screen.blit(best_score, best_score_rect)
        screen.blit(player_rotate, rotate_rect)
        screen.blit(try_again_surface, try_again_surface_rect)
        screen.blit(exit_surface, exit_surface_rect)
        pygame.display.update()
