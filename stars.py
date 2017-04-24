import sys
import copy
import math
import Line_Point_colour

def draw_star(lines, n):
	new_lines = copy.deepcopy(lines)

	for i in range(n):
		for line in new_lines:
			line.rotate(2*math.pi/n)
			print 'line', line

def load_line_file(file_object):
	line_objects = [ ]
	for line in file_object:
		# convert text line to a Line object
		line_object = line.split()
		point0 = Line_Point_colour.Point(float(line_object[1]), float(line_object[2]))
		point1 = Line_Point_colour.Point(float(line_object[3]), float(line_object[4]))
		line_object = Line_Point_colour.Line(point0, point1, line_object[5])

		line_objects.append(line_object)
	
	return line_objects

if len(sys.argv) != 2:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' star_layers'
	sys.exit(1)
try:
	star_layers = int(sys.argv[1])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' star_layers'
	sys.exit(2)
if star_layers < 1:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' star_layers'
	sys.exit(3)

L = load_line_file(sys.stdin)

draw_star(L, star_layers)
