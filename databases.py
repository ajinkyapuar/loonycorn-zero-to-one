import urllib2, cookielib
import zipfile, os
import time
import sqlite3
import csv
import xlsxwriter
from datetime import datetime


########################################################################################################################

# STEP 1:

########################################################################################################################

# sqlConnection = sqlite3.connect("example.db")
#
# sqlCursor = sqlConnection.cursor()
#
# sqlCursor.execute(
#     "CREATE TABLE prices (SYMBOL text, SERIES text, OPEN real, HIGH real, LOW real, CLOSE real, LAST real, PREVCLOSE real, TOTTRDQTY real, TOTTRDVAL real, TIMESTAMP date, TOTALTRADES real, ISIN text, PRIMARY KEY (SYMBOL, SERIES, TIMESTAMP))")
#
# sqlConnection.commit()
#
# print sqlCursor.execute("SELECT * FROM prices")


########################################################################################################################

# STEP 2:

########################################################################################################################
# def download(localZipFilePath, urlOfFileName):
#     # Request headers to the website to make it look like a human is downloading the content and not a bot
#     hdr = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
#         'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*q=0.8',
#         'Accept-Charset': 'ISO-8859-1;utf-8,q=0.7,*;q=0.3',
#         'Accept-Encoding': 'none',
#         'Accept-Language': 'en-US,en;q=0.8',
#         'Connection': 'keep-alive'
#     }
#
#     webRequest = urllib2.Request(urlOfFileName, headers=hdr)
#
#     try:
#         page = urllib2.urlopen(webRequest)
#         content = page.read()
#         output = open(localFilePath, 'wb')
#         output.write(bytearray(content))
#         output.close()
#         print "File Downloaded!"
#     except urllib2.HTTPError, e:
#         print "*** Error! ***"
#         print e.fp.read()
#         print "***** Could not download the file! *****"

#
# def unzip(localZipFilePath, localExtractFilePath):
#     if os.path.exists(localZipFilePath):
#         print "Zip file exists!"
#         listOfFiles = []
#         fh = open(localZipFilePath, 'rb')
#         zipFileHandler = zipfile.ZipFile(fh)
#         for fileName in zipFileHandler.namelist():
#             # print fileName
#             zipFileHandler.extract(fileName, localExtractFilePath)
#             listOfFiles.append(localExtractFilePath + fileName)
#         print "Files Extracted: " + str(len(listOfFiles))
#         print listOfFiles
#         fh.close()


########################################################################################################################

# Test

# zipFilePath = "/Users/ajinkyapuar/Documents/Python/stackSkills/loonycorn-zero-to-one/Data/NSE_2006-16/cm02JAN2006bhav.csv.zip"
#  fileExtractPath = "/Users/ajinkyapuar/Documents/Python/stackSkills/loonycorn-zero-to-one/Data/"


# unzip(zipFilePath, fileExtractPath)

########################################################################################################################

# def downloadAndUnzipForPeriod(listOfMonths, listOfYears):
#     for year in listOfYears:
#         for month in listOfMonths:
#             for dayOfMonth in range(31):
#                 date = dayOfMonth + 1
#                 dateStr = str(date)
#                 if date < 10:
#                     dateStr = "0" + dateStr
#                 print dateStr, "-", month, "-", year
#                 fileName = "cm" + str(dateStr) + str(month) + str(year) + "bhav.csv.zip"
#                 urlOfFileName = "https://www.nseindia.com/content/historical/EQUITIES" + year + "/" + month + "/" + fileName
#                 localZipFilePath = "/Users/ajinkyapuar/Documents/Python/stackSkills/loonycorn-zero-to-one/Data/" + fileName
#                 download(localZipFilePath, urlOfFileName)
#                 unzip(localZipFilePath, localExtractFilePath)
#                 # sleep for 10 seconds
#                 time.sleep(10)
#     print "All files downloaded and Extracted!"


# localExtractFilePath = "/Users/ajinkyapuar/Documents/Python/stackSkills/loonycorn-zero-to-one/Data/"
# listOfMonths = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
# listOfYears = ['2014']

# downloadAndUnzipForPeriod(listOfMonths, listOfYears)


########################################################################################################################

# MODIFICATION

def extractAllFiles(localZipFilePath, localExtractFilePath, listOfMonths, listOfYears):
    print "*********************** Starting extraction process! ***********************"
    for year in listOfYears:
        for month in listOfMonths:
            for dayOfMonth in range(31):
                date = dayOfMonth + 1
                dateStr = str(date)
                if date < 10:
                    dateStr = "0" + dateStr
                # fileName = "cm" + str(dateStr) + str(month) + str(year) + "bhav.csv.zip"
                fileName = "fo" + str(dateStr) + str(month) + str(
                    year) + "bhav.csv.zip"  # this and the above line required. execute both
                filePath = localZipFilePath + fileName
                # print filePath
                if os.path.exists(filePath):
                    print "***************************"
                    print "Zip file exists! " + fileName
                    fh = open(filePath, 'rb')
                    zipFileHandler = zipfile.ZipFile(fh)
                    for file in zipFileHandler.namelist():
                        # print fileName
                        zipFileHandler.extract(file, localExtractFilePath)
                    fh.close()
                    print "Zip file extracted"
                    print "***************************"
                    time.sleep(0.25)
                    # else:
                    # print "***************************"
                    # print "Zip file not found!"
                    # print "***************************"

    print "*********************** All files have been extracted! ***********************"


localZipFilePath = "/Users/ajinkyapuar/Documents/Python/stackSkills/loonycorn-zero-to-one/Data/NSE_2006-16/"
localExtractFilePath = "/Users/ajinkyapuar/Documents/Python/stackSkills/loonycorn-zero-to-one/Data/NSE_2006-2016_Extracted/"
listOfMonths = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
listOfYears = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']

# extractAllFiles(localZipFilePath, localExtractFilePath, listOfMonths, listOfYears)

########################################################################################################################


# STEP 3: Parse each file and insert each row into database

########################################################################################################################


sqlConnection = sqlite3.connect("example.db")


def insertRows(fileName, sqlConnection):
    sqlCursor = sqlConnection.cursor()
    lineNum = 0
    with open(fileName, 'rb') as csvfile:
        lineReader = csv.reader(csvfile, delimiter=",", quotechar="\"")
        for row in lineReader:
            lineNum = lineNum + 1
            if lineNum == 1:
                print "Skipping Header row"
                # print row
                continue
            date_object = datetime.strptime(row[10], '%d-%b-%Y')
            # print  len(row)
            # print "Row Length : " + str(len(row))
            # print row
            if len(row) == 14:
                # print "Row Length : " + str(len(row))
                # print row
                oneTuple = [row[0], row[1], float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]),
                            float(row[7]), float(row[8]), float(row[9]), date_object, float(row[11]), row[12]]
                sqlCursor.execute("INSERT INTO prices VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", oneTuple)
            elif len(row) == 12:
                # print "Row Length : " + str(len(row))
                oneTuple = [row[0], row[1], float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]),
                            float(row[7]), float(row[8]), float(row[9]), date_object, "NULL", "NULL"]
                sqlCursor.execute("INSERT INTO prices VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", oneTuple)
            else:
                print "****************************************************"
                print "Data changed"
                print "****************************************************"
        sqlConnection.commit()
        print "*********************** Done iterating over file content. File Closed! ***********************"


localExtractFilePath = "/Users/ajinkyapuar/Documents/Python/stackSkills/loonycorn-zero-to-one/Data/NSE_2006-2016_Extracted/"

count = 1
# for file in os.listdir(localExtractFilePath):
#     print count
#     print file
#     if file.endswith(".csv"):
#         insertRows(localExtractFilePath + '/' + file, sqlConnection)
#     count += 1


########################################################################################################################


# STEP 4: Run a test query and check if data is inserted in the DB


########################################################################################################################

t1 = 'BHARATFORG'
series = 'EQ'

sqlCursor = sqlConnection.cursor()

cursor = sqlCursor.execute(
    "SELECT symbol, max(close), min(close), max(timestamp), min(timestamp), count(timestamp) FROM prices WHERE symbol = ? and series = ? GROUP BY symbol ORDER BY timestamp",
    (t1, series))


# for row in cursor:
#     print row



########################################################################################################################


# STEP 5: Input a stock ticker and output an excel spreadsheet with stock movement for an entire year with a line graph


########################################################################################################################


def createExcelWithDailyPriceMoves(ticker, series, sqlConnection):
    # print ticker
    sqlCursor = sqlConnection.cursor()
    cursor = sqlCursor.execute(
        "SELECT symbol, timestamp, close FROM prices WHERE symbol = ? and series = ? ORDER BY timestamp",
        (ticker, series))
    excelFileName = "/Users/ajinkyapuar/Documents/Python/stackSkills/loonycorn-zero-to-one/Data/" + ticker + ".xlsx"
    # print excelFileName
    workbook = xlsxwriter.Workbook(excelFileName)
    worksheet = workbook.add_worksheet("Summary")
    worksheet.write_row("A1", ["Top Traded Stocks"])
    worksheet.write_row("A2", ["Stock", "Date", "Closing"])
    lineNum = 3
    for row in cursor:
        print row
        worksheet.write_row("A" + str(lineNum), list(row))
        lineNum = lineNum + 1
    chart1 = workbook.add_chart({'type': 'line'})
    chart1.add_series({
        'categories': '=Summary!$B$3:$B$' + str(lineNum),
        'values': '=Summary!$C$3:$C$' + str(lineNum)
    })
    chart1.set_title({'name': ticker})
    chart1.set_x_axis({'name': 'Date'})
    chart1.set_y_axis({'name': 'Closing Price'})
    worksheet.insert_chart('F2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()


# ticker = input("Input stock ticker : ")
# series = input("Input series : ")

# createExcelWithDailyPriceMoves(ticker, series, sqlConnection)


########################################################################################################################


# STEP 6: Drop table


########################################################################################################################

sqlCursor = sqlConnection.cursor()

cursor.execute("DROP TABLE prices")

sqlConnection.commit()

sqlConnection.close()
