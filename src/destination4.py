import logging
import logging.handlers
import pygame as pg
import pygame_commons.pgbase as pgbase
from football.ItemPosition import *
from football.Team import *

logging.basicConfig(
    format="[%(asctime)s] [%(levelname)-10s] %(message)s", level=logging.INFO)


def main():
    pg.init()
    if not pg.get_init():
        return

    pgbase.set_logo()
    pgbase.set_game_window_title("Futbol")
    surface = pgbase.setup_display_surface(500, 1000)

    players_in_team = 7
    # F-M-D
    formation = ["3-2-1", "1-3-2", "2-2-2"]

    team_1 = Team(5, formation[0], 'red')
    team_2 = Team(5, formation[2], 'blue')

    team1_y = 100
    for player in team_1:
        player.draw(surface, center=Position(100, team1_y))
        team1_y += 50

    team2_y = 100
    for player in team_2:
        player.draw(surface, center=Position(800, team2_y))
        team2_y += 50

    game_running = True
    while game_running:
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False

    return


if __name__ == "__main__":
    main()
