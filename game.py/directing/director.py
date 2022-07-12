from pyparsing import White
from casting.cast import Cast
from casting.lives import Lives
from shared.point import Point
from scripting.game_over import GameOver
from casting.actor import Actor

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.score = 0
        # for i in range(3):
        #     self.lives = "#"
        #     score = Lives()
        #     score.set_text(self.lives)
        #     score.set_font_size(30)
        #     score.set_color(White)
        #     score.set_position(Point(1200, 0))
        #     score.set_message(1)
        #     cast = Cast()
        #     cast.add_actor("lives", score)
        #     cast.remove_actor(self.lives, score)
        # self.lives = "# # #"



    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the space_ship.
        
        Args:
            cast (Cast): The cast of actors.
        """
        space_ship = cast.get_first_actor("space_ships")
        items = cast.get_actors("items")
        velocity = self._keyboard_service.get_direction()
        art_velocity = self._keyboard_service.move_direction()
        space_ship.set_velocity(velocity)
        for item in items: 
            item.set_velocity(art_velocity)


    def _do_updates(self, cast):
        """Updates the space_ship's position and resolves any collisions with items.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        banner2 = cast.get_first_actor("lives")
        lives = Actor()
        lives.set_text("# # #")
        cast.add_actor("lives", lives)
        #the guy youre using, only moves right and left-- the gem catcher - cristian
        space_ship = cast.get_first_actor("space_ships")
        #these are meant to be moving too
        items = cast.get_actors("items")

        # banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        space_ship.move_next(max_x, max_y)

        #for loop to display the massege of the score when the space_ship has the same position as the gem or rock.
        for item in items:
            item.move_next(max_x, max_y)
            if space_ship.get_position().equals(item.get_position()):
                if item.get_text() == "*":
                    message = item.get_message()
                    self.score += message
                    banner.set_text(f"Score: {self.score}")
                    banner2.set_text(f"Lives: {lives}")
                    # added this!!! it removes the items when we touch them
                    cast.remove_actor("items", item) 
                elif item.get_text() == "o":
                    message = item.get_message()
                    self.score -= message
                    cast.remove_actor("lives", lives)
                    banner.set_text(f"Score: {self.score}")
                    banner2.set_text(f"Lives: {lives}")
                    cast.remove_actor("item", item)
                    if self.score < 0:
                        self.score = 0
                        banner.set_text(f"Score: {self.score}")
                        cast.remove_actor("items", item) 
                        if banner2 == "":
                            self._is_game_over = True

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()