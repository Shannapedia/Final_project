from casting.actor import Actor
from scripting.action import Action
from shared.point import Point
from directing.director import Director
from shared.color import Color

MAX_X = 1500
MAX_Y = 900
WHITE = Color(255, 255, 255)

class GameOver(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of GameOver is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new GameOver."""
        self._is_game_over = False

def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_game_over(cast)
            
def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            space_ship = cast.get_first_actor("space_ships")
            items = cast.get_actors("items")

            x = int(MAX_X / 2)
            y = int(MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)
            space_ship.set_color(WHITE)

            for item in items:
                item.set_color(WHITE)