<?php

$command = escapeshellcmd('sudo python /home/pi/led-gui/LED/walk.py');
$output = shell_exec($command);
echo $output;

header('location: index.html');

?>
