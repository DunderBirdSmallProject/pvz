import pygame
from .. import constants as ct

card_name_list = [ct.CARD_SUNFLOWER, ct.CARD_PEASHOOTER, ct.CARD_SNOWPEA, ct.CARD_WALLNUT,
                  ct.CARD_CHERRYBOMB, ct.CARD_THREEPEASHOOTER, ct.CARD_REPEATERPEA, ct.CARD_CHOMPER,
                  ct.CARD_PUFFSHROOM, ct.CARD_POTATOMINE, ct.CARD_SQUASH, ct.CARD_SPIKEWEED,
                  ct.CARD_JALAPENO, ct.CARD_SCAREDYSHROOM, ct.CARD_SUNSHROOM, ct.CARD_ICESHROOM,
                  ct.CARD_HYPNOSHROOM, ct.CARD_WALLNUT]

plant_sun_list = [50, 100, 175, 50, 150, 325, 200, 150, 0, 25, 50, 100, 125, 25, 25, 75, 75, 50]
plant_frozen_time_list = [7500, 7500, 7500, 30000, 50000, 7500, 7500, 7500, 7500, 30000,
                          30000, 7500, 50000, 7500, 7500, 50000, 30000, 7500]

class Gaming:

    def __init__(self):
        self.current_time = None
        self.screen = pygame.display.get_surface()
        self.screen.fill(ct.BLACK_COLOR)
        self.over = False
        self.selcard_list = []

    def StartUp(self, current_time):
        self.current_time = current_time
    
    def LoadCard(self, selcard_list, planttype):
        self.selcard_list = selcard_list
        self.planttype = planttype
    
    def Update(self, current_time, onclick, mouse_pos):
        self.current_time = current_time
        self.screen.blit(ct.BACKGROUND_0, (-220, 0))
        self.screen.blit(ct.CHOOSERBACKGROUND, (0, 0))
        self.DisplaySelCard()

    def DisplaySelCard(self):
        for i, card in enumerate(self.selcard_list):
            card.left = 32 + 53 * (i + 1)
            card.right = card.left + card.image.get_rect().width
            card.top = 8
            card.bottom = 8 + card.image.get_rect().height
            card.image.set_alpha(255)
            self.screen.blit(card.image, (card.left, card.top))
