import urllib2
import os
import zipfile
import csv
import xlsxwriter
import sys

########################################################################################################################

# STEP 1:

########################################################################################################################

url = "https://www.nseindia.com/content/historical/EQUITIES/2016/DEC/cm06DEC2016bhav.csv.zip"

localFilePath = "/Users/ajinkyapuar/Documents/Python/stackSkills/loonycorn-zero-to-one/Data/cm06DEC2016bhav.csv.zip"

# Request headers to the website to make it look like a human is downloading the content and not a bot
hdr = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*q=0.8',
    'Accept-Charset': 'ISO-8859-1;utf-8,q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}
#
webRequest = urllib2.Request(url, headers=hdr)

try:
    page = urllib2.urlopen(webRequest)
    content = page.read()
    output = open(localFilePath, 'wb')
    output.write(bytearray(content))
    output.close()
    print "File Downloaded!"
except urllib2.HTTPError, e:
    print e.fp.read()
    print "***** Could not download the file! *****"

########################################################################################################################

# STEP 2:

########################################################################################################################

localExtractFilePath = "/Users/ajinkyapuar/Documents/Python/stackSkills/loonycorn-zero-to-one/Data/"

if os.path.exists(localFilePath):
    print "Zip file exists!"
    listOfFiles = []
    fh = open(localFilePath, 'rb')
    zipFileHandler = zipfile.ZipFile(fh)
    for fileName in zipFileHandler.namelist():
        # print fileName
        zipFileHandler.extract(fileName, localExtractFilePath)
        listOfFiles.append(localExtractFilePath + fileName)
    print "Files Extracted: " + str(len(listOfFiles))
    print listOfFiles
    fh.close()

########################################################################################################################

# STEP 3:

########################################################################################################################

oneFileName = listOfFiles[0]
lineNum = 0
listOfLists = []

with open(oneFileName, 'rb') as csvFile:
    lineReader = csv.reader(csvFile, delimiter=",", quotechar="\"")
    for row in lineReader:
        lineNum = lineNum + 1
        if lineNum == 1:
            print "Skipping Header row"
            # print row
            continue
        symbol = row[0]
        close = row[5]
        prevClose = row[7]
        tradedQty = row[9]
        pctChange = float(close) / float(prevClose) - 1
        oneResultRow = [symbol, pctChange, float(tradedQty)]
        # print oneResultRow
        listOfLists.append(oneResultRow)
        # print symbol, "{:,1f}".format(float(tradedQty) / 1e6) + "M INR", "{:, 1f}".format(pctChange * 100) + "%"
    print "CSV file parsed"
    # print listOfLists

########################################################################################################################

# STEP 4:

########################################################################################################################

listOfListsSortedByPct = sorted(listOfLists, key=lambda x: x[1], reverse=True)
print "\n********** Sorting List by Percentage **********\n"
print listOfListsSortedByPct

listOfListsSortedByQty = sorted(listOfLists, key=lambda x: x[2], reverse=True)
print "\n********** Sorting List by Quantity **********\n"
print listOfListsSortedByQty

########################################################################################################################

# STEP 5:

########################################################################################################################

excelFileName = "/Users/ajinkyapuar/Documents/Python/stackSkills/loonycorn-zero-to-one/Data/cm06DEC2016bhav.xlsx"

workbook = xlsxwriter.Workbook(excelFileName)

worksheet = workbook.add_worksheet("Summary")

worksheet.write_row("A1", ["Top Traded Stocks"])

worksheet.write_row("A2", ["Stock", "Percentage Change", "Value Traded (INR)"])

for rowNum in range(5):
    worksheet.write_row("A" + str(rowNum + 3), listOfLists[rowNum])

print "Created Workbook with Summary Worksheet of Top 5 Shares of the Day"
workbook.close()

########################################################################################################################

# STEP 6:

########################################################################################################################
