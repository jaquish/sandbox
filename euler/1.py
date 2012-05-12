import pyglet
import time

window = pyglet.window.Window()
pyglet.gl.glClearColor(.4,.4,.4,1)

BOARD_SIZE = 100

yes, no, unknown = range(3)
no_color       = (255 ,  20,   20, 255)
yes_color      = (20  ,  255,  20, 255)
unknown_color  = (20  ,  20 , 255, 255)

class Board:
	def __init__(self, size):
		self.state = [unknown]*size
		
		self.toDraw = []
		for i in range(len(self.state)):
			label = pyglet.text.Label(
						str(i), 
                        font_name='Times New Roman Bold', 
                        font_size=14,
                        x=(40*i) % (40*10), y= window.height - (i/10 * 40),
                        anchor_x='left', anchor_y='top')
			self.toDraw.append(label)

		self.current = 0

	def printme(self):
		
		for i in range(len(self.state)):
			self.toDraw[i].draw()

	def compute_next(self,dt):

		i = self.current
		if (i >= len(self.state)):
			return

		if (i % 3 == 0):
			self.state[i] = yes
			self.toDraw[i].color = yes_color
		elif (i % 3 == 1):
			self.state[i] = no
			self.toDraw[i].color = no_color
		else:
			self.state[i] = unknown	
			self.toDraw[i].color = unknown_color

		self.current += 1
		self.toDraw[i].draw()

@window.event
def on_draw():
	window.clear()
	b.printme()

b = Board(BOARD_SIZE)


pyglet.clock.schedule_interval(b.compute_next, 0.01)
pyglet.app.run()
