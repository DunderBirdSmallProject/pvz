import pygame
from .. import constants as ct

class Mainmenu:

    def __init__(self):
        self.current_time = None
        self.advopstart_time = None
        self.advop_time = None
        self.screen = pygame.display.get_surface()
        self.screen.fill(ct.BLACK_COLOR)
        self.onbutton = False
        self.advtype = 0
        self.Twoform = [ct.ADVENTURE_BUTTON, ct.ADVENTURE_HIGHLIGHT]
        self.over = False
        self.AdventureOption()
        self.next = ct.SELECTPLANT_STATE

    def StartUp(self, current_time):
        self.current_time = current_time
    
    def Update(self, current_time, onclick, mouse_pos):
        self.current_time = current_time
        if onclick:
            self.CheckAdvOp(mouse_pos)
        if self.onbutton:
            wholetime = self.current_time - self.advop_time
            if wholetime > 200:
                self.advtype += 1
                self.advtype %= 2
                self.advop_time = self.current_time
            if self.current_time - self.advopstart_time > 1300:
                self.over = True
        self.screen.blit(ct.MAINMENU, (0, 0))
        self.screen.blit(self.Twoform[self.advtype], (470, 75))

    def AdventureOption(self):
        self.advoption_left = 470
        self.advoption_top = 75
        self.advoption_right = self.advoption_left + ct.ADVOPTION_WIDTH
        self.advoption_bottom = self.advoption_top + ct.ADVOPTION_HEIGHT

    def CheckAdvOp(self, mouse_pos):
        x, y = mouse_pos
        if(x >= self.advoption_left and x <= self.advoption_right and
            y >= self.advoption_top and y <= self.advoption_bottom):
            self.advopstart_time = self.advop_time = self.current_time
            self.onbutton = True
    


        
        