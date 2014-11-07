import math as m

class Point(object):
	""" Represents a point in 2-D space.
	"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distance(self):
		return m.sqrt(self.x**2 + self.y**2)


pop = Point(3,4)
dist = pop.distance()



def print_point(p):
	print '(%g,%g)' % (p.x,p.y)

def distance_between_points(p):
	distance = math.sqrt(p.x**2 + p.y**2)
	print distance

