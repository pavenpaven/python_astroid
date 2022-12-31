import pygame
import conf

mine_color = conf.conf_search("mine_color")
mine_color = mine_color.split(",")
mine_color = tuple(list(map(int, mine_color)))

astroid_size = int(conf.conf_search("astroid_size"))
mine_size = int(conf.conf_search("mine_size"))
mine_size = (mine_size, mine_size)

class Mine:
    mines = []
    def __init__(self, pos):
        self.pos = pos
        self.timer = 60
        __class__.mines.append(self)

    def render(self, window):
        if self.timer > 0:
            self.timer -= 1

        pygame.draw.rect(window, mine_color, pygame.Rect(self.pos, mine_size))

    def check_astroids(self, astroids):
        for n,i in enumerate(astroids):
            rect = pygame.Rect((i[0], i[1]), (astroid_size, astroid_size))
            if rect.colliderect(pygame.Rect(self.pos, mine_size)):
                astroids.pop(n)
                return True
        return False

    def collide_player(self, player_hitbox) -> bool:
        if self.timer<2:
            player_rect = pygame.Rect(player_hitbox[0], (60,60))
            return player_rect.colliderect(pygame.Rect(self.pos, mine_size))
        return False


