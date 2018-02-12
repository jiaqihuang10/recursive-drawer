import sys
import math
import Line_Point_colour

def draw_flake(center,length,color):
	x_distance = length*math.cos(math.pi/3)/2 #the distance from the center point to each start and end point
	y_distance = length*math.sin(math.pi/3)/2
	# points on the left side as start points
	#first line: start point and end point
	start_1 = Line_Point_colour.Point(center.x - x_distance, center.y + y_distance)
	end_1 = Line_Point_colour.Point(center.x + x_distance, center.y - y_distance)
	
	start_2 = Line_Point_colour.Point(center.x - length/2, center.y)
	end_2 = Line_Point_colour.Point(center.x + length/2, center.y)

	start_3 = Line_Point_colour.Point(center.x - x_distance, center.y - y_distance)
	end_3 = Line_Point_colour.Point(center.x + x_distance, center.y + y_distance)
	#generate 3 lines
	line1 = Line_Point_colour.Line(start_1, end_1,color)
	print 'line', line1
	line2 = Line_Point_colour.Line(start_2, end_2,color)
	print 'line', line2
	line3 = Line_Point_colour.Line(start_3, end_3,color)
	print 'line', line3

	#return a list of 6 new centers
	c1 = Line_Point_colour.Point(center.x - x_distance*2/3, center.y + y_distance*2/3)
	c2 = Line_Point_colour.Point(center.x + x_distance*2/3, center.y - y_distance*2/3)
	c3 = Line_Point_colour.Point(center.x - length/3, center.y)
	c4 = Line_Point_colour.Point(center.x + length/3, center.y)
	c5 = Line_Point_colour.Point(center.x - x_distance*2/3, center.y - y_distance*2/3)
	c6 = Line_Point_colour.Point(center.x + x_distance*2/3, center.y + y_distance*2/3)

	center_list = [c1,c2,c3,c4,c5,c6]
	return center_list

def recursive_draw (center_list,length,level,color):
	# end recursion if base case reached
	if (level == 0):
		return
	for center in center_list:
		recursive_draw(draw_flake(center,length,color), length/3, level-1,color)


# ********** process the command line arguments


if len(sys.argv) < 3:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' levels(>=1) length_of_diagonal(<=300) color(optional)'
	sys.exit(1)
try:
	level = int(sys.argv[1])
	if len(sys.argv) == 3:
		color = 'SkyBlue'
		length = int(sys.argv[2])
	elif len(sys.argv) == 4:
		length = int(sys.argv[2]) 
		color = sys.argv[3]	
		#get a list of all colors
		colors=[]
		try:
			color_file = open('css_colours.txt', 'r')
			for c in color_file:
				colors.append(c.strip())
		except IOError:
			print >> sys.stderr, 'Cannot open file: css_colours.txt'

		if color not in colors:
			print >> sys.stderr, 'Please provide a valid color name.'
			sys.exit(2)
	if length > 300:
		print >> sys.stderr, 'Please provide a valid length of diagonal(<= 300).'
		sys.exit(3)
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' levels(>=1) length_of_diagonal(<=300) color(optional)'
	sys.exit(4)
if level < 1 :
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' levels(>=1) length_of_diagonal(<=300) color(optional)'
	sys.exit(5)

##start from the center of the canvas

center_list = []
center = Line_Point_colour.Point(0.0,0.0)
center_list.append(center)

recursive_draw(center_list,length,level,color)








