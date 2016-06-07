import telnetlib
import config

tncon = telnetlib.Telnet(config.url["tykki"])


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
