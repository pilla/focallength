
# FocalLength

This is a small script I wrote to get statistics about which focal lengths I used for taking pictures. It gets the data from EXIF tags. 

As it is, it should also work for other EXIF tags as long as the tag content is a numeric value (that can be converted to integer), mostly because it is using a numeric sort for the x axis.

## Running

The script takes three parameters. The first is the file termination (JPG, NEF, ...) that will be used, the second is the directory (. for current directory). The third parameter is optional and is an alternative EXIF tag.

## Output

The script outputs a graph with the number of occurrences of each focal length found plus their cumulative distribution.

