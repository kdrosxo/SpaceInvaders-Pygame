import pygame
import os
pygame.font.init()
WIDTH,HEIGHT = 750,750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space shooter game")


RED_SPACESHIP = pygame.image.load(os.path.join("assets","pixel_ship_red_small.png"))
GREEN_SPACESHIP = pygame.image.load(os.path.join("assets","pixel_ship_green_small.png"))
BLUE_SPACESHIP = pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))
YELLOW_SPACESHIP = pygame.image.load(os.path.join("assets","pixel_ship_yellow.png"))

RED_LASER = pygame.image.load(os.path.join("assets","pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets","pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets","pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets","pixel_laser_yellow.png"))

BG = RED_LASER = pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")),(WIDTH,HEIGHT))

class Ship:
    def __init__(self,x,y,color,health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = []
        self.lasers = []
        self.cooldown_counter = 0

    def draw(self,window):
        window.blit(self.ship_img,(self.x,self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_img = YELLOW_SPACESHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)   #Crop the image hitbox ,for pixel perfect collision
        self.max_health = health

class Enemy(Ship):
    COLOR_MAP = {"red":(RED_SPACESHIP,RED_LASER),
            "green":(GREEN_SPACESHIP,GREEN_LASER),
            "blue":(BLUE_SPACESHIP,BLUE_LASER)
                }

    def __init__(self,x,y,color,health=100):
        super().__init__(x,y,health)
        self.ship_img,self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self,vel):
        self.y += val
