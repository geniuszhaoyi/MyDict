<?php

header("Content-Type: text/html; charset=UTF-8");

$database='myDict';
$conn=mysql_connect("localhost", "root", "zy19930108");
mysql_query("set character set 'utf8'");
mysql_query("set names set 'utf8'");

if(!isset($_GET['user'])){
    die('failed');
}

mysql_db_query($database, "INSERT INTO (`user`) VALUES ('"+$_GET['user']+"'); ", $conn);

print 'success';

mysql_close($conn);
?>


