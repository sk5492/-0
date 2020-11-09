<!DOCTYPE html>
<html>
<head>
	<title>생존일</title>
	<meta charset="utf-8">
</head>
<body>
<?
$year=$_POST["a"];

echo "입력한 날짜는? $year";

$today = getdate();
$mon = $today['mon'];
$mday = $today['mday'];
$yea = $today['year'];
$a=mktime(9,0,1,$mon,$mday,$yea)-mktime(9,0,1,substr($year,5,2),substr($year,8,2),substr($year,0,4));

echo "<br>생존일은 ",$a/86400+1,"일";

$t=time();

echo "<br> 현재 일자는 ", date("Y-M-d H-i-s",$t);

?>
</form>
</body>
</html>