import pygame
from starcrusher2025_games.configs.player import Player
from starcrusher2025_games.configs.window import Window
from starcrusher2025_games.update.requests import notify_user_if_update_available

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
        self.paintmode = False
        notify_user_if_update_available('starcrusher2025-games')

    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.stop()
                    elif event.key in [pygame.K_a, pygame.K_LEFT]:
                        self.keys['left'] = True
                    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                        self.keys['right'] = True
                    elif event.key in [pygame.K_w, pygame.K_UP]:
                        self.keys['up'] = True
                    elif event.key in [pygame.K_s, pygame.K_DOWN]:
                        self.keys['down'] = True
                    elif event.key == pygame.K_F11:
                        self.window.toggle_fullscreen()

                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_a, pygame.K_LEFT]:
                        self.keys['left'] = False
                    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                        self.keys['right'] = False
                    elif event.key in [pygame.K_w, pygame.K_UP]:
                        self.keys['up'] = False
                    elif event.key in [pygame.K_s, pygame.K_DOWN]:
                        self.keys['down'] = False
                        
            
            self.update()
            self.render()

            self.clock.tick(self.target_fps)

        pygame.quit()

    def update(self):
        self.player.handle_keys(self.keys)
        self.player.keep_within_bounds(self.window.width, self.window.height)

    def render(self):
        if self.paintmode == True:
            self.player.render(self.window.screen)
            pygame.display.flip()
        else:
            self.window.screen.fill(self.window.background_color)
            self.player.render(self.window.screen)
            pygame.display.flip()

    def stop(self):
        self.running = False

    def set_fps(self, fps):
        self.target_fps = fps

    def paint_mode(self,mode):
        if mode == True:
            self.paintmode = True

    @property
    def window(self):
        return self._window
    
    def set_background_image(self, image_path_bg=None):
        self.window.set_background(image_path_bg)

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

    def load_player_image(self, image_path_player):
        self.player.load_player_image(image_path_player)

    def set_window_size(self, width, height):
        self.window.set_size(width, height)

    def set_bgc(self, color):
        self.window.set_bgc(color)
    
    def get_player_position(self):
        self.player.get_player_position(self)