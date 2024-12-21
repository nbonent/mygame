import pygame
import random

#инициализация
pygame.init()

#экран
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))

font = pygame.font.Font(None, 36)

class GameObject:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)

class Spaceship(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


class Asteroid(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)#super вызывает метод инициализации из родительского класса и дополняет свой метод

    def move(self):
        self.rect.y +=1

def main():
    clock = pygame.time.Clock()

    spaceship = Spaceship(500, 650)
    asteroids = [Asteroid(random.randrange(0, width), random.randrange(0, 400)) for _ in range(20)]
    bullets = []
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(pygame.Rect(spaceship.rect.centerx, spaceship.rect.top, 10, 10))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            spaceship.move(-10, 0)
        if keys[pygame.K_RIGHT]:
            spaceship.move(10, 0)


        for asteroid in asteroids:
            asteroid.move()

        for bullet in bullets[:]:
            bullet.y -= 15
            if bullet.bottom < 0:
                bullets.remove(bullet)

        #столкновения
        for asteroid in asteroids[:]:
            if spaceship.rect.colliderect(asteroid.rect):
                score -=10
            for bullet in bullets[:]:
                if asteroid.rect.colliderect(bullet):
                    score += 10
                    asteroids.remove(asteroid)
                    bullets.remove(bullet)

        #рендер
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0,255,0), spaceship.rect)
        for asteroid in asteroids:
            pygame.draw.rect(screen,(255,0,0), asteroid.rect)
        for bullet in bullets:
            pygame.draw.rect(screen, (255,255,255), bullet)

        score_text = font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()



