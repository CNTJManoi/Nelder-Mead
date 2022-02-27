import matplotlib.pyplot as plt


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __rmul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        return Vector(x, y)

    def c(self):
        return self.x, self.y

    def x(self):
        return self.x

    def y(self):
        return self.y


# objective function
def f(point):
    x, y = point
    return 100 * (x - y ** 2) ** 2 + (1 - x) ** 2


FunctionX = []
FunctionY = []


def nelder_mead(alpha=1, beta=0.5, gamma=2, maxiter=70):
    v1 = Vector(0, 0)
    v2 = Vector(1.0, 0)
    v3 = Vector(0, 1)

    for i in range(maxiter):
        adict = {v1: f(v1.c()), v2: f(v2.c()), v3: f(v3.c())}
        points = sorted(adict.items(), key=lambda x: x[1])

        b = points[0][0]
        g = points[1][0]
        w = points[2][0]

        mid = (g + b) / 2

        xr = mid + alpha * (mid - w)
        if f(xr.c()) < f(g.c()):
            w = xr
        else:
            if f(xr.c()) < f(w.c()):
                w = xr
            c = (w + mid) / 2
            if f(c.c()) < f(w.c()):
                w = c
        if f(xr.c()) < f(b.c()):

            xe = mid + gamma * (xr - mid)
            if f(xe.c()) < f(xr.c()):
                w = xe
            else:
                w = xr
        if f(xr.c()) > f(g.c()):

            xc = mid + beta * (w - mid)
            if f(xc.c()) < f(w.c()):
                w = xc
        FunctionX.append(v1.x)
        FunctionX.append(v2.x)
        FunctionX.append(v3.x)
        FunctionY.append(v1.y)
        FunctionY.append(v2.y)
        FunctionY.append(v3.y)
        v1 = w
        v2 = g
        v3 = b
    return b


print("Результат работы алгоритма: ")
xk = nelder_mead()
print("Лучшая точка: %s" % (xk))
print("Значение функции в этой точке: %s" % f(xk.c()))

plt.title("Симплекс")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(FunctionX, FunctionY)
plt.show()