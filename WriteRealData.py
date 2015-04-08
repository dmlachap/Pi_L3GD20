#!/usr/bin/python

# Writes data from a L3GD20 3-axis gyro to a text file on a Raspberry Pi
# Uses the Gyro-L3GD20-Python library by mpolaczyk
# https://github.com/mpolaczyk/Gyro-L3GD20-Python
# Adapted by Dan LaChapelle (dml337@cornell.edu)

# To access output file:
# $ scp <raspberry-pi-username>@<raspberry-pi-ip>:/<path-to-output>/<filename> /<path-to-destination> 

from L3GD20 import L3GD20

import time

# Communication object
s = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)

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
filename = raw_input("Enter the filename of the output file:")
filename += '.txt'


# Calculate angle
dt = 0.02
x = 0
y = 0
z = 0
while 1==1:
	time.sleep(dt)
	dxyz = s.Get_CalOut_Value()
	x += dxyz[0]*dt;
	y += dxyz[1]*dt;
	z += dxyz[2]*dt;
	printstr = "{:7.2f} {:7.2f} {:7.2f}".format(x, y, z)
	print(printstr)
	# File I/O is left in loop. 
	# Alternative implementation: 
	# 	have loop go over a set number of iterations, put file.close() after
	file = open(filename,'w')
	file.write(printstr)
	file.close()

