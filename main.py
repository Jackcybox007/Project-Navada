import pygame
import time, sys
from lib.vehical import vehical

car = vehical(2000)

class main:
    def __init__(self):
        pygame.init()
        self.Display = pygame.display.set_mode((1360, 700))
        
        self.clock = pygame.time.Clock()
        self.t0 = time.time()
        self.t1 = time.time()

        self.input = [0,0,1]

        self.run()

    def update(self):
        self.t1 = time.time()
        self.dt = (self.t1 - self.t0)
        self.t0 = time.time()
        car.update(self.dt, self.input[0], self.input[1], self.input[2])

        self.clock.tick()        
    def display(self):
        self.Display.fill((0,0,0))

        pygame.display.flip()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                self.input[0] = max(min(self.input[0] + 0.1 * self.dt, 1), 0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                self.input[1] = max(min(self.input[0] + 0.1 * self.dt, 1), 0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.input[2] = max(min(self.input[2] - 1, len(car.gears)), 0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                self.input[2] = max(min(self.input[2] + 1, len(car.gears)), 0)
            elif event.type == pygame.KEYUP and event.key == pygame.K_w:
                self.input[0] = 0
            elif event.type == pygame.KEYUP and event.key == pygame.K_w:
                self.input[1] = 0
            
                

    def run(self):
        self.running = True
        while self.running:
            self.event_handler()
            self.update()
            self.display()

    def quit(self):
        sys.exit(0)

if __name__ == "__main__":
    app = main()
