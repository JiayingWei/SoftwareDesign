class Point(object):
	""" Represents a point in 2-D space.
	"""
	def __init__(self,x = 0,y = 0):
		self.x = x
		self.y = y

	def __str__(self):
		return '(%g,%g)' % (chicken.x,chicken.y)

class Rectangle(object):
	"""Represents a Rectangle.

	attributes: width, height, corner.
	"""
	def __init__(self,width,height,corner ):
		self.width = width
		self.height = height
		self.corner = corner

	def move_rectangle(self,rect, dx, dy):
		self.corner.x = self.corner.x - dx
		self.corner.y = self.corner.y - dy

bob = Rectangle(width = 100, height = 100, corner = Point(0, 0))
print bob