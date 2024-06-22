import pygame

class Window:
    def __init__(self, width=800, height=600):
        self._width = width
        self._height = height
        self.screen = pygame.display.set_mode((width, height))
        self.background_color = (0, 0, 0)

    def set_size(self, width, height):
        self._width = width
        self._height = height
        self.screen = pygame.display.set_mode((width, height))

    def set_bgc(self, color_name):
        if color_name.lower() == "black":
            self.background_color = (0, 0, 0)
        elif color_name.lower() == "white":
            self.background_color = (255, 255, 255)
        elif color_name.lower() == "lightblue":
            self.background_color = (173, 216, 230)
        elif color_name.lower() == "darkblue":
            self.background_color = (0, 0, 139)
        else:
            print(f"Color '{color_name}' not recognized.")

    def fill(self):
        self.screen.fill(self.background_color)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
