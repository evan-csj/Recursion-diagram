import sys
import Line_Point_colour
#NOTE: We asked permission to import random and we were approved
import random

colourList =['AliceBlue','AntiqueWhite','Aqua','Aquamarine','Azure','Beige','Bisque','Black','BlanchedAlmond','Blue','BlueViolet','Brown','BurlyWood','CadetBlue','Chartreuse','Chocolate','Coral','CornflowerBlue','Cornsilk','Crimson','Cyan','DarkBlue','DarkCyan','DarkGoldenRod','DarkGray','DarkGrey','DarkGreen','DarkKhaki','DarkMagenta','DarkOliveGreen','DarkOrange','DarkOrchid','DarkRed','DarkSalmon','DarkSeaGreen','DarkSlateBlue','DarkSlateGray','DarkSlateGrey','DarkTurquoise','DarkViolet','DeepPink','DeepSkyBlue','DimGray','DimGrey','DodgerBlue','FireBrick','FloralWhite','ForestGreen','Fuchsia','Gainsboro','GhostWhite','Gold','GoldenRod','Gray','Grey','Green','GreenYellow','HoneyDew','HotPink','IndianRed','Indigo','Ivory','Khaki','Lavender','LavenderBlush','LawnGreen','LemonChiffon','LightBlue','LightCoral','LightCyan','LightGoldenRodYellow','LightGray','LightGrey','LightGreen','LightPink','LightSalmon','LightSeaGreen','LightSkyBlue','LightSlateGray','LightSlateGrey','LightSteelBlue','LightYellow','Lime','LimeGreen','Linen','Magenta','Maroon','MediumAquaMarine','MediumBlue','MediumOrchid','MediumPurple','MediumSeaGreen','MediumSlateBlue','MediumSpringGreen','MediumTurquoise','MediumVioletRed','MidnightBlue','MintCream','MistyRose','Moccasin','NavajoWhite','Navy','OldLace','Olive','OliveDrab','Orange','OrangeRed','Orchid','PaleGoldenRod','PaleGreen','PaleTurquoise','PaleVioletRed','PapayaWhip','PeachPuff','Peru','Pink','Plum','PowderBlue','Purple','RebeccaPurple','Red','RosyBrown','RoyalBlue','SaddleBrown','Salmon','SandyBrown','SeaGreen','SeaShell','Sienna','Silver','SkyBlue','SlateBlue','SlateGray','SlateGrey','Snow','SpringGreen','SteelBlue','Tan','Teal','Thistle','Tomato','Turquoise','Violet','Wheat','White','WhiteSmoke','Yellow','YellowGreen']

def recursive_draw(point0, point1, point2, depth, rand):
	# end recursion if base case reached
	if (depth == 0):
		return
	
	point0New = Line_Point_colour.Point((point0.x + point1.x)/2,(point0.y + point1.y)/2)
	point1New = Line_Point_colour.Point((point1.x + point2.x)/2,(point1.y + point2.y)/2)
	point2New = Line_Point_colour.Point((point0.x + point2.x)/2,(point0.y + point2.y)/2)
	side0 = Line_Point_colour.Line(point0New, point1New, colourList[rand])
	side1 = Line_Point_colour.Line(point1New, point2New, colourList[rand])
	side2 = Line_Point_colour.Line(point0New, point2New, colourList[rand])
	print 'line', side0
	print 'line', side1
	print 'line', side2
	
	if rand+1 >= len(colourList):
		rand = 0

	# continue with recursion
	recursive_draw(point0, point0New, point2New, depth-1, rand+1)
	recursive_draw(point0New, point1, point1New, depth-1, rand+1)
	recursive_draw(point2New, point1New, point2, depth-1, rand+1)	
# ********** process the command line arguments

if not (len(sys.argv) == 2 or len(sys.argv) == 3):
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' depth colour_number'
	sys.exit(1)
try:
	depth = int(sys.argv[1])
	if len(sys.argv) == 3:
		colour = int(sys.argv[2])
	else:
		colour = random.randint(0, len(colourList)-1)
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' depth colour_number'
	sys.exit(2)
if depth < 1 or colour < 0 or colour > 147:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' depth colour_number'
	sys.exit(3)

point0 = Line_Point_colour.Point(-125.0,-108.5)
point1 = Line_Point_colour.Point(125.0,-108.5)
point2 = Line_Point_colour.Point(0.0,108.5)
side0 = Line_Point_colour.Line(point0, point1)
side1 = Line_Point_colour.Line(point1, point2)
side2 = Line_Point_colour.Line(point0, point2)

print 'line', side0
print 'line', side1
print 'line', side2

recursive_draw(point0, point1, point2, depth-1, colour)
