<?
require 'setup.php';
require 'connect.php';

//Require the connect.php file where you connect to a mysql database using PDO and store the connection in a $con variable

/*
for example:

<?
$dbserver = 'localhost';
$dbusername = 'user';
$dbpassword = 'pass';
$dbdatabase = 'wakeup';

try{
	$con = new PDO('mysql:host='.$dbserver.';dbname='.$dbdatabase, $dbusername, $dbpassword);
	$con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
	$con->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_OBJ);
	$con->setAttribute(PDO::MYSQL_ATTR_INIT_COMMAND, 'SET NAMES UTF8');
} catch (PDOException $e) {
	throw new PDOException("Error : " . $e->getMessage());
}

*/

class wakeupException extends Exception {}


try{
	wakeupMachine($con, $argv[1], $argv[2]);//$_GET['machine_id'], $_GET['token']);
} catch(wakeupException $we){
	errorResponse($we->getMessage());
}


function wakeupMachine($con, $id, $token){
	if(!isset($id)){
		throw new wakeupException('Machine id not set');
	}

	try{
		//get info about the machine from database
		$stmt = $con->prepare("SELECT koneet.wakeuplevel, koneet.name, koneet.ip, koneet.mac FROM koneet WHERE koneet.id = :id");
		$stmt->bindParam(':id', $id, PDO::PARAM_INT);
		$stmt->execute();
		$res = $stmt->fetchAll();
	} catch(Exception $e){
		errorResponse('Error dealing with the database');
		return;
	}

	if(count($res) != 1){
		throw new wakeupException('Machine not found');
	} else {
		$row = $res[0];
		//if authentication for wakeup needed
		if($row->wakeuplevel > 0){
			if(!isset($token)){
				throw new wakeupException("Token required to wake up this machine");
			}

			try{
				$stmt2 = $con->prepare("SELECT level FROM tokens WHERE token = :token");
				$stmt2->bindParam(':token', $token, PDO::PARAM_STR);
				$stmt2->execute();
				$res2 = $stmt2->fetchAll();

			} catch(Exception $e){
				errorResponse('Error dealing with the database');
				return;
			}

			if(count($res2) <= 0){
				throw new wakeupException('Invalid token');
			}

			$level = $res2[0]->level;
			if($level >= $row->wakeuplevel){
				wakeHerUp($row->ip, $row->mac);
				successResponse("Wol package sent succefully to the machine: ".$row->name);
			}

		//if authentication not needed
		} else {
			wakeHerUp($row->ip, $row->mac);
			successResponse("Wol package sent succefully to the machine: ".$row->name);
		}
	}
}

function wakeHerUp($ip, $mac){
	/* determineProxy is a function in setup.php
	which gives the ip of a gateway to the subnett
	that the machine is on. The wol package is then
	sent to that ip.
	*/
	$wip = determineProxy($ip);
	// use the command line program wakeonlan to send the wol package
	$res = shell_exec("/usr/bin/wakeonlan -i $wip $mac");
}

function errorResponse($msg){
	echo '<h1 style="color:red;">Diminishing failure</h1>';
	echo $msg;
}

function successResponse($msg){
	echo '<h1 style="color:green;">Great success!</h1>';
	echo $msg;
}
