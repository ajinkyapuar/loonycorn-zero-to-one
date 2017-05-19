#
# ############################################################################################################################################################
# main page url
#     body|
#         |course-sidebar
#             |lecture-sidebar
#                 div|course-section (*)
#                     ul|section-list (*)
#                         li|data-lecture-id
#                           |data-lecture-url
#
# video url page
#     div|course-main-bar
#             div|lecture-attachment
#                 |wistia_responsive_padding
#                     |wistia_responsive_padding
#                         |attachment-wistia-player
#                             |w-chrome
#                                 |wistia_grid_33_wrapper
#                                     |wistia_grid_33_main
#                                         |wistia_grid_33_center
#                                             |wistia_video_wrapper_55
#                                                 |wistia_32_vulcan
#                                                     video|
#                                                         source|
# ############################################################################################################################################################

import urllib2
from bs4 import BeautifulSoup

hdr = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*q=0.8',
    'Accept-Charset': 'ISO-8859-1;utf-8,q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}


def get_all_video_links(url, hdr):
    # print url
    webRequest = urllib2.Request(url, headers=hdr)
    # print webRequest
    try:
        page = urllib2.urlopen(webRequest).read()
        # print  page
        print "********** Page Downloaded! **********"
        soup = BeautifulSoup(page)
        # print soup.find_all('a', {"class": "item"}, href=True)
        for link in soup.find_all('a', {"class": "item"}, href=True):
            print "**********"
            print "https://stackskills.com" + link['href']
            download_video_page("https://stackskills.com" + link['href'], hdr)
            # print link.text
            print "**********"
    except urllib2.HTTPError, e:
        print e.fp.read()
        print "***** Could not download the file! *****"


def download_video_page(url, hdr):
    # print url
    webRequest = urllib2.Request(url, headers=hdr)
    # print webRequest
    try:
        # TODO: Login and then download files
        page = urllib2.urlopen(webRequest).read()
        print page
    except urllib2.HTTPError, e:
        print e.fp.read()
        print "***** Could not download the file! *****"


url = "https://stackskills.com/courses/enrolled/70316"

get_all_video_links(url, hdr)


# vidURL = "https://stackskills.com/courses/from-0-1-machine-learning1/lectures/1028998"
#
# download_video_page(vidURL, hdr)
# FB9
