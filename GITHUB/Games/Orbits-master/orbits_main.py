"""
-*- coding: utf-8 -*-
----------------------------------------------
--- Author         : Mayank Ashokkumar Lad
--- Mail           : mayanklad12@gmail.com
--- Github         : https://github.com/mayanklad
--- LinkedIn       : https://www.linkedin.com/in/mayank-lad-602568151
----------------------------------------------
"""
#Imports
#import sys
import time
import math
from random import randint
import pygame
from pygame import gfxdraw
import names

class Orbits:
    """Main Class"""
    def __init__(self):

        # Define some colors
        self.BLACK = pygame.Color(  0,   0,   0)
        self.WHITE = pygame.Color(255, 255, 255)
        self.RED   = pygame.Color(255,   0,   0)
        self.GREEN = pygame.Color(  0, 255,   0)
        self.BLUE  = pygame.Color(  0,   0, 255)

        pygame.init()

        # Set the height and width of the screen
        self.size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN | pygame.SRCALPHA)
        self.status_surface = pygame.Surface(
            [pygame.display.Info().current_w / 5, pygame.display.Info().current_h], pygame.SRCALPHA)

        pygame.display.set_caption("Orbits")

        #background = pygame.image.load('space3.jpg').convert()
        #background = pygame.transform.scale(background, size)

        # Loop until the user clicks the close button.
        self.done = False

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()
        self.FPS = 60

        # Starting position of the circle
        self.circle_x = 50
        self.circle_y = 50

        self.planet = []
        self.planet_color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.removed_planets = []

        # Speed and direction of circle
        self.dir_x = 0
        self.dir_y = 0

        self.theta = 0
        self.alpha = 0

        self.MILLION = 1 * pow(10, 6)

        self.v = 0  # Mm/s
        self.a = 0  # Mm/s2

        # Ms (t Ms = 365/fps years => 1 real-time sec = 1 in-game year)
        self.t = (3600 * 24 * 365 / self.MILLION) / self.FPS

        self.b_r = 25
        self.p_r = 5
        self.p_m = 5.972 * pow(10, 16)  # Mkg

        self.G = 6.674 * pow(10, -11) # Nm2/kg2 = (m)3/s2(kg)
        #self.M = 1.989 * pow(10, 30) / self.MILLION    # Mkg
        self.M = 1.989 * pow(10, 18)    #mkg
        self.scale = 50 * pow(10, 3) / 1366    # 1 pixel = scale Mm

        self.mouseClicked1 = False
        self.mouseClicked2 = False
        self.eaten = False

        # This is a font we use to draw text on the screen (size 36)
        #font = pygame.font.Font('freesansbold.ttf', 12)

        # Use this boolean variable to trigger if the game is over.
        self.game_over = False

        if __name__ == 'orbits_main':
            self.main()


    def draw_circle(self, surface, color, center, radius, fill=False, border=False):
        """Draw Circle"""
        if fill:
            gfxdraw.filled_circle(surface, int(center[0]), int(center[1]), radius, color)
            if border:
                gfxdraw.aacircle(surface, int(center[0]), int(center[1]), radius, color)
        else:
            gfxdraw.aacircle(surface, int(center[0]), int(center[1]), radius, color)

    def draw_line(self, surface, color, p1, p2):
        """Draw line"""
        pygame.draw.aaline(surface, color, p1, p2)

    def distance(self, p1, p2):
        """Calculate distance between two points"""
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def angle(self, dy, dx):
        """Calculate slope of vector"""
        return math.atan2(dy, dx)

    def collision(self, c1, r1, c2, r2):
        """Check Collision of planet and black hole"""
        return bool(pow(c1[1] - c2[1], 2) + pow(c1[0] - c2[0], 2) <= pow(r1 + r2, 2))

    def out_of_screen(self, i):
        """Check if planet goes out of screen display"""
        return bool(
            self.planet[i]['x'] - self.p_r > self.screen.get_width()
            or self.planet[i]['x'] + self.p_r < 0
            or self.planet[i]['y'] - self.p_r > self.screen.get_height()
            or self.planet[i]['y'] + self.p_r < 0)

    def name_position(self, i, dis_from_bh):
        """Calculate the position on connecting line to print planet name"""
        m = (
            (self.planet[i]['y'] - self.screen.get_height()/2)
            / (self.planet[i]['x'] - self.screen.get_width()/2))

        A = 1 + pow(m, 2)
        B = - (2 * self.screen.get_width()/2 * A)
        C = (pow(self.screen.get_width()/2, 2) * A) - pow(dis_from_bh, 2)

        x = [
            (-B + math.sqrt(pow(B, 2)-(4*A*C))) / (2*A),
            (-B - math.sqrt(pow(B, 2)-(4*A*C))) / (2*A)]

        y = [
            (x[0] - self.screen.get_width()/2) * m + self.screen.get_height()/2,
            (x[1] - self.screen.get_width()/2) * m + self.screen.get_height()/2]

        if self.planet[i]['x'] < self.screen.get_width()/2:
            return [x[1], y[1]]
        else:
            return [x[0], y[0]]

    def update_acceleration(self, i):
        """Update acceleration of planet"""
        a_x = 0
        a_y = 0
        alpha = 0
        a = 0

        if len(self.planet) > 0:
            for j in range(0, len(self.planet)):
                if j == i:
                    continue
                alpha = self.angle(
                    self.planet[j]['y'] - self.planet[i]['y'],
                    self.planet[j]['x'] - self.planet[i]['x'])
                a = (self.G * self.p_m) / (pow(self.scale, 2) * (
                    pow(self.planet[j]['y'] - self.planet[i]['y'], 2)
                    + pow(self.planet[j]['x'] - self.planet[i]['x'], 2)))
                a_x += a * math.cos(alpha)
                a_y += a * math.sin(alpha)

        alpha = self.angle(
            self.screen.get_height()/2 - self.planet[i]['y'],
            self.screen.get_width()/2 - self.planet[i]['x'])

        a = (self.G * self.M) / (pow(self.scale, 2) * (
            pow(self.screen.get_height()/2 - self.planet[i]['y'], 2)
            + pow(self.screen.get_width()/2 - self.planet[i]['x'], 2)))

        a_x += a * math.cos(alpha)
        a_y += a * math.sin(alpha)
        self.planet[i]['acceleration'] = math.sqrt(pow(a_x, 2) + pow(a_y, 2))
        self.planet[i]['alpha'] = self.angle(a_y, a_x)

    def update_velocity(self, i):
        """Update velocity of planet"""
        self.planet[i]['velocity'] = math.sqrt(
            pow(self.planet[i]['velocity'] * math.cos(self.planet[i]['theta'])
            + self.planet[i]['acceleration'] * math.cos(self.planet[i]['alpha']) * self.t, 2)
            + pow(self.planet[i]['velocity'] * math.sin(self.planet[i]['theta'])
            + self.planet[i]['acceleration'] * math.sin(self.planet[i]['alpha']) * self.t, 2))

        self.planet[i]['theta'] = self.angle(
            self.planet[i]['velocity'] * math.sin(self.planet[i]['theta'])
            + self.planet[i]['acceleration'] * math.sin(self.planet[i]['alpha']) * self.t,
            self.planet[i]['velocity'] * math.cos(self.planet[i]['theta'])
            + self.planet[i]['acceleration'] * math.cos(self.planet[i]['alpha']) * self.t)

    def update_position(self, i):
        """Update position of planet"""
        self.planet[i]['x'] += (
            (
                (self.planet[i]['velocity'] * math.cos(self.planet[i]['theta']) * self.t)
                + (
                    0.5
                    * self.planet[i]['acceleration'] * math.cos(self.planet[i]['alpha'])
                    * pow(self.t, 2)))
            / self.scale)

        self.planet[i]['y'] += (
            (
                (self.planet[i]['velocity'] * math.sin(self.planet[i]['theta']) * self.t)
                + (
                    0.5
                    * self.planet[i]['acceleration'] * math.sin(self.planet[i]['alpha'])
                    * pow(self.t, 2)))
            / self.scale)

    def update_life(self, i):
        """Calculate the life of planet ( 1 unit = 24 hrs or 1 day)"""
        self.planet[i]['life'] += 1 / self.FPS    # Days

    def initial_speed(self):
        """Calculate initial speed of planet"""
        self.v = (10 / 25) * self.distance(
            [self.circle_x, self.circle_y],
            [self.dir_x, self.dir_y])

    def game_over_text(self, fsize=40):
        """Text to print when game is over"""
        # Set the screen background
        #screen.blit(background, (0, 0))
        self.screen.fill((50, 50, 50))
        # If game over is true, draw game over
        font = pygame.font.Font('./data/fonts/freesansbold.ttf', fsize)
        text = font.render("Black Hole Wins", True, self.WHITE)
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_hei
        self.screen.blit(text, [text_x, text_y])

    def closing_animation(self, fsize=40):
        """Closing Animation"""
        for i in range(0, int(self.screen.get_width()/2) - 10):
            self.draw_circle(
                self.screen,
                self.BLACK,
                [int(self.screen.get_width()/2), int(self.screen.get_height()/2)],
                10 + i + 1,
                True,
                True)
            pygame.display.flip()

        font = pygame.font.Font('./data/fonts/freesansbold.ttf', fsize)
        text = font.render("Black Hole Wins", True, self.WHITE)
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2
        self.screen.blit(text, [text_x, text_y])
        pygame.display.flip()

        time.sleep(3)

    def main_surface_text(self, fsize=20):
        """Main surface text"""
        font = pygame.font.Font('./data/fonts/freesansbold.ttf', fsize)
        text = font.render("Press q to destroy universe", True, (200, 200, 200))
        self.screen.blit(text, [0, 0])

    def status_surface_text(self, fsize=11):
        """Status surface text"""
        # Planet details columns
        font = pygame.font.Font('./data/fonts/freesansbold.ttf', fsize)
        text1 = font.render("PLANET", True, self.WHITE)
        text2 = font.render("SPEED (Mm/s)", True, self.WHITE)
        text3 = font.render("DISTANCE (Mm)", True, self.WHITE)

        width = self.status_surface.get_width()
        height = self.status_surface.get_height()

        text_x1 = 5
        text_x2 = width / 3
        text_x3 = (width / 3) * 2
        text_y1 = text_y2 = text_y3 = 35
        self.status_surface.blit(text1, [text_x1, text_y1])
        self.status_surface.blit(text2, [text_x2, text_y2])
        self.status_surface.blit(text3, [text_x3, text_y3])

        # Scaling units details
        text4 = font.render("1 real time sec = 1 year", True, self.WHITE)
        text4_rect = text4.get_rect()
        self.status_surface.blit(
            text4,
            [(width/2) - (text4_rect.width/2), height - 50 - text4_rect.height])

        text5 = font.render("1 cm = {0:.2f} Mm".format(37.795275591 * self.scale), True, self.WHITE)
        text5_rect = text5.get_rect()
        self.status_surface.blit(
            text5,
            [(width/2) - (text5_rect.width/2), height - 50 - text5_rect.height - text4_rect.height])

        self.draw_line(
            self.status_surface,
            self.WHITE,
            [width/2 - text4_rect.width/2 - 10, height - 50],
            [width/2 + text4_rect.width/2 + 10, height - 50])

        self.draw_line(
            self.status_surface,
            self.WHITE,
            [width/2 - text4_rect.width/2 - 11, height - 55],
            [width/2 - text4_rect.width/2 - 11, height - 45])

        self.draw_line(
            self.status_surface,
            self.WHITE,
            [width/2 + text4_rect.width/2 + 11, height - 55],
            [width/2 + text4_rect.width/2 + 11, height - 45])

    def distance_text(self, surface, pos, i, fsize=11):
        """Display planet's distance from black hole"""
        font = pygame.font.Font('./data/fonts/freesansbold.ttf', fsize)
        dis = None
        text1 = None 
        if surface == self.screen:
            dis = self.distance(
                [self.circle_x, self.circle_y],
                [self.screen.get_width()/2, self.screen.get_height()/2])

            text1 = font.render("{0:.2f} Mm".format(dis), True, self.WHITE)    
        else:
            dis = self.distance(
                [self.planet[i]['x'], self.planet[i]['y']],
                [self.screen.get_width()/2, self.screen.get_height()/2])

            text1 = font.render("{0:.2f}".format(dis), True, self.WHITE)
        text_rect1 = text1.get_rect()
        text_x1 = pos[0]
        text_y1 = pos[1] - text_rect1.height
        surface.blit(text1, [text_x1, text_y1])

    def life_text(self, surface, pos, i, fsize=11):
        """Display planet's life"""
        font = pygame.font.Font('./data/fonts/freesansbold.ttf', fsize)
        text1 = font.render(
            "{0:.1f} earth year(s)".format(self.planet[i]['life']), True, self.WHITE)
        text_rect1 = text1.get_rect()
        text_x1 = pos[0]
        text_y1 = pos[1] - text_rect1.height
        surface.blit(text1, [text_x1, text_y1])


    def speed_text(self, surface, pos, vel, fsize=11):
        """Display planet's speed text"""
        font = pygame.font.Font('./data/fonts/freesansbold.ttf', fsize)
        text1 = None
        correction = 0
        if surface == self.screen:
            text1 = font.render("{0:.2f} Mm/s".format(vel), True, self.WHITE)
        else:
            text1 = font.render("{0:.2f}".format(vel), True, self.WHITE)
        text_rect1 = text1.get_rect()
        if surface == self.screen:
            correction = - text_rect1.width
        text_x1 = pos[0] + correction
        text_y1 = pos[1] - text_rect1.height
        surface.blit(text1, [text_x1, text_y1])

    def name_text(self, surface, color, pos, i, background=None, fsize=11, connecting_line=False):
        """Display planet's name"""
        font = pygame.font.Font('./data/fonts/freesansbold.ttf', fsize)
        text1 = font.render(self.planet[i]['name'], True, color, background)
        text_rect1 = text1.get_rect()
        text_x1 = 0
        if surface == self.screen and connecting_line:
            text_x1 = pos[0] - text_rect1.width/2
        else:
            text_x1 = pos[0]
        text_y1 = pos[1] - text_rect1.height
        surface.blit(text1, [text_x1, text_y1])

    def planet_remove_text(self, name, reason, fsize=11):
        """Message to print when planet is eaten or escaped"""
        width = self.screen.get_width()
        #height = self.screen.get_height()
        font = pygame.font.Font('./data/fonts/freesansbold.ttf', fsize)
        text1 = None
        if reason == 'eaten':
            text1 = font.render("Planet {} was EATEN by BLACK HOLE".format(name), True, self.WHITE)
        elif reason == 'escaped':
            text1 = font.render("Planet {} ESCAPED from BLACK HOLE".format(name), True, self.WHITE)
        text_rect1 = text1.get_rect()
        text_x1 = width/2 - text_rect1.width/2
        text_y1 = 10
        self.screen.blit(text1, [text_x1, text_y1])

    def crossed_limit(self, var):
        """Checking int08's limit"""
        if var >= 32700 or var <= -32700:
            return True
        else:
            return False

    # -------- Main Program Loop -----------
    def main(self):
        """Main function"""
        while not self.done:

            # Limit frames per second
            self.clock.tick(self.FPS)

            # --- Event Processing
            for event in pygame.event.get():
                if (
                    event.type == pygame.QUIT
                    or (event.type == pygame.KEYDOWN and event.key == pygame.K_q)):

                    self.done = True
                    self.game_over = True

                elif event.type == pygame.MOUSEMOTION:

                    if self.mouseClicked1:
                        self.dir_x, self.dir_y = event.pos
                        self.initial_speed()

                    else:
                        self.circle_x, self.circle_y = event.pos

                elif event.type == pygame.MOUSEBUTTONUP:

                    if not self.mouseClicked1:
                        self.mouseClicked1 = True
                        self.mouseClicked2 = False
                        self.circle_x, self.circle_y = event.pos
                        self.dir_x, self.dir_y = self.circle_x, self.circle_y

                    else:
                        self.mouseClicked1 = False
                        self.mouseClicked2 = True
                        self.dir_x, self.dir_y = event.pos
                        self.theta = self.angle(
                            self.dir_y - self.circle_y,
                            self.dir_x - self.circle_x)

                        self.alpha = self.angle(
                            self.screen.get_height()/2 - self.circle_y,
                            self.screen.get_width()/2 - self.circle_x)

                        self.a = (self.G * self.M) / (
                            pow(self.screen.get_height()/2 - self.circle_y, 2)
                            + pow(self.screen.get_width()/2 - self.circle_x, 2))

                        self.planet.append({
                            'name': names.get_last_name(),
                            'color': self.planet_color,
                            'x': self.circle_x,
                            'y': self.circle_y,
                            'velocity': self.v,
                            'theta': self.theta,
                            'acceleration': self.a,
                            'alpha': self.alpha,
                            'life': 0})
                        
                        self.circle_x, self.circle_y = self.dir_x, self.dir_y

                        self.planet_color = (randint(0, 255), randint(0, 255), randint(0, 255))

            # --- Game Logic

            if not self.eaten:
                # Actual logic
                if len(self.planet) > 0:
                    p_i = 0
                    while p_i < len(self.planet):
                        if self.collision(
                            (self.screen.get_width()/2, self.screen.get_height()/2),
                            self.b_r,
                            (self.planet[p_i]['x'], self.planet[p_i]['y']),
                            self.p_r):

                            self.removed_planets.append([self.planet[p_i]['name'], 'eaten', 0])
                            del self.planet[p_i]

                        else:
                            self.update_position(p_i)
                            if (
                                self.crossed_limit(self.planet[p_i]['x'])
                                or self.crossed_limit(self.planet[p_i]['y'])):

                                self.removed_planets.append([self.planet[p_i]['name'], 'escaped', 0])
                                del self.planet[p_i]

                            else:
                                self.update_acceleration(p_i)
                                self.update_velocity(p_i)
                                self.update_life(p_i)
                                p_i += 1

                # --- Draw the frame

                # Set the screen background
                # screen.blit(background, (0, 0))
                self.screen.fill((50, 50, 50))
                self.status_surface.fill((0, 0, 0, 112))

                # Draw the shapes

                # Drawing connecting line for planets from black hole core
                    # For new planet on the cursor to be created
                    # Connecting line
                self.draw_line(
                    self.screen,
                    (100, 100, 100),
                    [self.screen.get_width()/2, self.screen.get_height()/2],
                    [self.circle_x, self.circle_y])
                    # For current planets
                if len(self.planet) > 0:
                    for i in range(0, len(self.planet)):
                        if self.out_of_screen(i):
                            # Connecting line
                            self.draw_line(
                                self.screen,
                                (100, 100, 100),
                                [self.screen.get_width()/2, self.screen.get_height()/2],
                                [self.planet[i]['x'], self.planet[i]['y']])
                            # Planet's name on connecting line
                            pos = self.name_position(i, 150)
                            #pos = [self.planet[i]['x'] - (self.planet[i]['x'] - self.screen.get_width()/2)/2, 
                            #    self.planet[i]['y'] - (self.planet[i]['y'] - self.screen.get_height()/2)/2]
                            self.name_text(
                                self.screen,
                                self.BLACK,
                                pos,
                                i,
                                background=(100, 100, 100),
                                connecting_line=True)
                            #self.name_text(self.screen, [xx[1], yy[1]], i)

                # Drawing black hole
                self.draw_circle(
                    self.screen,
                    self.BLACK,
                    [self.screen.get_width()/2, self.screen.get_height()/2],
                    20,
                    True)

                # Drawing black hole aura
                for i in range(1, 50):
                    self.draw_circle(
                        self.screen,
                        (0, 0, 0, i),
                        [self.screen.get_width()/2, self.screen.get_height()/2],
                        50-i,
                        True)

                if self.mouseClicked1 and not self.mouseClicked2:
                    self.draw_line(
                        self.screen,
                        self.WHITE,
                        [self.circle_x, self.circle_y],
                        [self.dir_x, self.dir_y])

                    self.speed_text(self.screen, [self.dir_x, self.dir_y], self.v)

                # Drawing current planets and details of them
                if len(self.planet) > 0:
                    for i in range(0, len(self.planet)):

                        # For main surface
                        if not self.out_of_screen(i):
                            self.name_text(
                                self.screen,
                                self.WHITE,
                                [self.planet[i]['x'] + self.p_r + 5, self.planet[i]['y']],
                                i)#,
                                #background=(100, 100, 100))

                            self.draw_circle(
                                self.screen,
                                self.planet[i]['color'],
                                [self.planet[i]['x'], self.planet[i]['y']],
                                5,
                                True,
                                True)

                        # For status surface
                        self.name_text(
                            self.status_surface,
                            self.WHITE,
                            [5, 73+(i*55)],
                            i
                            )

                        self.draw_circle(
                            self.status_surface,
                            self.planet[i]['color'],
                            [10, 82+(i*55)],
                            5,
                            True,
                            True)

                        self.speed_text(
                            self.status_surface,
                            [self.status_surface.get_width()/3, 73+(i*55)],
                            self.planet[i]['velocity'])

                        self.distance_text(
                            self.status_surface,
                            [2*self.status_surface.get_width()/3, 73+(i*55)],
                            i)

                        self.life_text(
                            self.status_surface,
                            [5, 105+(i*55)],
                            i)

                if len(self.removed_planets) > 0:
                    i = 0
                    while i < len(self.removed_planets):
                        self.planet_remove_text(
                            self.removed_planets[i][0],
                            reason=self.removed_planets[i][1])
                        self.removed_planets[i][2] += 1
                        if self.removed_planets[i][2] == self.FPS * 5:
                            del self.removed_planets[i]
                        else:
                            i += 1

                # New planet on the cursor to be created
                self.draw_circle(
                    self.screen,
                    self.planet_color,
                    [self.circle_x, self.circle_y],
                    5,
                    True,
                    True)

                self.distance_text(
                    self.screen,
                    [self.circle_x + self.p_r + 5, self.circle_y],
                    i)

            # Till window is not closed, draw this stuff.
            if not self.done:
                #status surface
                self.status_surface_text()
                self.screen.blit(self.status_surface, (0, 0))

                self.main_surface_text()
                pygame.display.flip()
            else:
                self.closing_animation()


        # on exit.
        pygame.quit()
        #sys.exit(0)

if __name__ == '__main__':
    O = Orbits()
    O.main()
