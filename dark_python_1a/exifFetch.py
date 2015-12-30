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

def findImages(url):
    print('Searching for images on ', url)
    urlContent = urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    # imgTags = soup.findAll('img')
    scriptTags = soup.findAll('script')
    # return imgTags
    return scriptTags

def downloadImage(imgTag):
    #soup.findAll('img')[0].get('src')
    try:
        
        imgSrc = imgTag['src']
        imgContent = urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        print('Downloading image...', imgFileName)
        imgFile.close()
        irint('Downloading image...', imgFileName)
        return imgFileName
    except:
        return ''

def testForExif(imgFileName):
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
    except:
        pass

def main():
    parser = optparse.OptionParser('usage%prog -u <target url>')
    parser.add_option('-u', dest='url', type='string', help='specify url address')
    (options, args) = parser.parse_args()
    url = options.url
    if url == None:
        print(parser.usage)
        exit(0)
    else:
        # imgTags = findImages(url)
        scriptTags = findImages(url)
        print(scriptTags)  
        for imgTag in imgTags:
            imgFileName = downloadImage(imgTag)
            testForExif(imgFileName)
        return imgTags
if __name__ == '__main__':
    a = main()

