<?php
header("Content-Type: text/html; charset=UTF-8");

$database='myDict';
$conn=mysql_connect("localhost", "root", "zy19930108");
mysql_query("set character set 'utf8'");
mysql_query("set names set 'utf8'");

print '<table border=0>';
print '<tr><td>用户</td><td>&nbsp;&nbsp;</td><td>不认识</td><td>见过</td><td>熟悉</td><td>掌握</td></tr>';

$result=mysql_db_query($database, "SELECT `user` FROM `User`; ", $conn);
while($one=mysql_fetch_array($result)){
    $result1=mysql_db_query($database, "SELECT `status`,count(*) FROM `RecitingWord` WHERE `user`='".$one[0]."' group by `status`; ");
    $array=array(0,0,0,0); //-1,0 1 2,3,4,5 6-
    while($x=mysql_fetch_array($result1)){
        $x0=intval($x[0]);
        if($x0==-1 || $x0==0) $array[0]+=intval($x[1]);
        if($x0==1) $array[1]+=intval($x[1]);
        if($x0==2 || $x0==3 || $x0==4 || $x0==5) $array[2]+=intval($x[1]);
        if($x0>=6) $array[3]+=intval($x[1]);
    }
    print "<tr><td>".$one[0]."</td><td>&nbsp;&nbsp;</td>";
    print "<td>".$array[0]."</td>";
    print "<td>".$array[1]."</td>";
    print "<td>".$array[2]."</td>";
    print "<td>".$array[3]."</td>";
    print "</tr>";
}

print '</table>';

?>


