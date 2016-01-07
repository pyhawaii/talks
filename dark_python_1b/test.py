import maxminddb
from PIL import Image
from PIL.ExifTags import TAGS
from pprint import pprint 
import sys

imageName = sys.argv[1]

reader = maxminddb.open_database('GeoLite2-City.mmdb')

data = reader.get('1.1.1.1')
# print(data)

reader.close()

exifData = {}
imgFile = Image.open(imageName)
# imgFile = Image.open('image_test2.jpg')
info = imgFile._getexif()
if info:
    for (tag, value) in info.items():
        decoded = TAGS.get(tag, tag)
        exifData[decoded] = value
    exifGPS = exifData.get('GPSInfo', None)
    if exifGPS:
        print(imgFile, ' contains GPS MetaData', exifGPS)

pprint(exifData)        
