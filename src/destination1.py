import pygame
import os
import logging
import logging.handlers

logging.basicConfig(
    format="[%(asctime)s] [%(levelname)-10s] %(message)s", level=logging.INFO)

def main():
    # init the python game module.
    num_of_ok_init, num_of_bad_init = pygame.init()
    logging.info("Number of successful inits {}. Number of bad inits {}".format(
        num_of_ok_init, num_of_bad_init))

    # check if the game is correctly init.
    if pygame.get_init() == False:
        return

    logging.info("Game initialized. Starting..")

    # Set a logo. Recommended file formats for images are .jpeg and .png
    game_logo_path = os.path.join(os.path.dirname(
        __file__), "..", "resources/my_game_icon.jpeg")
    logging.debug("Icon resource path - {}".format(game_logo_path))
    game_logo = pygame.image.load(game_logo_path)
    pygame.display.set_icon(game_logo)

    logging.debug("Set game window logo..")

    # Set a window title
    pygame.display.set_caption("MyGame")

    # set up the window of the game
    screen = pygame.display.set_mode(size=(200, 200))
    game_running = True

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False


if __name__ == "__main__":
    main()
