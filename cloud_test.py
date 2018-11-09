# This is a Python 3 script that creates a word cloud (really a phrase cloud) 
# of subject headings. To use phrases with the WordCloud library, you need to feed 
# a dictionary (not a list) with the phrase as a string and the frequency as an 
# integer. 

# References
# https://www.datacamp.com/community/tutorials/wordcloud-python
# https://stackoverflow.com/questions/26063231/read-specific-columns-with-pandas-or-other-python-module
# https://stackoverflow.com/questions/32737137/what-does-header-argument-in-pandas-read-csv-mean
# https://stackoverflow.com/questions/26716616/convert-a-pandas-dataframe-to-a-dictionary
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_dict.html
# https://stackoverflow.com/questions/38666527/what-is-the-necessity-of-plt-figure-in-matplotlib
# https://matplotlib.org/tutorials/colors/colormaps.html
# https://matplotlib.org/gallery/images_contours_and_fields/interpolation_methods.html
# https://minimaxir.com/2016/05/wordclouds/
# https://www.pythonanywhere.com/forums/topic/12097/


# Import the os library so you can use command line/shell type commands
# https://docs.python.org/2/library/os.html
import os

# Import numpy for handling multi-dimensional arrays and matrices
# http://www.numpy.org/
import numpy as np

# Import Pandas for data analysis
# https://pandas.pydata.org/
import pandas as pd

# Import Image from PIL (via Pillow, installed via PIP)
# https://pillow.readthedocs.io/en/5.3.x/; 
from PIL import Image

# Import the word cloud library
# https://github.com/amueller/word_cloud
from wordcloud import WordCloud

# Import matplotlib, which is a library that enables others libraries to plot
# https://matplotlib.org/index.html
import matplotlib.pyplot as plt

# Import various palettes with palettable (installed via PIP)
# https://jiffyclub.github.io/palettable/
from palettable.cartocolors.qualitative import Vivid_10

# Load subject heading data into pandas dataframe
# header=0 tells pandas that the first line in the file (in programmer counting)
# is where the column headers are.
df = pd.read_csv("ce_headings.csv", header=0)

# Convert normalized all caps headings into title case
df['NORMAL_HEADING'] = df['NORMAL_HEADING'].str.title()

# Convert the dataframe to a dictionary with the .to_dict split argument, which 
# treats the headers, data and indexes as different parts of a dictionary.
# By taking the 'data' part, you get a list of lists that can then be turned into a # clean dictionary.
headings = df.to_dict('split')

# WordCloud's "generate from frequencies" requires a dictionary with the string and 
# the frequency. Create a blank dictionary to hold the data.
headings_dict = {}

# Populate the dictionary with the header/frequency key value pairs from the data 
# part of .to_dict.
headings_dict = dict([(d[0], d[1]) for d in headings['data']])

# Check the output (remove when done)
print(headings_dict)

# Create the word cloud (WordCloud) and assign it to the variable wordcloud
wordcloud = WordCloud(
	# width/height = dimensions of the image
	width=1500,height=1000, 
	#  max words = the maximum words/phrases it will include
	max_words=200,
	# relative scaling is how much the size scales. 0 is not much difference (rank # is most important), 1 is the # most difference (frequency is most important).# It has to be between 0 and 1. Adjust depending on data and range of 
	# frequencies
	relative_scaling=.75,
	# whether to remove the trailing "s"
	normalize_plurals=False, 
	# background color default is black
	background_color="white",
	# colormap is a set of colors that can be used
	colormap=Vivid_10.mpl_colormap,
	min_font_size = 10
	# generate from frequencies tells WordCloud to use the frequency table rather # than tokenizing into words and requires the dictionary name as an argument.
	).generate_from_frequencies(headings_dict)

# Create a figure object
plt.figure()
# Tell it what the object should have in it (data = wordcloud variable and interpolation = how it scales color up and down)
plt.imshow(wordcloud, interpolation='none')
# Turn the axis lines off
plt.axis('off')
# Print the title (needs more space between)
plt.title('Monograph Subject Headings Published in Sri Lanka')
# Pops the image up on your screen
plt.show()
# Cleans up memory
plt.close()

# write the image to a png file in the same location as the script (why no title?)
wordcloud.to_file("first_attempt.png")




