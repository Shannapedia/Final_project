from shared.point import Point
from casting.actor import Actor
from shared.color import Color

MAX_X = 1500
MAX_Y = 900
WHITE = Color(255, 255, 255)

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._keyboard_service2 = keyboard_service
        self.score = 0

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the space_ship.
        """
        space_ship = cast.get_first_actor("space_ships")
        space_ship2 = cast.get_first_actor("space_ships2")
        items = cast.get_actors("items")
        velocity = self._keyboard_service.get_direction()
        velocity2 = self._keyboard_service2.get_direction2()
        art_velocity = self._keyboard_service.move_direction()
        space_ship.set_velocity(velocity2)
        space_ship2.set_velocity(velocity)
        for item in items: 
            item.set_velocity(art_velocity)


    def _do_updates(self, cast):
        """Updates the space_ship's position and resolves any collisions with items.
        """
        banner = cast.get_first_actor("banners")
        banner2 = cast.get_first_actor("banners2")
        space_ship = cast.get_first_actor("space_ships")
        space_ship2 = cast.get_first_actor("space_ships2")
        items = cast.get_actors("items")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        space_ship.move_next(max_x, max_y)
        space_ship2.move_next(max_x, max_y)

        for item in items:
            item.move_next(max_x, max_y)
            if space_ship.get_position().equals(item.get_position()):
                if item.get_text() == "*":
                    message = item.get_message()
                    self.score += message
                    banner2.set_text(f"Player 2: {self.score}")
                    cast.remove_actor("items", item) 
                    if self.score == 10:
                        x = int(MAX_X / 2)
                        y = int(MAX_Y / 2)
                        position = Point(x, y)
                        message = Actor()
                        message.set_text(f"Game Over! \nPLayer 2 Won! {self.score} Points!")
                        message.set_position(position)
                        cast.add_actor("messages", message)
                        space_ship.set_color(WHITE)
                        space_ship2.set_color(WHITE)
                        for item in items:
                            item.set_color(WHITE)
                elif item.get_text() == "o":
                    message = item.get_message()
                    self.score -= message
                    banner2.set_text(f"Player 2: {self.score}")
                    cast.remove_actor("items", item)
                    if self.score < 0:
                        self.score = 0
                        banner2.set_text(f"Score: {self.score}")

        for item in items:
            if space_ship2.get_position().equals(item.get_position()):
                if item.get_text() == "*":
                    message = item.get_message()
                    self.score += message
                    banner.set_text(f"Player 1: {self.score}")
                    cast.remove_actor("items", item)
                    if self.score == 10:
                        x = int(MAX_X / 2)
                        y = int(MAX_Y / 2)
                        position = Point(x, y)
                        message = Actor()
                        message.set_text(f"Game Over! \nPLayer 1 Won! {self.score} Points!")
                        message.set_position(position)
                        cast.add_actor("messages", message)
                        space_ship.set_color(WHITE)
                        space_ship2.set_color(WHITE)
                        for item in items:
                            item.set_color(WHITE)                     
                elif item.get_text() == "o":
                    message = item.get_message()
                    self.score -= message
                    banner.set_text(f"Player 1: {self.score}")
                    cast.remove_actor("items", item)
                    if self.score < 0:
                        self.score = 0
                        banner.set_text(f"Score: {self.score}")


    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        """      
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()         