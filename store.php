<?php
$myfile = fopen("data.txt", "w") or die("Unable to open file!");
$host = $_SERVER["REMOTE_ADDR"];

$txt = "long:" . $_GET['long'] . "\nlat:" . $_GET['lat'] . "\nIP:" . $host . "\nUser agent:" . $_GET["uagent"];
fwrite($myfile, $txt);
fclose($myfile);

?>