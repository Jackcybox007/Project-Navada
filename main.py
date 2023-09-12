import pygame
import time

screen_width = 1360
screen_height = 700

class app:
    def __init__(self) -> None:
        
        pygame.init()

        self.WIN = pygame.display.set_mode((screen_width, screen_height), vsync=1)
        pygame.display.set_caption("Main")

        self.clock = pygame.time.Clock()
        self.running = True

        self.t0 = 0
        self.t1 = 0
        self.dt = 0

        self.Objects = []

        self.run()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update_pygame(self):
        self.t1 = time.time()
        self.clock.tick()
        self.dt = (self.t1 - self.t0) / 1000
        self.t0 = time.time()

    def _update_physics(self):
        pass

    def _update_display(self):
        self.WIN.fill((0,0,0))
        for Object in self.Objects:
            Object.draw(self.WIN)
        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.event_handler()
            self._update_pygame()
            self._update_physics()
            self._update_display()

if __name__ == "__main__":
    APP = app()

            
            
