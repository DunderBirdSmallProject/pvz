import pygame
import sys
from . import constants as ct

SCREEN_FPS = 60

class GameControl:

    def __init__(self):
        self.state = None
        self.state_dict = []
        self.state_name = None
        self.current_time = 0.0
        self.clock = pygame.time.Clock()
        self.fps = SCREEN_FPS
        self.isrun = True
        self.mouse_pos = None
        self.onclick = False

    def get_state(self, state_dict, state_name):
        self.state_dict = state_dict
        self.state_name = state_name
        self.state = state_dict[state_name]
        self.state.StartUp(self.current_time)

    def flip_state(self):
        templist = temp = []
        if self.state_name == ct.SELECTPLANT_STATE:
            templist = self.state.selcard_list
            temp = self.state.card_list
        self.state_name = self.state.next
        self.state = self.state_dict[self.state_name]
        if self.state_name == ct.GAME_STATE:
            self.state.LoadCard(templist, temp)

    def CheckEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.onclick = True
                    print('mouse', event.pos)
                    self.mouse_pos = event.pos
        
    def Update(self):
        self.current_time = pygame.time.get_ticks()
        if self.state.over:
            self.flip_state()
        self.state.Update(self.current_time, self.onclick, self.mouse_pos)
        self.onclick = False


    def RunGame(self):
        while True:
            self.CheckEvent()
            self.Update()
            pygame.display.update()
            self.clock.tick(self.fps)
        print('Game Over')
