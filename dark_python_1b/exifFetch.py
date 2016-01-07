# Excerpted from Violent Python, by TJ O'Connor
# Revised to account for python 3 and changes to several libraries.

from urllib.request import urlopen
# import urllib2
import optparse

# from urlparse import urlsplit
from urllib.parse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS
import re
tags = None
def findImages(url):
    print('Searching for images on ', url)
    urlContent = urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    # imgTags = soup.findAll('img')
    scriptTags = soup.findAll('script')
    # return imgTags
    return scriptTags

def downloadImage(imgTag):
    try:
        imgSrc = 'https://' + imgTag
        # imgSrc = imgTag['src']
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
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
            print(info)
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print(imgFileName, 'contains GPS Metadata')
    except:
        pass

def main():
    parser = optparse.OptionParser('usage%prog -u <target url>')
    parser.add_option('-u', dest='url', type='string', help='specify url address')
    (options, args) = parser.parse_args()
    url = options.url
    prog = re.compile(".*\.staticflickr.com.*24034886721_.*_o.jpg")
    if url == None:
        print(parser.usage)
        exit(0)
    else:
        # imgTags = findImages(url)
        scriptTags = findImages(url)
        # print(scriptTags)  
        imgURLS = []
        for scriptTag in scriptTags:
            matches = re.findall(prog, scriptTag.get_text())
            if matches:
                imgURLS.extend(matches)
        for imgTag in imgURLS:
            print(imgTag)
            imgFileName = downloadImage(imgTag)
            testForExif(imgFileName)
        # return imgTags
if __name__ == '__main__':
    main()

