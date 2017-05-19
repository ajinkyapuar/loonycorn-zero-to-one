number = 10

print "Number in global scope : ", number


def modifyNumber(n):
    print "Argument passed : ", n
    n = n * 10
    print "Argument modified : ", n
    return


modifyNumber(number)

print "Number in global scope : ", number
print "#################################################################"

radius = 5


def areaOfCircle(r):
    return 3.14 * r * r


print "Area of Circle with radius : " + str(radius) + " is : " + str(areaOfCircle(radius))
print "#################################################################"

radiusList = [2, 3, 4, 5]


def areaOfCircles(rList):
    areaList = []
    for r in rList:
        areaList.append(3.14 * r * r)
    return areaList


print "Areas of Circles with radii : " + str(radiusList) + " is : " + str(areaOfCircles(radiusList))
print "#################################################################"


def areaAndCircumference(rList):
    areaList = []
    circumList = []
    result = {"Areas": areaList, "Circumferences": circumList}
    for r in rList:
        areaList.append(3.14 * r * r)
        circumList.append(2 * 3.14 * r)
    return result


results = areaAndCircumference(radiusList)

print "Areas of Circles with radii : " + str(radiusList) + " is : " + str(
    results["Areas"]) + " and their circumferences : " + str(results["Circumferences"])


print "#################################################################"

temp = "ABC123"


def reverseString(s):
    if s is None:
        return s
    if (len(s) <= 1):
        return s
    else:
        return reverseString(s[1:]) + s[0]


print "Reverse of the string : " + temp + " is : " + reverseString(temp)

print "#################################################################"
