import random

from casting.actor import Actor
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
DEFAULT_ARTIFACTS = 20


def main():

    cast = Cast()

    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    banner2 = Actor()
    banner2.set_text("Go")
    banner2.set_font_size(FONT_SIZE)
    banner2.set_position(Point(1200, 0))
    cast.add_actor("banners", banner2)
    
    x = int(MAX_X / 2)
    y = int(MAX_Y - 30)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    

    for i in range(DEFAULT_ARTIFACTS):
        random_symbol=["*","o"]
        text = random.choice(random_symbol)

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        score = Score()
        score.set_text(text)
        score.set_font_size(FONT_SIZE)
        score.set_color(color)
        score.set_position(position)
        score.set_message(1)
        cast.add_actor("artifacts", score)
        cast.remove_actor(robot, score)

    """ Initialize services that game use and start """
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()