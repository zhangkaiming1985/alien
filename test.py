class Base:
	def __init__(self):
		print("it is base class.")


class Leaf(Base):
	def __init__(self):
		# Base.__init__(self)
		super().__init__()
		print("it is leaf class")

test = Leaf()
