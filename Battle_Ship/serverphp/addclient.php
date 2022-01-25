<?php
if(isset($_GET['client'])) {
    if(isset($_GET['connect'])) {
        exec("echo -n '" . $_GET['connect'] . "' > 'connect/p" . $_GET['client'] . "'");
    }
}
if(isset($_GET['ammountofclients'])) {
    exec("echo -n '" . $_GET['ammountofclients'] . "' > 'connect/clients'");
}
if(isset($_GET['clientdatafoldernumber'])) {
    exec("mkdir info/pinfo" . $_GET['clientdatafoldernumber']);
    exec("mkdir info/pinfo" . $_GET['clientdatafoldernumber'] . "/boardtop");
    exec("mkdir info/pinfo" . $_GET['clientdatafoldernumber'] . "/boardbot");
    exec("mkdir info/pinfo" . $_GET['clientdatafoldernumber'] . "/ships");
    exec("mkdir info/pinfo" . $_GET['clientdatafoldernumber'] . "/ships/destroy");
    exec("mkdir info/pinfo" . $_GET['clientdatafoldernumber'] . "/ships/sub");
    exec("mkdir info/pinfo" . $_GET['clientdatafoldernumber'] . "/ships/cruse");
    exec("mkdir info/pinfo" . $_GET['clientdatafoldernumber'] . "/ships/battle");
    exec("mkdir info/pinfo" . $_GET['clientdatafoldernumber'] . "/ships/care");


}
?>
