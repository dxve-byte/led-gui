<?php

$command = escapeshellcmd('sudo killall python');
$output = shell_exec($command);
echo $output;

header('location: index.html');

?>
