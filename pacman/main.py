import pygame

import colors
import util
from level import Level


class Game:
    def __init__(self):
        pygame.display.set_caption('Pacman')
        self.screen = pygame.display.set_mode([606, 606])

        pygame.mixer.init()
        pygame.mixer.music.load('res/bgm.ogg')
        pygame.mixer.music.play(-1, 0.0)

        pygame.font.init()
        self.font_small = pygame.font.Font('res/alger.ttf', 18)
        self.font_big = pygame.font.Font('res/alger.ttf', 24)

        self.clock = pygame.time.Clock()

    def run(self):
        level = Level()
        wall_sprites = level.setup_walls(colors.SKYBLUE)
        gate_sprites = level.setup_gate(colors.WHITE)
        hero_sprites, ghost_sprites = level.setup_players()
        food_sprites = level.setup_food(colors.YELLOW, colors.WHITE)
        super_food_sprites = level.setup_super_food(colors.YELLOW,
                                                    colors.WHITE)
        path_data = level.setup_path_data()
        
        score = 0
        movement = util.Vector2.zero()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        movement = -1 * util.Vector2.right()
                    elif event.key == pygame.K_RIGHT:
                        movement = util.Vector2.right()
                    elif event.key == pygame.K_UP:
                        movement = util.Vector2.up()
                    elif event.key == pygame.K_DOWN:
                        movement = -1 * util.Vector2.up()

            self.screen.fill(colors.BLACK)

            for hero in hero_sprites:
                hero.update(wall_sprites, gate_sprites, movement)

            for hero in hero_sprites:
                score += len(
                    pygame.sprite.spritecollide(hero, food_sprites, True))
                score += 2 * len(
                    pygame.sprite.spritecollide(hero, super_food_sprites,
                                                True))
            for hero in hero_sprites:
                for ghost in ghost_sprites:
                    if ghost.AIProgram is not None:
                        tmp_move_buffer = ghost.AIProgram(path_data, ghost, hero)
                    ghost.update(wall_sprites, gate_sprites, tmp_move_buffer)

            wall_sprites.draw(self.screen)
            gate_sprites.draw(self.screen)
            hero_sprites.draw(self.screen)
            ghost_sprites.draw(self.screen)
            food_sprites.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)


if __name__ == '__main__':
    Game().run()
