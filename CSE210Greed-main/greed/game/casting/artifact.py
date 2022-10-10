from game.casting.actor import Actor
class Artifact(Actor):
    #inheritance form actor. but artifacts should manage points
    def __init__(self):
        self._points = 1        
    def get_points(self):
        #return point
        return self._points

    def set_points(self, points):
       #setting point when with the given arg
        self._points = points
        