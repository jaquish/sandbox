import pyglet

window = pyglet.window.Window()
pyglet.gl.glClearColor(.4,.4,.4,1)


yes, no, unknown = range(3)

class Board:
	def __init__(self, size):
		self.state = [unknown]*size

	def printme(self):
		for i in range(len(self.state)):
			label = pyglet.text.Label(
						str(i), 
                        font_name='Times New Roman Bold', 
                        font_size=14,
                        x=(40*i) % (40*10), y= window.height - (i/10 * 40),
                        anchor_x='left', anchor_y='top')

			no_color       = (255 ,  20,   20, 255)
			yes_color      = (20  ,  255,  20, 255)
			unknown_color  = (20  ,  20 , 255, 255)

			if   (self.state[i] == no):
				label.color = no_color
			elif (self.state[i] == yes):
			 	label.color = yes_color
			else:
			 	label.color = unknown_color

			label.draw()

	def compute(self):
		for i in range(len(self.state)):
			if (i % 3 == 0):
				self.state[i] = yes
			elif (i % 3 == 1):
				self.state[i] = no
			else:
				self.state[i] = unknown	

@window.event
def on_draw():
	window.clear()
	b.printme()

b = Board(100)
pyglet.app.run()

b.compute()

