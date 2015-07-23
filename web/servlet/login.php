<?php
function CURDATE(){
    return date("Y-m-d",time());
}

header("Content-Type: text/html; charset=UTF-8");

$database='myDict';
$conn=mysql_connect("localhost", "root", "zy19930108");
mysql_query("set character set 'utf8'");
mysql_query("set names set 'utf8'");

if(isset($_GET["user"])){
    $result=mysql_db_query($database, "SELECT `lastLogin`,`newwordSize` FROM User WHERE `user`='".$_GET["user"]."'; ", $conn);
    $oneuser=mysql_fetch_array($result);
    if($oneuser){
        if(CURDATE()!=$oneuser[0]){
            $listmax=intval($oneuser[1]);
            mysql_db_query($database, "UPDATE User SET `lastLogin`='".CURDATE()."' WHERE `user`='".$_GET["user"]."'; ", $conn);
            $sql="SELECT `word` FROM `WordBase` WHERE source='GRE3000' AND 
                NOT EXISTS (SELECT `word` FROM `RecitingWord` WHERE `RecitingWord`.user='".$_GET["user"]."' and `WordBase`.word=`RecitingWord`.word)
                ORDER BY 'word' LIMIT 0,".$listmax."; ";
//            print $sql;
            $result=mysql_db_query($database, $sql, $conn);
            for($i=0;$i<$listmax;$i+=1){
                $one=mysql_fetch_array($result);
                if($one){
                    mysql_db_query($database, "INSERT INTO `RecitingWord` (`word`,`user`) VALUES ('".$one[0]."','".$_GET["user"]."'); ", $conn);
                }else{
                    break;
                }
            }
        }
        print 'success';
    }else{
        print 'invalid user error';
    }
}else{
    print 'no user error';
}

mysql_close($conn);
?>


