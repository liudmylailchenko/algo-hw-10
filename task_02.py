import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def f(x):
    return x**2


a, b = 0, 2

N = 100000

x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

points_under_curve = np.sum(y_rand < f(x_rand))

rectangle_area = (b - a) * f(b)
area_mc = (points_under_curve / N) * rectangle_area

integral_quad, error = quad(f, a, b)

print("Метод Монте-Карло:", area_mc)
print("Аналітичний інтеграл (quad):", integral_quad)
print("Похибка обчислення quad:", error)

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, "r", linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

ax.scatter(x_rand[:1000], y_rand[:1000], s=1, color="blue", alpha=0.5)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()
