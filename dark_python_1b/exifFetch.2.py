# Excerpted from Violent Python, by TJ O'Connor
# Revised to account for python 3 and changes to several libraries.

from urllib.request import urlopen
import optparse

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
    imgTags = soup.findAll(attrs={"href": "/wiki/"})    # <a class="download_link" href="
    # scriptTags = soup.findAll('script')
    print('imgTags', imgTags)
    return imgTags
    # return scriptTags

def downloadImage(imgTag):
    try:
        # imgSrc = 'https://' + imgTag
        imgSrc = imgTag['href']
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
            # print(info)
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print(imgFileName, exifGPS, 'contains GPS Metadata')
    except:
        pass

def main():
    parser = optparse.OptionParser('usage%prog -u <target url>')
    parser.add_option('-u', dest='url', type='string', help='specify url address')
    (options, args) = parser.parse_args()
    url = options.url
    # prog = re.compile("img.src='//(\w\w\.staticflickr.com.*\.jpg)")
    if url == None:
        print(parser.usage)
        exit(0)
    else:
        imgTags = findImages(url)
        # scriptTags = findImages(url)
        # print(scriptTags)  
        # imgURLS = []
        # for scriptTag in scriptTags:
        for imgTag in imgTags:
            imgFileName = downloadImage(imgTag)
            testForExif(imgFileName)
if __name__ == '__main__':
    main()

