import serial, time, sys

#Something has to be connected to port.

ser = serial.Serial('COM3', 9600)

while ser.isOpen() == True:
	print 'Port is open...\n'
	print "Port name:", ser.name
	print "Baudrate:", ser.baudrate
	time.sleep(2)
	
	input = raw_input('Which way should the servo turn: left, center, or right? ')
	
	if (input.lower() == 'l') or (input.lower() == 'left'):
		ser.write('l')
		time.sleep(1)
		
	elif (input.lower() == 'r') or (input.lower() == 'right'):
		ser.write('r')
		time.sleep(1)
		
	elif (input.lower() == 'c') or (input.lower() == 'center'):
		ser.write('c')
		time.sleep(1)
		
	elif (input.lower() == 'exit') or (input.lower() == 'quit'):
		ser.write('c') # center servo before disconnecting serial
		print 'Goodbye!'
		time.sleep(1)
		ser.close()
		
	else:
		print '\nFollow the instructions next time, Goodbye!'
		time.sleep(1)
		sys.exit()
		

ser.close()		
sys.exit()
	

