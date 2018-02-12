# process command line arguments
if [ $# -ne 3 ]; then
	echo "Syntax: bash snow_flower.sh number_of_levels snowflake_levels color"
	exit
fi

number_of_levels=$1
snowflake_levels=$2
color=$3

snowflake_diagonal="250"

if [ "$number_of_levels" = "3" ]; then
	#echo "too big"
	snowflake_diagonal="200" #no space before and after =
fi

if [ "$number_of_levels" = "4" ]; then
	#echo "too big"
	snowflake_diagonal="120" #no space before and after =
fi

# generate snowflake
python generate_snowflake.py $snowflake_levels $snowflake_diagonal $color > snowflake.txt
# replicate snowflakes to form a flower
python transform_snowflake.py $number_of_levels < snowflake.txt > snow_flower.txt
python lines_to_svg_colour.py snow_flower.txt > snow_flower.svg
