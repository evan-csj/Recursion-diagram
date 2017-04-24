import sys
import copy
import math
import Line_Point_colour

def draw_split(lines, m):
	for j in range(0,m):
		for k in range(0,m):
			new_lines = copy.deepcopy(lines)
			for line in new_lines:
				line.scale(float(1.0/m))
				line.translate(float((500.0/(m*2.0))-250.0+(500.0/m)*j), float((500.0/(m*2.0))-250.0+(500.0/m)*k))
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
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' split_factor'
	sys.exit(1)
try:
	split_factor = int(sys.argv[1])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' split_factor'
	sys.exit(2)
if split_factor < 1:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' split_factor'
	sys.exit(3)

L = load_line_file(sys.stdin)

draw_split(L, split_factor)
