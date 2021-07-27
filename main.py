import gspread
from time import time, sleep
from Sensors.ds18b20 import DS18B20


def writeSheet(arg1, arg2, arg3):
    gc = gspread.service_account(
        filename='/home/pi/solarMonitor/solarmonitor-320601-8f2bdc50d596.json')
    sh = gc.open("solarMonitorSheet").sheet1
    row = [arg1, arg2, arg3]
    sh.append_row(row, value_input_option='USER_ENTERED',insert_data_option='INSERT_ROWS')



def readOneWire():
    """ test temperature sensors
    x = DS18B20()
    count=x.device_count()
    i = 0
    while i < count:
            print(x.tempC(i))
            i += 1
    """
    temp1 = '1'
    temp2 = '2'
    return (temp1, temp2)


def main():
    time_stamp = time()
    tReadings = readOneWire()
    """ test temperature sensors
	x = DS18B20()
	count=x.device_count()
	i = 0
	while i < count:
		print(x.tempC(i))
		i += 1
	test"""
    writeSheet(time_stamp, tReadings[0], tReadings[1])


if __name__ == "__main__":
    main()
