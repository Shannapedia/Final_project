class Cast:
    """ A collection of actors. Cast is keeps track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name. """

    def __init__(self):
        """ Constructs a new Actor. """
        self._actors = {}
        
    def add_actor(self, group, actor):
        """ Adds an actor to the given group. """
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        """ Gets the actors in the given group. """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        """ Gets all of the actors in the cast. """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_first_actor(self, group):
        """ Gets the first actor in the given group. """
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    def get_second_actor(self, group):
        """ Gets the first actor in the given group. """
        result = None
        if group in self._actors.keys():
            result = self._actors[group][1]
        return result    

    def remove_actor(self, group, actor):
        """ Removes an actor from the given group. """
        if group in self._actors:
            self._actors[group].remove(actor)