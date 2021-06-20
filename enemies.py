
from settings import *



class Enemy(pg.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        
        #ENEMY PROPERTIES

        self.image = None
        self.rect = self.image.get_rect()

        self.last_update = pg.time.get_ticks()


    def update(self):
        now = pg.time.get_ticks()
        


class Yokai(Enemy):
    def __init__(self):
        super().__init__()


class Oni(Enemy):
    def __init__(self):
        super().__init__()