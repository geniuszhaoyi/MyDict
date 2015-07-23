<?php
header("Content-Type: text/html; charset=UTF-8");

$database='myDict';
$intervalSecs=60;
$conn=mysql_connect("localhost", "root", "zy19930108");
mysql_query("set character set 'utf8'");
mysql_query("set names set 'utf8'");

if(!isset($_GET["user"])){
    die('no user error');
}

if(isset($_GET["user"]) && isset($_GET["word"]) && isset($_GET["status"])){
    $result=mysql_db_query($database, "lock table RecitingWord write;", $conn);
    $result=mysql_db_query($database, "SELECT `word`,`status` FROM `RecitingWord` WHERE user='".$_GET["user"]."' AND word='".$_GET["word"]."'; ", $conn);
    $status=intval(mysql_fetch_array($result)['status']);
    
    if($_GET["status"]=="0") $status=$status+1;
    if($_GET["status"]=="1") if($status<5) $status=$status+1; else $status=$status;
    if($_GET["status"]=="2") $status=$status;
    if($_GET["status"]=="3") $status=$status-1;
    
    $minstatus=-1;
    if($status<$minstatus) $status=$minstatus;
    
    $result=mysql_db_query($database, "UPDATE `RecitingWord` SET `status`='".$status."',`lastRecite`='".date('Y-m-d H:i:s',time())."' WHERE user='".$_GET["user"]."' AND word='".$_GET["word"]."'; ", $conn);
    $result=mysql_db_query($database, "unlock tables;", $conn);
}


$result=mysql_db_query($database, "SELECT `word`,`status`,`lastRecite` FROM `RecitingWord` WHERE user='".$_GET["user"]."'; ", $conn);

$array=array();
while($one=mysql_fetch_array($result)){
    if(intval($one['status'])>=10) continue;
    if(intval(strtotime($one['lastRecite']))+$intervalSecs*pow(intval($one['status']),4)>=time()) continue;
    $array[]=$one;
}

if(count($array)==0){
    print '{"word":"__EMPTY__"}';
}else{
    $i=rand(0,count($array)-1);
    $result=mysql_db_query($database, "SELECT `word`,`desc`,`MWXml` FROM `WordBase` WHERE word='".$array[$i][0]."'; ", $conn);
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
    
    $i1=stripos($MWXml,'<wav>');
    $i2=stripos($MWXml,'</wav>');
    $MWWav='http://media.merriam-webster.com/soundc11/'.substr($MWXml,$i1+5,1).'/'.substr($MWXml,$i1+5,$i2-$i1-5);
    $MWDesc='';
    while($i1=stripos($MWXml,'<dt>')){
        //$i1=stripos($MWXml,'<dt>');
        $i2=stripos($MWXml,'</dt>');
        $MWDesc=$MWDesc.substr($MWXml,$i1+4,$i2-$i1-4).'<br>';
        $MWXml=substr($MWXml,$i2+4+1);
    }

    print '{"word":"'.$word.'","desc":"'.$desc.'","MWDesc":"'.$MWDesc.'","MWWav":"'.$MWWav.'"}';
}

mysql_close($conn);
?>



