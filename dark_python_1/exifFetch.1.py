# Excerpted from Violent Python, by TJ O'Connor
# Revised to account for python 3 and changes to several libraries.

import optparse

from urllib.request import urlopen
from urllib.parse import urlsplit
from bs4 import BeautifulSoup

from os.path import basename

from PIL import Image
from PIL.ExifTags import TAGS

import re
from pprint import pprint

fout = open('kml_demo.kml', 'w')

def findImages(url):
    '''Opens the web page given by url and parses the contents
    to locate and return all the image tags.
    '''

    print('Searching for images on ', url)
    urlContent = urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags


def downloadImage(imgTag):
    '''Parses the image tag to identify the image url and the image name.
    Opens/downloads the image, writes the image to disk and returns the image
    filename.
    '''

    try:
        imgSrc = imgTag['src']
        imgContent = urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        print('Downloading image...', imgFileName)
        imgFile.close()
        return imgFileName
    except:
        return ''


def testForExif(imgFileName):
    '''Tests the image for EXIF data. If EXIF data is present, extracts the data
    related to the GPS location.
    ''' 
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()

        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']

            if exifGPS:
                print(imgFileName, 'contains GPS Metadata')
                pprint(exifGPS)
                return gpsExtractor(exifGPS)
    except:
        pass


def gpsExtractor(exifGPS):
    '''Parses the exif GPS data for the latitude and longitude. Calibrates based
    on the 'N'/'S' references and 'E'/'W' references and converts degrees, minutes, 
    seconds to decimal degrees.

    THe exifGPS data comes in the following format... 
    
    { 0: b'\x02\x02\x00\x00',
      1: 'N',
      2: ((21, 1), (35, 1), (427253, 10000)),       # DMS units/divisors
      3: 'W',
      4: ((158, 1), (5, 1), (599670, 10000)),       # DMS units/divisors
      5: 0,
      6: (21000, 1000),
      7: ((0, 1), (25, 1), (3, 1)),
     29: '2015:12:28'}
    '''
    
    def converter(decDMS):
        '''Converts degrees/minutes/seconds to decimal degrees'''

        degs = decDMS[0][0]
        mins = decDMS[1][0]
        secs = decDMS[2][0]/decDMS[2][1]
        decDeg = degs + (mins + secs/60)/60
        return decDeg 

    N_S = exifGPS[1]
    if N_S == 'N':
        lat_DecDeg = round(converter(exifGPS[2]), 6)
    else:
        lat_DecDeg = round(converter(exifGPS[2]), 6) * -1

    E_W = exifGPS[3]
    if E_W == 'E':
        lon_DecDeg = round(converter(exifGPS[4]), 6) 
    else:
        lon_DecDeg = round(converter(exifGPS[4]), 6) * -1 

    print(N_S, lat_DecDeg, E_W, lon_DecDeg)
    return (lon_DecDeg, lat_DecDeg)


def kml(name, lon, lat):
    '''Generates a kml document from the filename, the latitude and the longitude.'''

    kml_header = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>'''
    kml_tail = '''</Document>
</kml> '''
    kml_coord = '''<Placemark>
<name>{}</name>
<Point>
<coordinates>{},{}</coordinates>
</Point>
</Placemark>
'''

    return kml_header + kml_coord.format(name, lon, lat) + kml_tail


def main():
    '''Finds images, downloads them and test for and extracts EXIF data.
    '''

    parser = optparse.OptionParser('usage%prog -u <target url>')
    parser.add_option('-u', dest='url', type='string', help='specify url address')
    (options, args) = parser.parse_args()
    url = options.url

    if url == None:
        print(parser.usage)
        exit(0)
    else:
        imgTags = findImages(url)
        for imgTag in imgTags:
            imgFileName = downloadImage(imgTag)
            gpsData = testForExif(imgFileName)
            if gpsData:
                lonDD, latDD = gpsData
                output = kml(imgFileName, lonDD, latDD) 

    fout.write(output)
    fout.close()


if __name__ == '__main__':
    main()

