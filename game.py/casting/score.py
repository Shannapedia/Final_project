from casting.actor import Actor

class Score(Actor):
    """ Score provide a message to count the score. """
    def __init__(self):
        super().__init__()
        self._message = 0
        
    def get_message(self):
        """ Gets the score message. """
        return self._message
    
    def set_message(self, message):
        """ Updates the message to the given one. """
        self._message = message

    def get_text(self):
        """ Gets score's text. """
        return self._text
