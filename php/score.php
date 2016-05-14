<?php
	$servername = "localhost";
	$username = "root";
	$password = "";
	$cookie_name = "smallstone";
	$databasename = "smallstone";
	
	try {
		$conn = new PDO("mysql:host=$servername;dbname=$databasename", $username, $password);
		$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		//echo "Connected!";
		//$sql = "SELECT * FROM Users";
		//$stmt = $conn->prepare($sql); 
		//$stmt->execute();
		
		//$result = $stmt->setFetchMode(PDO::FETCH_ASSOC); 
		//$resultArr = $stmt->fetch();
		//echo $resultArr['username'];
		//$resultArr = $stmt->fetch();
		//echo $resultArr['username'];
		$totalCorrect = $_POST["totalCorrect"];
		$totalPoints = $_POST["totalPoints"];
		$topic = $_POST["topic"];
		echo $totalCorrect;
		
		$sql = "INSERT INTO QUESTION(pointsCorrect, pointsTotal, topic, testtakerID)
				VALUES
				('$totalCorrect', '$totalPoints', '$topic', null)
				";
		$conn->exec($sql);
	}catch(PDOException $e){
		echo "Connection failed: " . $e->getMessage();

	}
?>