import pyray


class VideoService:
    #draw the window for the game

    def __init__(self, caption, width, height, size_cell, frame_rate, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = size_cell
        self._frame_rate = frame_rate
        self._debug = debug

    def close_window(self):
        #Closes the window and releases all computing resources
        pyray.close_window()

    def clear_buffer(self):
        #Clears the buffer in preparation for the next rendering.
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._drawGrid()
    
    def draw_actor(self, actor):
        #Draws the actor's text on the screen.
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()
        pyray.draw_text(text, x, y, font_size, color)
        
    def draw_actors(self, actors):
        #Draws the text for the given list of actors .actors is a list
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        #Copies the buffer contents to the screen. 
        pyray.end_drawing()

    def get_cell_size(self):
        #returb the video screen's cell size.
        return self._cell_size

    def get_height(self):
        #encapsulate the video screen's height.
        return self._height

    def get_width(self):
        #encapsulate the video screen's width.
        return self._width

    def is_window_open(self):
        #returnboolean: True if the window is closing
        return not pyray.window_should_close()

    def openWindow(self):
        #using methods from pyray to render the screen
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)

    def _drawGrid(self):
        #drawing a grid
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)
        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)