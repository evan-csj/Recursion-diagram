# process command line arguments
if [ $# -ne 4 ]; then
	if [ $# -ne 3 ]; then
		echo "Syntax: bash TriangleStarSplit.sh depth_of_triangles starting_colour depth_of_star number_of_stars"
		echo "Note: leave starting_colour empty if you want a random starting colour"
		exit
	fi
fi

if [ $# -ne 4 ]; then

	triangle_depth=$1
	star_depth=$2
	star_number=$3

	# generate triangles
	python generate_triangles.py $triangle_depth > triangle.txt

	# generate a star
	python stars.py $star_depth < triangle.txt > star.txt

	# generate stars
	python split.py $star_number < star.txt > stars.txt
	python lines_to_svg_colour.py stars.txt > stars.svg
else
	triangle_depth=$1
	triangle_color=$2
	star_depth=$3
	star_number=$4

	# generate triangles
	python generate_triangles.py $triangle_depth $triangle_color > triangle.txt

	# generate a star
	python stars.py $star_depth < triangle.txt > star.txt

	# generate stars
	python split.py $star_number < star.txt > stars.txt
	python lines_to_svg_colour.py stars.txt > stars.svg
fi
