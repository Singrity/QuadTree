import pygame as pg


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pg.draw.rect(pg.display.get_surface(), (0, 0, 0), [self.x, self.y, 4, 4])
        #pg.display.get_surface().set_at((self.x, self.y), (0, 0, 0))


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)
        self.rect.center = self.x, self.y

    def __contains__(self, point):
        return self.x - self.w <= point.x <= self.x + self.w and self.y - self.h <= point.y <= self.y + self.h


class QuadTree:
    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def insert(self, point):

        if point not in self.boundary:
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()
                self.divided = True

            if self.north_west.insert(point):
                return True
            elif self.north_east.insert(point):
                return True
            elif self.south_west.insert(point):
                return True
            elif self.south_east.insert(point):
                return True

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h

        self.nw = Rectangle(x - w // 4, y - h // 4, w // 2, h // 2)
        self.north_west = QuadTree(self.nw, self.capacity)

        self.ne = Rectangle(x + w // 4, y - h // 4, w // 2, h // 2)
        self.north_east = QuadTree(self.ne, self.capacity)

        self.sw = Rectangle(x - w // 4, y + h // 4, w // 2, h // 2)
        self.south_west = QuadTree(self.sw, self.capacity)

        self.se = Rectangle(x + w // 4, y + h // 4, w // 2, h // 2)
        self.south_east = QuadTree(self.se, self.capacity)

        self.divided = True

    def draw(self):
        pg.draw.rect(pg.display.get_surface(), (0, 0, 0), self.boundary.rect, 1)
        if self.divided:
            self.north_west.draw()
            self.north_east.draw()
            self.south_west.draw()
            self.south_east.draw()

        for p in self.points:
            pg.draw.rect(pg.display.get_surface(), (255, 0, 0), [p.x, p.y, 2, 2])




