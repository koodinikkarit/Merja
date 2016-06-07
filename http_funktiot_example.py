import httplib
import config

def taistorequest(con, cpu):
	conn = httplib.HTTPConnection(config.url["taisto"])
	url = "/api?con=%s&cpu=%s" % (con, cpu)
	conn.request("GET", url)
	response = conn.getresponse()
	conn.close()
        if(response.status == 500):
                raise httplib.HTTPException("request unsucceful, check your parameters")

def taistodefault():
	taistorequest(7,2)



def wakeupkone():
        conn = httplib.HTTPConnection(config.url["wakeup"])
        conn.request("GET", "/api/?machine_id=1")
        conn.close()

