
from settings import *



class Player(pg.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        
        #PLAYER PROPERTIES

        self.image = None
        self.rect = self.image.get_rect()

        self.last_update = pg.time.get_ticks()


    def update(self):
        now = pg.time.get_ticks()
        
