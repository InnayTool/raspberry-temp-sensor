
#!/bin/python3

from datetime import datetime

inp = open("/sys/bus/w1/devices/10-0008032e4133/hwmon/hwmon0/temp1_input", "r")
out = open("/home/pi/temp.txt","a")


line = inp.read()

out.write(str(datetime.now()) + ": " + line[:-4] + "," + line[-4:-1] + " °C\n")
out.close()
print("Hallo Welt")
