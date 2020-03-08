import serial
import time
import csv

# set up the serial line
ser = serial.Serial('COM3', 115200, timeout = 5)
time.sleep(2)
# Read and record the data
data = []                       # empty list to store the data
start_time = time.time()
for i in range(500):
    b = ser.readline()
    # print(b.decode())      # read a byte string
    string_n = b.decode()
    print(string_n)  # decode byte string into Unicode
    # string = string_n.rstrip() # remove \n and \r
    # flt = float(string)        # convert string to float
    # print(flt)
    data.append(string_n)           # add to the end of data list
    if 'Send any character'.encode() in b:
        jo = 's'
        newjo = jo.encode()
        ser.write(newjo)
    time.sleep(0.001)            # wait (sleep) 0.1 seconds

ser.close()
elapsed_time = time.time() - start_time
print(elapsed_time)
# show the data
print("\nAppended Data\n\n\n\n\n\n\n")
# print(data)
acc = []
xAcc = []
yAcc = []
for line in data:
    # line = line.rstrip()
    acc.append(line.split('\t'))
print(acc[:20])
for i in range(20, len(acc)-40):
    xAcc.append(int((acc[i][1]))/16834)
    yAcc.append(int((acc[i][2]))/16834)
print(xAcc)
print(yAcc)
with open("accelerations.csv",'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["xAcc", "yAcc"])
    for i in range(len(xAcc)):
        writer.writerow([xAcc[i],yAcc[i]])
    writer.writerow([str(elapsed_time), '0'])
