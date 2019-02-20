import pygame

import pygame.sysfont


class Start:
    def __init__(self, screen, stats):
        self.title = pygame.font.SysFont("comicsansms", 150)
        self.sub = pygame.font.SysFont("comicsansms", 80)
        self.medium = pygame.font.SysFont("comicsansms", 30)

        # toggle pages
        self.page = True

        self.white = (255, 255, 255)
        self.green = (50, 255, 50)
        self.red = (255, 0, 0)

        #  Space Invaders
        self.space = self.title.render("SPACE", True, self.white)
        self.space_btn = self.space.get_rect()
        self.space_btn.centerx = screen.get_rect().centerx
        self.space_btn.centery = screen.get_rect().centery - 300
        self.inv = self.title.render("INVADERS", True, self.green)
        self.inv_btn = self.inv.get_rect()
        self.inv_btn.centerx = screen.get_rect().centerx
        self.inv_btn.centery = screen.get_rect().centery - 200

        #  png that displays the alien with the pts system
        self.score = pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/menu.png')
        self.score_btn = self.score.get_rect()
        self.score_btn.centerx = screen.get_rect().centerx
        self.score_btn.centery = screen.get_rect().centery + 30

        # high scores ON menu
        self.high = self.medium.render("HIGH SCORES", True, self.white)
        self.high_btn = self.high.get_rect()
        self.high_btn.centerx = screen.get_rect().centerx
        self.high_btn.centery = screen.get_rect().centery + 310

        # once you click high scores this will be the title
        self.hs = self.title.render("HIGH SCORE", True, self.white)
        self.hs_btn = self.hs.get_rect()
        self.hs_btn.centerx = screen.get_rect().centerx
        self.hs_btn.centery = screen.get_rect().centery - 300

        # back button
        self.back = self.medium.render("BACK", True, self.white)
        self.back_btn = self.back.get_rect()
        self.back_btn.centerx = screen.get_rect().centerx
        self.back_btn.centery = screen.get_rect().centery + 310

        # open text file and get high score
        self.hss = self.title.render(str(stats.current), True, self.white)
        self.hss_btn = self.hss.get_rect()
        self.hss_btn.centerx = screen.get_rect().centerx
        self.hss_btn.centery = screen.get_rect().centery

    def start_blit(self, screen, stats):
        if self.page is True:
            screen.blit(self.space, self.space_btn)
            screen.blit(self.inv, self.inv_btn)
            screen.blit(self.score, self.score_btn)
            screen.blit(self.high, self.high_btn)

        if self.page is False:
            screen.blit(self.hs, self.hs_btn)
            screen.blit(self.back, self.back_btn)
            self.hss = self.title.render(str(stats.current), True, self.white)
            screen.blit(self.hss, self.hss_btn)

        # Display
        pygame.display.flip()
