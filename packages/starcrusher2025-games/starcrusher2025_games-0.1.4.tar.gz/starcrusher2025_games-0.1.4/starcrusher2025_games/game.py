import pygame
from starcrusher2025_games.configs.player import Player
from starcrusher2025_games.configs.window import Window

class Game:
    def __init__(self):
        pygame.init()
        self._window = Window()
        self.clock = pygame.time.Clock()
        self.running = False
        self._player = Player()
        self.keys = {
            'left': False,
            'right': False,
            'up': False,
            'down': False
        }

    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.stop()
                    elif event.key == pygame.K_a:
                        self.keys['left'] = True
                    elif event.key == pygame.K_d:
                        self.keys['right'] = True
                    elif event.key == pygame.K_w:
                        self.keys['up'] = True
                    elif event.key == pygame.K_s:
                        self.keys['down'] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.keys['left'] = False
                    elif event.key == pygame.K_d:
                        self.keys['right'] = False
                    elif event.key == pygame.K_w:
                        self.keys['up'] = False
                    elif event.key == pygame.K_s:
                        self.keys['down'] = False
                self.render()
            
            self.update()
            self.render()

            self.clock.tick(self.target_fps)

        pygame.quit()

    def update(self):
        self.player.handle_keys(self.keys)
        self.player.keep_within_bounds(self.window.width, self.window.height)

    def render(self):
        self.player.render(self.window.screen)
        pygame.display.flip()

    def stop(self):
        self.running = False

    def set_fps(self, fps):
        self.target_fps = fps

    @property
    def window(self):
        return self._window

    @property
    def player(self):
        return self._player

    def set_player_color(self, color):
        self.player.set_color(color)

    def set_player_start_pos(self, start_pos):
        self.player.set_start_pos(start_pos)

    def set_player_size(self, size):
        self.player.set_size(size)

    def set_player_speed(self, speed):
        self.player.set_speed(speed)

    def load_player_image(self, image_path):
        self.player.load_player_image(image_path)

    def set_window_size(self, width, height):
        self.window.set_size(width, height)

    def set_bgc(self, color):
        self.window.set_bgc(color)
    
    def get_player_position(self):
        self.player.get_player_position(self)