# v0.8
# Unfinished GUI for Tres-project.
# Next steps:
# 1. Improve commenting code
# 2. Implement actual gameplay
# 3. Add balls in arrows when adding piece is available
# 4. Start building ai

import pygame
import math


class BoardGUI:

    def __init__(self):
        # color code:
        # 0 for nothing
        # 1 for yellow
        # 2 for blue
        # 3 for grey
        pygame.init()

        # same lists as in tres.py. Affected in tres.py and copied in here.
        # Need to think if I should remove these and just use get method for
        # drawing original lists from tres.py
        self.outer_ring = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.middle_ring = [0, 2, 0, 0, 0, 0, 0, 0]
        self.inner_ring = [0, 0, 1, 3]
        self.center = [2]

        # tells if player is placing piece or choosing what ring to rotate
        # 0 = waiting for piece to be placed
        # 1 = waiting for ring to be rotated ie. tilt ring by mouse position
        self.game_state = 1
        
        # 0 for no winners yet ie game continues
        # 1 for yellow winning
        # 2 for blue winning
        self.win_state = 0

        self.screen = pygame.display.set_mode((1000, 800))

        self.clock = pygame.time.Clock()

        self.mouseX, self.mouseY = 0, 0

        self.distance = 1000

        # bulk of images to be loaded and scaled and rotated
        self.inner = pygame.image.load("keskus.png")
        self.middle = pygame.image.load("keski.png")
        self.outer = pygame.image.load("ulommainen.png")
        self.grey = pygame.image.load("harmaa.png")
        self.blue = pygame.image.load("sininen.png")
        self.yellow = pygame.image.load("keltainen.png")
        self.arrow = pygame.image.load("nuoli2.png")
        self.inner.set_colorkey((255, 255, 255))
        self.middle.set_colorkey((255, 255, 255))
        self.outer.set_colorkey((255, 255, 255))
        self.grey.set_colorkey((255, 255, 255))
        self.blue.set_colorkey((255, 255, 255))
        self.yellow.set_colorkey((255, 255, 255))
        self.arrow.set_colorkey((255, 255, 255))

        self.arrownw = pygame.transform.rotate(self.arrow, -45)
        self.arrowne = pygame.transform.rotate(self.arrow, 225)
        self.arrowse = pygame.transform.rotate(self.arrow, 135)
        self.arrowsw = pygame.transform.rotate(self.arrow, 45)

        self.inner = pygame.transform.scale(self.inner, (225, 225))
        self.middle = pygame.transform.scale(self.middle, (375, 375))
        self.outer = pygame.transform.scale(self.outer, (525, 525))
        self.grey = pygame.transform.scale(self.grey, (70, 70))
        self.blue = pygame.transform.scale(self.blue, (70, 70))
        self.yellow = pygame.transform.scale(self.yellow, (70, 70))

        # I "saved time and money" by drawing everything with windows paint,
        # and now original inner ring is drawn in wrong angle and this is
        # best way to rotate it right
        self.rInner = pygame.transform.rotate(self.inner, 45)

        self.new_game()
    
    def new_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            
            self.mouseX = pygame.mouse.get_pos()[0]
            self.mouseY = pygame.mouse.get_pos()[1]

            self.distance = math.sqrt((self.mouseX - 500)**2 + (self.mouseY-400)**2)

            self.screen.fill((0, 0, 0))

            self.draw_rings()
            
            self.draw_arrows()

            self.draw_all_pieces()
            
            pygame.display.flip()
            self.clock.tick(30)

    def set_outer_ring(self, lista: list):
        self.outer_ring = lista

    def set_middle_ring(self, lista: list):
        self.inner_ring = lista

    def set_inner_ring(self, lista: list):
        self.inner_ring = lista

    def set_center(self, lista: list):
        self.center = lista

    def set_game_state(self):
        if self.game_state == 0:
            self.game_state = 1
        else:
            self.game_state = 0

    def draw_arrows(self):
        if self.game_state == 0:
            self.screen.blit(self.arrownw, (144, 34))
            pygame.draw.circle(self.screen, (0, 255, 0), (275, 170), 20)

            self.screen.blit(self.arrowsw, (135, 520))
            pygame.draw.circle(self.screen, (0, 255, 0), (270, 630), 20)

            self.screen.blit(self.arrowne, (624, 41))
            pygame.draw.circle(self.screen, (0, 255, 0), (727, 170), 20)

            self.screen.blit(self.arrowse, (620, 530))
            pygame.draw.circle(self.screen, (0, 255, 0), (730, 633), 20)
        if self.game_state == 1:
            self.screen.blit(self.arrownw, (144, 34))
            self.screen.blit(self.arrowsw, (135, 520))
            self.screen.blit(self.arrowne, (624, 41))
            self.screen.blit(self.arrowse, (620, 530))

    def draw_rings(self):
        if self.game_state == 0:
            self.screen.blit(self.rInner, self.rInner.get_rect(
                center=(500, 400)).topleft)
            self.screen.blit(self.middle, self.middle.get_rect(
                center=(500, 400)).topleft)
            self.screen.blit(self.outer, self.outer.get_rect(
                center=(500, 400)).topleft)
        if self.game_state == 1:
            if self.distance > 110:
                self.screen.blit(self.rInner, self.rInner.get_rect(
                    center=(500, 400)).topleft)
            else:
                self.rrInner = pygame.transform.rotate(self.inner, 15)
                self.screen.blit(self.rrInner, self.rrInner.get_rect(
                    center=(500, 400)).topleft)

            if self.distance > 180 or self.distance < 110:
                self.screen.blit(self.middle, self.middle.get_rect(
                    center=(500, 400)).topleft)
            else:
                self.rMiddle = pygame.transform.rotate(self.middle, 20)
                self.screen.blit(self.rMiddle, self.rMiddle.get_rect(
                    center=(500, 400)).topleft)

            if self.distance > 253 or self.distance < 180:
                self.screen.blit(self.outer, self.outer.get_rect(
                    center=(500, 400)).topleft)
            else:
                self.rOuter = pygame.transform.rotate(self.outer, 10)
                self.screen.blit(self.rOuter, self.rOuter.get_rect(
                    center=(500, 400)).topleft)

    def draw_center_piece(self, color: int):
        if color == 1:
            self.screen.blit(self.yellow, self.yellow.get_rect(
                center=(500, 400)).topleft)
        elif color == 2:
            self.screen.blit(self.blue, self.blue.get_rect(
                center=(500, 400)).topleft)
        elif color == 3:
            self.screen.blit(self.grey, self.grey.get_rect(
                center=(500, 400)).topleft)
        else:
            pass

    def draw_inner_piece(self, color: int, slot: int):
        if color == 1:
            self.screen.blit(self.yellow, self.yellow.get_rect(
                center=(
                500+70*math.cos(math.radians(45*(2*slot)+45)), 400-70*math.sin(math.radians(45*(2*slot)+45)))).topleft)
        elif color == 2:
            self.screen.blit(self.blue, self.blue.get_rect(
                center=(
                500+70*math.cos(math.radians(45*(2*slot)+45)), 400-70*math.sin(math.radians(45*(2*slot)+45)))).topleft)
        elif color == 3:
            self.screen.blit(self.grey, self.grey.get_rect(
                center=(
                500+70*math.cos(math.radians(45*(2*slot)+45)), 400-70*math.sin(math.radians(45*(2*slot)+45)))).topleft)
        else:
            pass

    def draw_inner_piece_tilted(self, color: int, slot: int):
        if color == 1:
            self.screen.blit(self.yellow, self.yellow.get_rect(
                center=(
                500+70*math.cos(math.radians(45*(2*slot)+15)), 400-70*math.sin(math.radians(45*(2*slot)+15)))).topleft)
        elif color == 2:
            self.screen.blit(self.blue, self.blue.get_rect(
                center=(
                500+70*math.cos(math.radians(45*(2*slot)+15)), 400-70*math.sin(math.radians(45*(2*slot)+15)))).topleft)
        elif color == 3:
            self.screen.blit(self.grey, self.grey.get_rect(
                center=(
                500+70*math.cos(math.radians(45*(2*slot)+15)), 400-70*math.sin(math.radians(45*(2*slot)+15)))).topleft)
        else:
            pass

    def draw_middle_piece(self, color: int, slot: int):
        if color == 1:
            self.screen.blit(self.yellow, self.yellow.get_rect(
                center=(
                500+145*math.cos(math.radians(45*(slot-1))), 400+145*math.sin(math.radians(45*(slot-1))))).topleft)
        elif color == 2:
            self.screen.blit(self.blue, self.blue.get_rect(
                center=(
                500+145*math.cos(math.radians(45*(slot-1))), 400+145*math.sin(math.radians(45*(slot-1))))).topleft)
        elif color == 3:
            self.screen.blit(self.grey, self.grey.get_rect(
                center=(
                500+145*math.cos(math.radians(45*(slot-1))), 400+145*math.sin(math.radians(45*(slot-1))))).topleft)
        else:
            pass  

    def draw_middle_piece_tilted(self, color: int, slot: int):
        if color == 1:
            self.screen.blit(self.yellow, self.yellow.get_rect(
                center=(
                500+145*math.cos(math.radians(45*(slot-1)-20)), 400+145*math.sin(math.radians(45*(slot-1)-20)))).topleft)
        elif color == 2:
            self.screen.blit(self.blue, self.blue.get_rect(
                center=(
                500+145*math.cos(math.radians(45*(slot-1)-20)), 400+145*math.sin(math.radians(45*(slot-1)-20)))).topleft)
        elif color == 3:
            self.screen.blit(self.grey, self.grey.get_rect(
                center=(
                500+145*math.cos(math.radians(45*(slot-1)-20)), 400+145*math.sin(math.radians(45*(slot-1)-20)))).topleft)
        else:
            pass   
    
    def draw_outer_piece(self, color: int, slot: int):
        if color == 1:
            self.screen.blit(self.yellow, self.yellow.get_rect(
                center=(
                500+219*math.cos(math.radians(22.5*(slot-2))), 400+219*math.sin(math.radians(22.5*(slot-2))))).topleft)
        elif color == 2:
            self.screen.blit(self.blue, self.blue.get_rect(
                center=(
                500+219*math.cos(math.radians(22.5*(slot-2))), 400+219*math.sin(math.radians(22.5*(slot-2))))).topleft)
        elif color == 3:
            self.screen.blit(self.grey, self.grey.get_rect(
                center=(
                500+219*math.cos(math.radians(22.5*(slot-2))), 400+219*math.sin(math.radians(22.5*(slot-2))))).topleft)
        else:
            pass

    def draw_outer_piece_tilted(self, color: int, slot: int):
        if color == 1:
            self.screen.blit(self.yellow, self.yellow.get_rect(
                center=(
                500+219*math.cos(math.radians(22.5*(slot-2)+13)), 400+219*math.sin(math.radians(22.5*(slot-2)+13)))).topleft)
        elif color == 2:
            self.screen.blit(self.blue, self.blue.get_rect(
                center=(
                500+219*math.cos(math.radians(22.5*(slot-2)+13)), 400+219*math.sin(math.radians(22.5*(slot-2)+13)))).topleft)
        elif color == 3:
            self.screen.blit(self.grey, self.grey.get_rect(
                center=(
                500+219*math.cos(math.radians(22.5*(slot-2)+13)), 400+219*math.sin(math.radians(22.5*(slot-2)+13)))).topleft)
        else:
            pass

    def draw_all_pieces_loop(self):
        for i in range(16):
            self.draw_outer_piece(self.outer_ring[i],i)
        for i in range(8):
            self.draw_middle_piece(self.middle_ring[i],i)
        for i in range(4):
            self.draw_inner_piece(self.inner_ring[i],i)
        
    def draw_all_pieces(self):
        self.draw_center_piece(self.center[0])
        if self.game_state == 1 and self.distance < 253 and self.distance > 180:
            for i in range(16):
                self.draw_outer_piece_tilted(self.outer_ring[i],i)
            for i in range(8):
                self.draw_middle_piece(self.middle_ring[i],i)
            for i in range(4):
                self.draw_inner_piece(self.inner_ring[i],i)
        elif self.game_state == 1 and self.distance < 180 and self.distance > 110:
            for i in range(16):
                self.draw_outer_piece(self.outer_ring[i],i)
            for i in range(8):
                self.draw_middle_piece_tilted(self.middle_ring[i],i)
            for i in range(4):
                self.draw_inner_piece(self.inner_ring[i],i)
        elif self.game_state == 1 and self.distance < 110:
            for i in range(16):
                self.draw_outer_piece(self.outer_ring[i],i)
            for i in range(8):
                self.draw_middle_piece(self.middle_ring[i],i)
            for i in range(4):
                self.draw_inner_piece_tilted(self.inner_ring[i],i)
        else:
            self.draw_all_pieces_loop()

    def add_piece_location(self):
        if self.game_state == 0 and pygame.mouse.get_pressed()[0] == True :    
            if 295 > self.mouseX and self.mouseX > 255 and 190 > self.mouseY  and self.mouseY > 150:
                # lisää "3"-slottiin
                return 3
            elif 290 > self.mouseX and self.mouseX > 250 and 650 > self.mouseY and self.mouseY > 610:
                # lisää "2"-slottiin
                return 2
            elif 747 > self.mouseX and self.mouseX > 707 and 190 > self.mouseY and self.mouseY > 150:
                # lisää "0"-slottiin
                return 0
            elif 750 > self.mouseX and self.mouseX > 710 and 653 > self.mouseY and self.mouseY > 613:
                # lisää "1"-slottiin
                return 1
            else:
                pass

if __name__ == "__main__":
    gui = BoardGUI()