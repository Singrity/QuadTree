import random

import pygame
import pygame as pg
from quad_tree import QuadTree, Rectangle, Point


class Application:
    def __init__(self):
        self.display = pg.display.set_mode((800, 600))
        self.clock = pg.time.Clock()

        self.boundary = Rectangle(400, 300, 800, 600)
        self.quad_tree = QuadTree(self.boundary, 10)
        self.points = []

        self.insert = False

        self.is_running = False

    def run(self):
        self.is_running = True
        while self.is_running:
            time_ms = self.clock.tick(60)
            time_s = time_ms / 1000
            self.handle_events()
            self.draw()
            self.update()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.insert = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.insert = False

    def draw(self):
        self.display.fill((255, 255, 255))
        self.quad_tree.draw()

        pg.display.flip()

    def update(self):
        if self.insert:
            for _ in range(3):
                x, y = pg.mouse.get_pos()
                point = Point(x, y)
                self.quad_tree.insert(point)
        for point in self.points:
            point.x += random.random()
            point.y += random.random()


if __name__ == '__main__':
    app = Application()
    app.run()
