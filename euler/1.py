import pyglet

window = pyglet.window.Window()


yes, no, unknown = range(3)

class Board:
	def __init__(self, size):
		self.state = ['unknown']*size

	def printme(self):
		for i in range(len(self.state)):
			label = pyglet.text.Label(str(i), 
                          font_name='Times New Roman Bold', 
                          font_size=14,
                          x=(40*i) % (40*10), y= window.height - (i/10 * 40),
                          anchor_x='left', anchor_y='top')
			label.draw();

@window.event
def on_draw():
	window.clear()
	b.printme()

b = Board(100)
pyglet.app.run()
