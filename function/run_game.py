import pygame
import sys
from . import setting
from . import constants as ct
from . import game_function as gf
from .state import mainmenu, select, gaming

def run_game():
    screen = setting.init()
    state_dict = {ct.MAINMENU_STATE: mainmenu.Mainmenu(),
                ct.SELECTPLANT_STATE: select.SelectPlant(),
                ct.GAME_STATE: gaming.Gaming()}
    game = gf.GameControl()
    game.get_state(state_dict, ct.MAINMENU_STATE)
    game.RunGame()