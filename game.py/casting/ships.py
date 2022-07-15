from casting.actor import Actor

class Ships(Actor):
    def set_font_size(self):
        """ Updates the size of the ships to a fixed value, independant of anything else on the program. """
        self._font_size = 20
        return self._font_size
