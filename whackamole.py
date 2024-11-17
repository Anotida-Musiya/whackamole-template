import pygame
import random

rows = 16
columns = 20

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        mole_row = 0
        mole_col = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y//32
                    col = x//32
                    print(x, y)
                    print(row,col)

                    if row == mole_row and col == mole_col:
                        mole_row = random.randrange(0, rows)
                        mole_col = random.randrange(0, columns)
                        print(mole_row, mole_col)

            screen.fill("light blue")

            for i in range(columns):
                pygame.draw.line(
                    screen,
                    "black",
                    (i * 32, 0),
                    (i * 32, 512)
                    )
            for i in range(rows):
                pygame.draw.line(
                    screen,
                    "black",
                    (0,i * 32),
                    (640, i * 32)
                )

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_col * 32, mole_row * 32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
