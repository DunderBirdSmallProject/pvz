import pygame
from .. import constants as ct

class ParaCard:
    def __init__(self, image, isselect, left, right, top, bottom, index):
        self.image = image
        self.isselect = isselect
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.index = index

class SelectPlant:

    def __init__(self):
        self.current_time = None
        self.screen = pygame.display.get_surface()
        self.screen.fill(ct.BLACK_COLOR)
        self.over = False
        self.card_list = [ct.CARD_SUNFLOWER, ct.CARD_PEASHOOTER, ct.CARD_SNOWPEA, ct.CARD_WALLNUT,
                  ct.CARD_CHERRYBOMB, ct.CARD_THREEPEASHOOTER, ct.CARD_REPEATERPEA, ct.CARD_CHOMPER,
                  ct.CARD_PUFFSHROOM, ct.CARD_POTATOMINE, ct.CARD_SQUASH, ct.CARD_SPIKEWEED,
                  ct.CARD_JALAPENO, ct.CARD_SCAREDYSHROOM, ct.CARD_SUNSHROOM, ct.CARD_ICESHROOM,
                  ct.CARD_HYPNOSHROOM, ct.CARD_WALLNUT]
        self.cardparameter = []
        self.selcard_list = []
        self.StartPosinit()
        self.next = ct.GAME_STATE
        self.LoadCard()
        self.cardnum = 0
        self.image = None

    def StartPosinit(self):
        self.startpos_left = 155
        self.startpos_right = 155 + 154
        self.startpos_top = 547
        self.startpos_bottom = 547 + 37

    def StartUp(self, current_time):
        self.current_time = current_time

    def LoadCard(self):
        y = ct.PANEL_Y_START + 43 - ct.PANEL_Y_STOP
        for i, plant in enumerate(self.card_list):
            if i % 8 == 0:
                x = ct.PANEL_X_START - ct.PANEL_X_STOP
                y += ct.PANEL_Y_STOP
            x += ct.PANEL_X_STOP
            plant = self.fix_image(plant, ct.CARD_WIDTH, ct.CARD_HEIGHT, 0.78)
            self.cardparameter.append(ParaCard(plant, False, x,  x + ct.CARD_WIDTH * 0.78, y, y + ct.CARD_HEIGHT * 0.78, i))
    
    def DisplayCard(self):
        for card in self.cardparameter:
            self.image = card.image
            self.SetAlpha(card.isselect)
            self.screen.blit(self.image, (card.left, card.top))

    def SetAlpha(self, isselect):
        if isselect:
            self.image.set_alpha(128)
        else:
            self.image.set_alpha(255)

    def DisplaySelCard(self):
        for i, card in enumerate(self.selcard_list):
            card.left = 32 + 53 * (i + 1)
            card.right = card.left + card.image.get_rect().width
            card.top = 8
            card.bottom = 8 + card.image.get_rect().height
            card.image.set_alpha(255)
            self.screen.blit(card.image, (card.left, card.top))

    def fix_image(self, image, width, height, scale):
        return pygame.transform.scale(image, (int(width * scale),
                                    int(height * scale)))
    
    def Update(self, current_time, onclick, mouse_pos):
        self.current_time = current_time
        if onclick:
            self.Checkmouse(mouse_pos)
        self.screen.blit(ct.BACKGROUND_0, (-500, 0))
        self.screen.blit(ct.CHOOSERBACKGROUND, (0, 0))
        self.screen.blit(ct.PANELBACKGROUND, (0, 87))
        if self.cardnum == ct.TOTALGAMECARD:
            ct.STARTBUTTON.set_alpha(255)
        else:
            ct.STARTBUTTON.set_alpha(128)
        self.screen.blit(ct.STARTBUTTON, (155, 547))
        self.DisplayCard()
        self.DisplaySelCard()

    def Checkmouse(self, mouse_pos):
        x, y = mouse_pos
        if(x >= self.startpos_left and x <= self.startpos_right and
        y >= self.startpos_top and y <= self.startpos_bottom and self.cardnum == 8):
            self.over = True
        else:
            if self.cardnum < ct.TOTALGAMECARD:
                for card in self.cardparameter:
                    if(x >= card.left and x <= card.right and
                    y >= card.top and y <= card.bottom and (not card.isselect)):
                        self.cardnum += 1
                        card.isselect = True
                        timage = pygame.transform.scale(card.image, (int(ct.CARD_WIDTH * 0.74),
                                    int(ct.CARD_HEIGHT * 0.78)))
                        temp = ParaCard(timage, False, 0, 0, 0, 0, card.index)
                        self.selcard_list.append(temp)
                        return
            for i, card in enumerate(self.selcard_list):
                if(x >= card.left and x <= card.right and
                y >= card.top and y <= card.bottom):
                    self.cardnum -= 1
                    for plant in self.cardparameter:
                        if card.index == plant.index:
                            plant.isselect = False
                            break
                    self.selcard_list.pop(i)
                    return