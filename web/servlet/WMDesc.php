<?php
header("Content-Type: text/html; charset=UTF-8");

$database='myDict';
$intervalSecs=60;
$conn=mysql_connect("localhost", "root", "zy19930108");
mysql_query("set character set 'utf8'");
mysql_query("set names set 'utf8'");

if(!isset($_GET["word"])){
    die('no word error');
}

$result=mysql_db_query($database, "SELECT `word`,`desc`,`MWXml` FROM `WordBase` WHERE word='".$_GET["word"]."'; ", $conn);
$one=mysql_fetch_array($result);
$word=$one[0];
$desc=$one[1];
$MWXml=base64_decode($one[2]);

if($MWXml==''){
    $key="73453d0d-497a-45a9-b625-e309e7db05bf";
    $uri="http://www.dictionaryapi.com/api/v1/references/collegiate/xml/".urlencode($word)."?key=".urlencode($key);
	$MWXml=file_get_contents($uri);
	mysql_db_query($database, "UPDATE `WordBase` SET `MWXml`='".base64_encode($MWXml)."' WHERE `word`='".$word."'; ", $conn);
}

print $MWXml;

mysql_close($conn);
?>

