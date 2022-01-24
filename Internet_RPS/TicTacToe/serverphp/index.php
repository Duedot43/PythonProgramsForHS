<?php
if ($_GET['clean'] == "1") {
    exec("rm connect/* && rm info/*");
    exec("echo p > connect/.placeholder");
    exec("echo p > info/.placeholder");
}
if ($_GET['clean'] == "2") {
    exec("rm info/*");
    exec("echo p > info/.placeholder");
}
echo("no");
?>