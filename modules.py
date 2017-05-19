import urllib2
import sys

urlToRead = 'http://www.google.com'

crawledWeblinks = {}

while urlToRead != '':
    try:
        urlToRead = input("Please enter the next URL to crawl: ")
        if urlToRead == "":
            print "OK, Exiting loop"
            break
        shortName = input("Please enter a short name for that URL " + urlToRead + " : ")
        webFile = urllib2.urlopen(urlToRead).read()
        crawledWeblinks[shortName] = webFile
    except:
        print "********************************Unexpected Error******************", sys.exc_info()
        stopOrProceed = input("Stop or Proceed? Enter 1 to stop, enter anything else to continue: ")
        if stopOrProceed == 1:
            print "Okay.... Stopping\n"
            break
        else:
            print "Cool! Lets continue\n"
            continue
    finally:
        print "Thank you! The given url has been downloaded."

print crawledWeblinks.keys()
# print crawledWeblinks.values()


# /Users/ajinkyapuar/anaconda/bin/jupyter_mac.command ; exit;
