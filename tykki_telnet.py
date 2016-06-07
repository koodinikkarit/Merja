import telnetlib

tncon = telnetlib.Telnet("192.168.180.10")


def powerup():
	global tncon
	tncon.write("(PWR1)")

def freeze(freeze):
	global tncon
	if freeze:
		tncon.write("(FRZ1)")
	else:
		tncon.write("(FRZ0)")

def blank(blank):
	global tncon
	if blank:
		tncon.write("(BLK1)")
	else:
		tncon.write("(BLK0)")
