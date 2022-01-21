<?php
if ($_GET['client'] == "1") {
    if ($_GET['move'] == "1") {
        exec("echo 1 > info/p1mv");
    }
}
if ($_GET['client'] == "1") {
    if ($_GET['move'] == "2") {
        exec("echo 2 > info/p1mv");
    }
}
if ($_GET['client'] == "1") {
    if ($_GET['move'] == "3") {
        exec("echo 3 > info/p1mv");
    }
}



if ($_GET['client'] == "2") {
    if ($_GET['move'] == "1") {
        exec("echo 1 > info/p2mv");
    }
}
if ($_GET['client'] == "2") {
    if ($_GET['move'] == "2") {
        exec("echo 2 > info/p2mv");
    }
}
if ($_GET['client'] == "2") {
    if ($_GET['move'] == "3") {
        exec("echo 3 > info/p2mv");
    }
}

if ($_GET['turn'] == "1") {
    exec("echo 1 > info/turn");
}
if ($_GET['turn'] == "2") {
    exec("echo 2 > info/turn");
}

if ($_GET['trdy1'] == "0") {
    exec("echo 0 > info/trdy1");
}
if ($_GET['trdy1'] == "1") {
    exec("echo 1 > info/trdy1");
}
if ($_GET['trdy2'] == "0") {
    exec("echo 0 > info/trdy2");
}
if ($_GET['trdy2'] == "1") {
    exec("echo 1 > info/trdy2");
}

if ($_GET['win'] == "0") {
    exec("echo 0 > info/win");
}
if ($_GET['win'] == "1") {
    exec("echo 1 > info/win");
}
if ($_GET['win'] == "2") {
    exec("echo 2 > info/win");
}
?>