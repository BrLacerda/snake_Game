import pygame
import random
                                            # TELA

wdt = 1200
hgt = 720

                                            # COBRA

square = 20


pixels = []

                                            # CORES

black = (0, 0, 0)
white = (255, 255, 255)
verde = (40, 180, 60)
amarela = (180, 180, 15)

                                            # INIT
pygame.init()
game_window = pygame.display.set_mode([wdt, hgt])
pygame.display.set_caption("WordSSnake")
clock = pygame.time.Clock()

def Letters():
    letterX = round(random.randrange(0, (wdt - square)) / 20.0) * 20.0
    letterY = round(random.randrange(0, (hgt - square)) / 20.0) * 20.0
    return letterX, letterY

def DrawLetters(large, letterX, letterY):
    pygame.draw.rect(game_window, amarela, (letterX, letterY, large, large))

def DrawSnake(large, pixels):
    for pixel in pixels:
        pygame.draw.rect(game_window, verde, [pixel[0], pixel[1], large, large])

def DrawScore(score):
    font = pygame.font.SysFont("Helvetica", 30)
    text = font.render(f"Score: {score - 1}", True, amarela)
    game_window.blit(text, [(wdt/2 - 40), 1])


def selectSpeed(key):
    if key == pygame.K_DOWN:
        speedX, speedY = 0, square

    if key == pygame.K_UP:
        speedX, speedY = 0, -square

    if key == pygame.K_LEFT:
        speedX, speedY = -square, 0

    if key == pygame.K_RIGHT:
        speedX, speedY = square, 0

    return speedX, speedY


def runGame():
    TheEnd = False

    x, y = wdt/2, hgt/2
    speedX, speedY = 0, 0
    letterX, letterY = Letters()
    snakeLarge = 1
    speed = 15

    while not TheEnd:
        game_window.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                TheEnd = True
            elif event.type == pygame.KEYDOWN:
                speedX, speedY = selectSpeed(event.key)


        x += speedX
        y += speedY

        pixels.append([x, y])
        if len(pixels) > snakeLarge:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                TheEnd = True
        for pixel in pixels:
            if pixel[0] > wdt - square or pixel[1] > hgt - square:
                TheEnd = True
            if pixel[0] < 0 or pixel[1] < 0:
                TheEnd = True

        DrawLetters(square, letterX, letterY)

        DrawSnake(square, pixels)

        DrawScore(snakeLarge)

        pygame.display.update()

        if x == letterX and y == letterY:
            snakeLarge += 1
            speed = speed*1.1
            letterX, letterY = Letters()


        clock.tick(speed)
runGame()
