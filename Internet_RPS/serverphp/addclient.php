<?php
if ($_GET['client'] == "1") {
    if ($_GET['connect'] == "1") {
        exec("echo 1 > connect/p1");
    }
}
if ($_GET['client'] == "1") {
    if ($_GET['connect'] == "0") {
        exec("echo 0 > connect/p1");
    }
}
if ($_GET['client'] == "2") {
    if ($_GET['connect'] == "1") {
        exec("echo 1 > connect/p2");
    }
}
if ($_GET['client'] == "2") {
    if ($_GET['connect'] == "0") {
        exec("echo 0 > connect/p2");
    }
}
?>