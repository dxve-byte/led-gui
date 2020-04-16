<?php

$command = escapeshellcmd('sudo python /home/pi/led-gui/LED/onecolor.py');
$output = shell_exec($command);
echo $output;

header('location: index.html');

?>
