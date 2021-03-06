#!/usr/bin/env python
# Writes data from a L3GD20 3-axis gyro to a text file on a Raspberry Pi
# Uses the Gyro-L3GD20-Python library by mpolaczyk
# https://github.com/mpolaczyk/Gyro-L3GD20-Python
# Adapted by Dan LaChapelle (dml337@cornell.edu)

# To access output file:
# $ scp <raspberry-pi-username>@<raspberry-pi-ip>:/<path-to-output>/<filename> /<path-to-destination> 

from L3GD20 import L3GD20

import time

tstart = time.time()

# Communication object
s = L3GD20(busId = 1, slaveAddr = 0x6a, ifLog = False, ifWriteBlock=False)

# Preconfiguration
s.Set_PowerMode("Normal")
s.Set_FullScale_Value("500dps")
s.Set_AxisX_Enabled(True)
s.Set_AxisY_Enabled(True)
s.Set_AxisZ_Enabled(True)

# Print current configuration
s.Init()
s.Calibrate()

# Print to file
# filename = raw_input("Enter the filename of the output file: ")
#filename += '.txt'

#filename = 'Tests.txt'
#file = open(filename,'a')
#datestr = 'Test ' + time.strftime("%c")
datestr = 'Test_' + time.strftime("%d_%b_%Y_%H:%M:%S", time.localtime())
filename = datestr + '.txt'

#dt = 0.02

dt = 0.01

# Get angular rate data
while 1==1:
	time.sleep(dt)
	dxyz = s.Get_CalOut_Value()
	tclock = time.clock() - tstart
	ttime = time.time() - tstart
	x = dxyz[0]
	y = dxyz[1]
	z = dxyz[2]
	printstr = "{: f} {: f} {: f} {: f} {: f}".format(tclock, ttime, x, y, z)
	print(printstr)
	# File I/O is done in loop. 
	file = open(filename,'a')
	printstr += '\n'
	file.write(printstr)
	file.close()


