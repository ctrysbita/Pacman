from enum import Enum

import pygame

import colors as colors
import util as util
from level import Level


class GameState(Enum):
    WELCOME = 0
    PLAYING = 1
    WIN = 2
    OVER = 3


class Game:
    def __init__(self):
        pygame.display.set_caption('Pacman')
        self.screen = pygame.display.set_mode([606, 606])

        pygame.mixer.init()

        pygame.font.init()
        self.font_small = pygame.font.Font('res/alger.ttf', 18)
        self.font_big = pygame.font.Font('res/alger.ttf', 24)
        self.font_title_small = pygame.font.Font('res/alger.ttf', 32)
        self.font_title_big = pygame.font.Font('res/alger.ttf', 72)

        self.clock = pygame.time.Clock()
        self.state = GameState.WELCOME
        self.score = 0

    def welcome(self):
        pygame.mixer.music.stop()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit(0)
                    elif event.key == pygame.K_RETURN:
                        self.state = GameState.PLAYING
                        return

            self.screen.fill(colors.WHITE)

            background_png = pygame.image.load('res/background.png')
            self.screen.blit(background_png, (0, 0))
            play_caption = self.font_big.render('Press ENTER to play', True,
                                                colors.BLACK)
            self.screen.blit(play_caption, (160, 300))
            play_caption = self.font_big.render('Press ESC to exit', True,
                                                colors.BLACK)
            self.screen.blit(play_caption, (180, 350))

            pygame.display.flip()

    def play(self):
        pygame.mixer.music.stop()
        # Load and Play BGM
        pygame.mixer.music.load('res/bgm.ogg')
        pygame.mixer.music.set_volume(0.75)
        pygame.mixer.music.play(-1, 0.0)

        level = Level()
        wall_sprites = level.setup_walls(colors.SKYBLUE)
        gate_sprites = level.setup_gate(colors.WHITE)
        hero_sprites, ghost_sprites = level.setup_players()
        food_sprites = level.setup_food(colors.YELLOW, colors.WHITE)
        super_food_sprites = level.setup_super_food(colors.YELLOW,
                                                    colors.WHITE)
        path_data = level.setup_path_data()

        self.score = 0
        movement = util.Vector2.zero()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = GameState.WELCOME
                        return
                    elif event.key == pygame.K_LEFT:
                        movement = util.Vector2.left()
                    elif event.key == pygame.K_RIGHT:
                        movement = util.Vector2.right()
                    elif event.key == pygame.K_UP:
                        movement = util.Vector2.up()
                    elif event.key == pygame.K_DOWN:
                        movement = util.Vector2.down()

            self.screen.fill(colors.BLACK)

            for hero in hero_sprites:
                hero.update(wall_sprites, gate_sprites, movement)

            for hero in hero_sprites:
                self.score += len(
                    pygame.sprite.spritecollide(hero, food_sprites, True))
                self.score += 2 * len(
                    pygame.sprite.spritecollide(hero, super_food_sprites,
                                                True))
            for hero in hero_sprites:
                for ghost in ghost_sprites:
                    if ghost.AIProgram is not None:
                        tmp_move_buffer = ghost.AIProgram(
                            path_data, ghost, hero)
                    ghost.update(wall_sprites, gate_sprites, tmp_move_buffer)

            wall_sprites.draw(self.screen)
            gate_sprites.draw(self.screen)
            food_sprites.draw(self.screen)
            super_food_sprites.draw(self.screen)
            hero_sprites.draw(self.screen)
            ghost_sprites.draw(self.screen)

            score_text = self.font_small.render("Score: %s" % self.score, True,
                                                colors.RED)
            self.screen.blit(score_text, (10, 10))

            if len(food_sprites) == 0 and len(super_food_sprites) == 0:
                self.state = GameState.WIN
                return

            if pygame.sprite.groupcollide(ghost_sprites, hero_sprites, False,
                                          False):
                self.state = GameState.OVER
                return

            pygame.display.flip()
            self.clock.tick(30)

    def show_score(self):
        pygame.mixer.music.stop()

        # Attach a translucent layer.
        translucent_layer = pygame.Surface((606, 606))
        translucent_layer.set_alpha(255*0.9)
        translucent_layer.fill(colors.WHITE)
        self.screen.blit(translucent_layer, (0, 0))

        if self.state == GameState.WIN:
            self.win()
        else:
            self.over()

    def win(self):
        # Load And Play win music
        pygame.mixer.music.load('res/win.ogg')
        pygame.mixer.music.play()

        welcome_title = self.font_title_small.render('Congratulations!', True, colors.BLACK)
        self.screen.blit(welcome_title, (150, 100))
        welcome_title = self.font_title_big.render('YOU WIN!', True, colors.SKYBLUE)
        self.screen.blit(welcome_title, (150, 148))
        score = self.font_big.render('Score: %s' % self.score, True,
                                     colors.BLACK)
        self.screen.blit(score, (250, 225))
        play_caption = self.font_big.render('Press ENTER to Replay', True, colors.BLACK)
        self.screen.blit(play_caption, (160, 300))
        play_caption = self.font_big.render('Press ESC to exit', True, colors.BLACK)
        self.screen.blit(play_caption, (180, 350))

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = GameState.WELCOME
                        return
                    elif event.key == pygame.K_RETURN:
                        self.state = GameState.PLAYING
                        return

    def over(self):
        # Load And Play lose music
        pygame.mixer.music.load('res/lose.ogg')
        pygame.mixer.music.play()

        welcome_title = self.font_title_big.render('Game Over', True, colors.RED)
        self.screen.blit(welcome_title, (115, 100))
        score = self.font_big.render('Final Score: %s' % self.score, True,
                                     colors.BLACK)
        self.screen.blit(score, (200, 200))
        play_caption = self.font_big.render('Press ENTER to Replay', True, colors.BLACK)
        self.screen.blit(play_caption, (160, 300))
        play_caption = self.font_big.render('Press ESC to exit', True, colors.BLACK)
        self.screen.blit(play_caption, (180, 350))

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = GameState.WELCOME
                        return
                    elif event.key == pygame.K_RETURN:
                        self.state = GameState.PLAYING
                        return

    def run(self):
        # State Machine Switch
        while True:
            {
                GameState.WELCOME: self.welcome,
                GameState.PLAYING: self.play,
                GameState.WIN: self.show_score,
                GameState.OVER: self.show_score
            }[self.state]()

if __name__ == '__main__':
    Game().run()