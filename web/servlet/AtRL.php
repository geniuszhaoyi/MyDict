<?php
header("Content-Type: text/html; charset=UTF-8");

$database='myDict';
$intervalSecs=60;
$conn=mysql_connect("localhost", "root", "zy19930108");
mysql_query("set character set 'utf8'");
mysql_query("set names set 'utf8'");

if(!isset($_GET['user']) || !isset($_GET['user'])){
    die('args error');
}

mysql_db_query($database, "INSERT INTO `RecitingWord` (`word`,`user`) VALUES ('".$_GET['word']."','".$_GET["user"]."'); ", $conn);

mysql_close($conn);
?>

