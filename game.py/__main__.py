import random
from casting.actor import Actor
from casting.ships import Ships

from casting.score import Score
from casting.cast import Cast
from directing.director import Director
from services.keyboard_service import KeyboardService
from services.video_service import VideoService
from shared.color import Color
from shared.point import Point

FRAME_RATE = 12
MAX_X = 1500
MAX_Y = 900
CELL_SIZE = 30
FONT_SIZE = 30
COLS = 60
ROWS = 40
CAPTION = "Final Project"
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
DEFAULT_ITEMS = 20
ROCKS = 15
GEMS = 30


def main():

    cast = Cast()

    """ Create the banners """
    banner = Actor()
    banner.set_text("Player 1: 0")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    banner2 = Actor()
    banner2.set_text("Player 2: 0")
    banner2.set_font_size(FONT_SIZE)
    banner2.set_color(WHITE)
    banner2.set_position(Point(1300, 0))
    cast.add_actor("banners2", banner2)
    
    x = int(MAX_X - 300)
    y = int(MAX_Y - 300)
    position = Point(x, y)

    space_ship = Ships()
    space_ship.set_text()
    space_ship.set_font_size()
    space_ship.set_color(WHITE)
    space_ship.set_position(position)
    cast.add_actor("space_ships", space_ship)

    x2 = int(MAX_X - 1200)
    y2 = int(MAX_Y - 300)
    position2 = Point(x2, y2)

    space_ship2 = Ships()
    space_ship2.set_text()
    space_ship2.set_font_size()
    space_ship2.set_color(RED)
    space_ship2.set_position(position2)
    cast.add_actor("space_ships2", space_ship2)

    for i in range(GEMS):
        gem = "*"
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        score = Score()
        score.set_text(gem)
        score.set_font_size(FONT_SIZE)
        score.set_color(color)
        score.set_position(position)
        score.set_message(1)
        cast.add_actor("items", score)
        cast.remove_actor(space_ship, score)

    for i in range(ROCKS):
        rock = "o"
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        score = Score()
        score.set_text(rock)
        score.set_font_size(FONT_SIZE)
        score.set_color(color)
        score.set_position(position)
        score.set_message(1)
        cast.add_actor("items", score)
        cast.remove_actor(space_ship, score)    

    """ Initialize services that game uses and start """
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()