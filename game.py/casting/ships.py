from casting.actor import Actor

"""This class contains a detail about the ships size, which we want to override to ensure consistency."""

class Ships(Actor):

    def __init__(self):
        super().__init__()
        self.set_font_size()
        self.set_text()

    def set_font_size(self):
        """ Updates the size of the ships to a fixed value, independant of anything else on the program. """
        self._font_size = 20
        return self._font_size

    def set_text(self):
        """The drawing of the spaceships, we override the set_text function in actor to ensure this is alwas a drawing"""
        self._text = ("""v
       /\\
       |__|
       |__|
    /|/\|\\""")
        return self._text
