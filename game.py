from pickle import TRUE
import sys
import pygame


# Make the game its own object
class Game:
    def __init__(self):
        pygame.init()

        # Window caption
        pygame.display.set_caption("Ninja game")
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()
        self.img = pygame.image.load("data/images/clouds/cloud_1.png")
        self.img_pos = [160, 260]
        self.movement = [False, False]
        self.img.set_colorkey((0, 0, 0))

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            self.img_pos[1] += self.movement[1] - self.movement[0]
            self.screen.blit(self.img, self.img_pos)  # merging different images/ collages onto images
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[1] = True
                    if event.type == pygame.DOWN:
                        self.movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.type == pygame.K_UP:
                        self.movement[0] = False

                    if event.type == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)  # loop will run at 60fps


Game().run()
