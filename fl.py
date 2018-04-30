#!/usr/bin/python3

import re
import sys
import os
import exifread
import numpy as np
import matplotlib.pyplot as plt




file_termination = sys.argv[1]
directory = sys.argv[2]

if len(sys.argv) > 3:
	target = sys.argv[3]
else:
	target = "EXIF FocalLength"

files = os.listdir(directory)

buckets = {}

# Count the frequencies
for file in files:
	if re.search("." + sys.argv[1] + "$",  file):
		print(file)
		# Open image file for reading (binary mode)
		f = open(directory + "/" + file, 'rb')
		# Return Exif tags
		tags = exifread.process_file(f)
		# Get focal length
		focal = tags[target]
		# for tag in tags.keys():
		# 	if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
		# 		print ("Key: %s, value %s" % (tag, tags[tag]))
		key = int(str(focal))
		if key in buckets:
			buckets[key] = buckets[key] + 1
		else:
			buckets[key] = 1
		print(focal)


# Order by key

tags_found = sorted(buckets.items(), key=lambda x: x[0])


# Get lists for x and y axis
x, y = zip(*tags_found)
x = list(x)
y = list(y)

print (x)
print (y)

# Get cumulative percentages
total = sum(y)
y_cu = []
curr = 0.0
for val in y:
	curr += val/total
	y_cu.append(curr)

print(y_cu)





# plot the cumulative histogram

# n, bins, patches = plt.hist(x, n_bins, density=True, histtype='step',
#                            cumulative=False, label='FocalLength')
fig, ax = plt.subplots()
plt.bar(x, y, 1, align = 'center')

ax.set_xlabel('Focal length (mm)')
ax.set_ylabel('Occurrences')
plt.xticks(x, x);

ax2 = ax.twinx()
ax2.plot(x, y_cu, 1, color='r')
ax2.set_ylabel('Cumulative %', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()

plt.show()

