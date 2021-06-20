from settings import *


class Game:
    def __init__(self,window):

        self.init_groups()
        self.screen = window

        self.gameExit = False

        self.clock = pg.time.Clock()

    
    def init_groups(self):
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
    

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(-1)
        self.all_sprites.draw(self.screen)



    def game_loop(self):
        
        
        while not self.gameExit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                
            
            self.update()
            self.draw()
            pg.display.flip()
        




game = Game(window)
game.game_loop()