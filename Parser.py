import csv
import math

# THIS IS FOR CSV FILES ONLY

def parseValues(filename):
    #gets a file name in string and output a nest list of acceleration values with the last value being the time duration
    accel_list = []
    with open(filename, 'r', newline = '') as csvfile:
        reader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
        
        for i in reader:
            mystr = i[0]
            b = mystr.split(',')
            accel_list.append(b)
            
        for j in range(1, len(accel_list)):
            accel = math.sqrt((float(accel_list[j][0]))**2 + (float(accel_list[j][1]))**2)
            accel_list[j] = accel
        accel_list.pop(0)
    return accel_list

    """
    legacy code
    for i in range(len(time_list)):
        entryLst = []
        entryLst.append(accel_list[i])
        entryLst.append(time_list[i])
        finalList.append(entryLst)
    return finalList
    # print(accel_list)
    # print(time_list)
    
        dict = {}
        for key in time_list:
            for value in accel_list:
                dict[key] = value
                accel_list.remove(value)
                break
            return dict
    """
        
def getJerk(acLst):
    # get the nested acceleration list and output a list of jerk values
    deltaT = acLst[len(acLst)-1]/(len(acLst)-1)
    jerkLst = []
    for i in range(len(acLst) - 1):
        nextVal = acLst[i]
        currVal = acLst[i - 1]
        jerkVal = nextVal - currVal/deltaT
        jerkLst.append(jerkVal)
    return jerkLst
    
def getExceedFreq(acLst, maxJerk = 0.9 , maxAcc = 2):
    jerkList = getJerk(acLst)
    exceedCount = 0
    timeDif = acLst[len(acLst) - 1]
    for i in jerkList:
        if abs(i) > maxJerk:
            exceedCount +=1
    for j in range(len(acLst)-1):
        if abs(acLst[j]) > maxAcc:
            exceedCount +=1
    
    return exceedCount/timeDif

if __name__ == "__main__":
    acLst1 = parseValues("accelerations1.csv")
    acLst2 = parseValues("accelerations2.csv")
    print(getExceedFreq(acLst1))
    print(getExceedFreq(acLst2))
