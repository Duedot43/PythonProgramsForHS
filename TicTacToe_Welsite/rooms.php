<?php
$uname = $_GET['uname'];
$get_rooms = exec("ls rooms | grep 1");
if($get_rooms != "1"){
    exec("mkdir rooms/1 && mkdir rooms/2 && mkdir rooms/3 && mkdir rooms/4 && mkdir rooms/5");
    exec("mkdir rooms/1/players && mkdir rooms/2/players && mkdir rooms/3/players && mkdir rooms/4/players && mkdir rooms/5/players");
    exec("mkdir rooms/1/moves && mkdir rooms/2/moves && mkdir rooms/3/moves && mkdir rooms/4/moves && mkdir rooms/5/moves");
}
if(isset($_GET['selection'])) {
    if(isset($_GET['uname'])) {
        $uname = $_GET['uname'];
        $selection = $_GET['selection'];
        $ckfrusr = exec("ls rooms/" . $selection . "/players/");
        if ($ckfrusr == ""){
            $client = "1";
        }
        if ($ckfrusr != ""){
            $client = "2";
        }
        header("Location: /rooms/play.php?uname=" . $uname . "&selection=" . $selection . "&setup=1&client=" . $client);
        exit;

    }
}
?>
<head>
    <link href="style.css" rel="stylesheet" type="text/css" />
</head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Select your room</title>
<tr>
<td>
<table width="100%" border="0" cellpadding="3" cellspacing="1">
<tr>
<td colspan="3"><strong>Please select a player room.<br></strong></td>
</tr>
<tr>

<td width="294"><input class="reg" type="button" value='Room 1' onclick="location='rooms.php?uname=<?php echo $uname;?>&selection=1'" /></td>

<td width="294"><input class="reg" type="button" value='Room 2' onclick="location='rooms.php?uname=<?php echo $uname;?>&selection=2'" /></td>

<td width="294"><input class="reg" type="button" value='Room 3' onclick="location='rooms.php?uname=<?php echo $uname;?>&selection=3'" /></td>

<td width="294"><input class="reg" type="button" value='Room 4' onclick="location='rooms.php?uname=<?php echo $uname;?>&selection=4'" /></td>

<td width="294"><input class="reg" type="button" value='Room 5' onclick="location='rooms.php?uname=<?php echo $uname;?>&selection=5'" /></td>

</tr>
<tr>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</table>
</td>
</tr>
</table>