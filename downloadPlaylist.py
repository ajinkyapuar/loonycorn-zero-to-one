import urllib2
import time
from bs4 import BeautifulSoup
from pytube import YouTube

hdr = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*q=0.8',
    'Accept-Charset': 'ISO-8859-1;utf-8,q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

url = "https://www.youtube.com/playlist?list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal"


def get_all_video_links(url, hdr):
    webRequest = urllib2.Request(url, headers=hdr)
    # print webRequest
    try:
        page = urllib2.urlopen(webRequest).read()
        # print page
        print "********** Page Downloaded! **********"
        soup = BeautifulSoup(page)
        # print  soup
        for link in soup.find_all('a', {"class": "pl-video-title-link"}, href=True):
            print link.text
            vidURL = link['href'].split('&')
            # print vidURL[0]
            print "https://www.youtube.com" + vidURL[0]
            # download_video("https://www.youtube.com" + vidURL[0], link.text)
            # time.sleep(120)
            print "********** Video Downloaded! **********"
    except urllib2.HTTPError, e:
        print e.fp.read()
        print "***** Could not download the file! *****"


# def download_video(url, name):
#     # print name
#     # print url
#     yt = YouTube(url)
#     print yt.filename
#     video = yt.get('mp4', '720p')
#     # print video
#     video.download('/googleML/')

get_all_video_links(url, hdr)


# pytube -f "Classifying Handwritten Digits with TF.Learn - Machine Learning Recipes" -p ~/Downloads/ https://www.youtube.com/watch?v=Gj0iyo265bc


