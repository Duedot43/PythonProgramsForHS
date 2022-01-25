<?php

if(isset($_GET['trdy'])) {
    if(isset($_GET['client'])) {
        exec("echo -n '" . $_GET['trdy'] . "' > 'info/pinfo" . $_GET['client'] . "/trdy'");
    }
}
if(isset($_GET['val'])) {
    if(isset($_GET['client'])) {
        if(isset($_GET['pos'])) {
            if(isset($_GET['board'])) {
                exec("echo -n '" . $_GET['val'] . "' > 'info/pinfo" . $_GET['client'] . "/board" . $_GET['board'] . "/" . $_GET['pos'] . "'");
            }
        }
    }
}

if(isset($_GET['turn'])) {
    exec("echo -n '" . $_GET['turn'] . "' > info/turn");
}

if(isset($_GET['all'])) {
    exec("echo -n '" . $_GET['all'] . "' > connect/all");
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
if ($_GET['win'] == "3") {
    exec("echo 3 > info/win");
}
?>