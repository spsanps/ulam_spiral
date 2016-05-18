import math

import numpy as np
import pygame

BLACK, WHITE = (0, 0, 0), (255, 255, 255)


def spiral(n):
    x, y, i = 0, 0, 0
    dx, dy = 0, -1

    while i < n:
        yield (x, y)

        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y): dx, dy = -dy, dx

        x += dx
        y += dy
        i += 1


def prime(to):
    primes = np.arange(3, to + 1, 2)
    is_prime = np.ones((to - 1) / 2, dtype=bool)

    for factor in primes[:int(math.sqrt(to))]:
        if is_prime[(factor - 2) / 2]: is_prime[(factor * 3 - 2) / 2::factor] = 0
    return np.insert(primes[is_prime], 0, 2)


def is_prime_list(to):
    primes = prime(to + 1000)
    l = np.zeros(to + 1, dtype=bool)
    i, n = 0, 1

    while n < to + 1:
        if n == primes[i]:
            l[n - 1] = True
            i += 1
        n += 1
    return l


def main():
    dim = 1000
    x, y = dim, dim
    WINDOW_SIZE = [x, y]
    done = False
    to = is_prime_list(x * y + 10)

    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Ulam's Spiral")
    screen.fill(WHITE)

    sx = x / 2 + 1
    sy = y / 2 + 1
    i = 2

    for add in spiral(x * y):
        x_add, y_add = add
        if to[i]:
            screen.set_at((sx + x_add, sy + y_add), BLACK)
            # comment the next line to update at end
            if i % 5000 == 0: pygame.display.flip()
        i += 1

    # pygame.image.save(screen, "screenshot.jpeg")
    pygame.display.flip()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  done = True
    pygame.quit()


main()
