<?php
header("Content-Type: text/html; charset=UTF-8");

$database='myDict';
$conn=mysql_connect("localhost", "root", "zy19930108");
mysql_query("set character set 'utf8'");
mysql_query("set names set 'utf8'");

$page=0;
if(!isset($_GET['word'])){
    die('[]');
}
if(isset($_GET['page'])){
    $page=intval($_GET['page']);
}

$result=mysql_db_query($database, "SELECT `word`, `desc`, `source` FROM `WordBase` WHERE `word` LIKE '".$_GET['word']."' LIMIT ".($page*10).",".($page*10+10)."; ", $conn);

//print "SELECT * FROM `WordBase` WHERE `word` IS LIKE '".$_GET['word']."' LIMIT ".($page*10).",".($page*10+10)."; ";

$array=array();
while($one=mysql_fetch_array($result,MYSQL_ASSOC)) $array[]=$one;

print json_encode($array);

mysql_close($conn);
?>

