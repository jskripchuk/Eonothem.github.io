<?php
$servername = "localhost";
$username = "root";
$password = "";
$cookie_name = "smallstone";
$databasename = "smallstone";

function allow(){
	//echo "Login sucessful!";
	echo true;
}

function deny(){
	//echo "Login denied!";
	echo false;
}

function sqlVerify($n, $p, $conn){
	$sql = "SELECT * FROM Users WHERE username = '$n'";
	$stmt = $conn->prepare($sql); 
    $stmt->execute();

    $result = $stmt->setFetchMode(PDO::FETCH_ASSOC); 
	$resultRow = $stmt->fetch();
	
	//if(password_verify($p, $resultRow['password']))
	if(password_verify($p, $resultRow['hashedPassword'])){
		//echo "Welcome user: ".$resultRow['username'].'</br>';
		return true;
	}else{
		return false;
	}
}

try {
    $conn = new PDO("mysql:host=$servername;dbname=$databasename", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	
	if(isset($_COOKIE[$cookie_name])){
		//echo "Cookie found. Verifying... </br>";
		$cookieData = json_decode($_COOKIE[$cookie_name], true);
		if(sqlVerify($cookieData['username'], $cookieData['password'], $conn)){
			allow();
		}else{
			deny();
		}
	}else{
		echo "Cookie not found. <br>";
		
		if(isset($_POST["username"]) && isset($_POST["password"])){
			$user = $_POST["username"];
			$pass = $_POST["password"];
			
			if(sqlVerify($user, $pass, $conn)){
				//echo "We're in.</br>";
				//echo "Setting cookie...</br>";
				$cookie_value = ["username" => $user, "password" => $pass];
				setcookie($cookie_name, json_encode($cookie_value),  time()+3600);
				echo "Cookie set! </br>";
				allow();
			}else{
				deny();
				echo "nah.";
			}
			
			
		}else{
			//echo "You didn't log in!";
		}
	}
}catch(PDOException $e){
    //echo "Connection failed: " . $e->getMessage();
    deny();
}
?>
