<?php
$servername = "localhost";
$username = "root";
$password = "";
$databasename = "smallstone";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$databasename", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	
	if(isset($_POST["username"]) && isset($_POST["password"])){
		$user = $_POST["username"];
		$pass = $_POST["password"];
		if(!isNameTaken($user,$conn)){
			$hashPass = password_hash($pass, PASSWORD_DEFAULT);
			$sql = "INSERT INTO Users(username, hashedPassword)
				VALUES
				('$user', '$hashPass')
				";
			$conn->exec($sql);
			echo "You're now part of the database!!<br>";
		}
	}
}catch(PDOException $e){
    echo "Connection failed: " . $e->getMessage();
}

function isNameTaken($n, $conn){
	$sql = "SELECT * FROM USERS WHERE username = '$n'";
	$stmt = $conn->prepare($sql); 
    $stmt->execute();

    $result = $stmt->setFetchMode(PDO::FETCH_ASSOC); 
	$resultRow = $stmt->fetch();
	
	if($resultRow['username'] == ""){
		echo "Name is not taken!";
		return false;
	}else{
		echo "Name already taken!";
		return true;
	}
}
?>
