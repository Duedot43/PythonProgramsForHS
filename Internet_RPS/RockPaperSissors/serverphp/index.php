<?php
if ($_GET['clean'] == "1") {
    exec("rm connect/* && rm info/*");
}
if ($_GET['clean'] == "2") {
    exec("rm info/*");
}
echo("no");
?>