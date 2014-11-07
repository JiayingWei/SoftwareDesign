def extract_class_info(filepath):
	"""read raw_text file, calculate GPA for each student. Write a file called class-grades.txt that contain 10line showing the students name followed by their gpa.
	"""
	f = open(filepath)
	lines = f.readlines()
	classmates = []
	for linenum in range(len(lines)):
		parse_student = lines[linenum].split(',')	#splits each line into seperate student information
		classmates.append(Student(parse_student[0]))
		letter_grades = []
		for grades in range(1,len(parse_student)):
			parse_student[grades] = parse_student[grades][1:2]
			letter_grades.append(parse_student[grades])
		classmates[linenum].grades = letter_grades
	return classmates

class Student(object):
	""" Creates a student object with a name, list of grades, and a GPA
	"""
	def __init__(self,name):
		self.name = name
		self.grades = []
		self.GPA = 0

	def __str__(self):
		return "%s's grade point average is %f" % (self.name, self.GPA)

	def calc_gpa(self,inputgrades, depth, originaldepth):
		"""Takes a list of grades, and then returns the calculated GPA
		"""
		gradeToNum = {'A': 4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.0}
		if depth == 1:
			self.GPA =  round(inputgrades[0]/originaldepth, 2)
			return self.name + ' ' + str(self.GPA)
		if inputgrades[0] in ['A','B','C','D','F']:
			inputgrades[0] = gradeToNum[inputgrades[0]]
		return self.calc_gpa([sum([inputgrades[0], gradeToNum[inputgrades[1]]])] + inputgrades[2:], depth - 1, originaldepth)

	def name_GPA(self,):
		"""creates a tuple of the person's name and gpa, while also determining if they will graduate or become a super senior
		"""
		self.tuple = (self.name, self.GPA)
		if self.GPA >= 2.5:
			self.status = 'graduated'
		else:
			self.status = 'supersenior'

def write_class_gpa(raw_grades):
	"""writes the class GPAs of all the students in the class
	"""
	classmates = extract_class_info(raw_grades)
	calculated_GPAs = []
	graduates = []
	superseniors = []
	grad_dict = {}
	supersr_dict = {}
	for classmate in classmates:
		calculated_GPAs.append(classmate.calc_gpa(classmate.grades, len(classmate.grades), len(classmate.grades)))
		classmate.name_GPA()
		print classmate
		if classmate.status == 'graduated':
			graduates.append(classmate.tuple)
			grad_dict[classmate.name] = classmate.GPA
		elif classmate.status == 'supersenior':
			superseniors.append(classmate.tuple)
			supersr_dict[classmate.name] = classmate.GPA
	print '\ngraduates list : '
	print graduates
	print 'superseniors list : '
	print superseniors
	print '\ngraduates dictionary : '
	print grad_dict
	print 'superseniors dictionary : '
	print supersr_dict

	filename = 'class-grades'
	with open(filename, 'w') as fileout:
		for name in calculated_GPAs:
			fileout.write(str(name + '\n'))



write_class_gpa('raw_grades.txt')
