<?php

if(isset($_GET['trdy'])) {
    if(isset($_GET['client'])) {
        exec("echo -n '" . $_GET['win'] . "' > 'info/pinfo" . $_GET['client'] . "/win'");
    }
}

if(isset($_GET['ded'])) {
    if(isset($_GET['client'])) {
        exec("echo -n '" . $_GET['ded'] . "' > 'info/pinfo" . $_GET['client'] . "/ded'");
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

if(isset($_GET['shpded'])) {
    if(isset($_GET['client'])) {
        if(isset($_GET['shpnm'])) {
            if(isset($_GET['shprnm'])) {
                exec("echo -n '" . $_GET['shpded'] . "' > 'info/pinfo" . $_GET['client'] . "/ships/" . $_GET['shprnm'] . "/" . $_GET['shpnm'] . "'");
            }
        }
    }
}

if(isset($_GET['in'])) {
    exec("echo -n '" . $_GET['in'] . "' > 'connect/in'");
}

if(isset($_GET['out'])) {
    exec("echo -n '" . $_GET['in'] . "' > 'connect/out'");
}

if(isset($_GET['turn'])) {
    exec("echo -n '" . $_GET['turn'] . "' > info/turn");
}

if(isset($_GET['all'])) {
    exec("echo -n '" . $_GET['all'] . "' > connect/all");
}
?>