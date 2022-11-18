import math

def makeCircle(x, y, quantity) :
    points = []
    X = 0
    Y = 0
    alpha = 360 / quantity
    alpha_tmp = 360 / quantity
    alpha_radians = math.radians(alpha)
    alpha_radians_tmp = math.radians(alpha)
    for i in range(quantity) :
        X = (x*math.cos(alpha_radians_tmp) - y*math.sin(alpha_radians_tmp))
        Y = (x*math.sin(alpha_radians_tmp) - y*math.cos(alpha_radians_tmp))
        points.append([X, Y, 0])
        alpha_radians_tmp += alpha_radians
        alpha_tmp += alpha
    return points


class Cone():
    verticies = []
    edges = []
    height = 0
    radius = 0
    polygons = 0
    transformed = False

    def __init__(self, height, radius, polygons = 17):
        self.verticies = []
        self.edges = []
        self.verticies.append([0, 0, height])
        self.verticies += makeCircle(radius, 0, polygons)
        for i in range(1, len(self.verticies) - 1):
            self.edges.append([i, i + 1])
            self.edges.append([i, 0])
        self.edges.append([1, len(self.verticies) - 1])
        self.edges.append([len(self.verticies) - 1, 0])

    def __del__(self):
        self.verticies.clear()
        self.edges.clear()
