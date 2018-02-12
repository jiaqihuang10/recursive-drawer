
import sys
import copy
import math
import Line_Point_colour


def draw(lines, scale, n, delta_y):
	new_lines = copy.deepcopy(lines)
	
	for line in new_lines:
		line.translate(0.0, delta_y)
		print 'line', line

	for line in new_lines:
		line.scale(scale)
		print 'line', line

	for i in range(n-1):
		for line in new_lines:
			line.rotate(2*math.pi/n)
			print 'line',line


def load_line_file(file_object):
	line_objects = [ ]
	for line in file_object:
		# convert text line to a Line object
		line_object = line.split()
		point0 = Line_Point_colour.Point(float(line_object[1]), float(line_object[2]))
		point1 = Line_Point_colour.Point(float(line_object[3]), float(line_object[4]))
		#######
		color = line_object[5]
		line_object = Line_Point_colour.Line(point0, point1,color)
		#######
		line_objects.append(line_object)
	
	return line_objects

# ***** process command line arguments

if len(sys.argv) != 2:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' Num of levels'
	sys.exit(1)
try:
	number_of_rings = int(sys.argv[1])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' Num of levels'
	sys.exit(2)
if number_of_rings < 1 or number_of_rings > 5:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' Must Be >1 and <5'
	sys.exit(3)

L = load_line_file(sys.stdin)

# ***** generate the rings

parameters = [
#	scale		rotation          transform
	[1.0,		1,                     0.0],
	[1.2,		6,                    25.0],
	[1.5,		12,                  50.0],
	[1.7,		18,                  75.0],
	[2.0,		24,                  100.0],
]

for i in range(number_of_rings):
	draw(L, parameters[i][0], parameters[i][1], parameters[i][2])


