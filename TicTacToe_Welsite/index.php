<?php
if(isset($_POST['uname'])) {
    $uname = $_POST['uname'];
    header("Location: /rooms.php?uname=" . $uname);
}
?>
<title>Register Your User</title>
<head>
    <link href="style.css" rel="stylesheet" type="text/css" />
</head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Register</title>
<tr>
    <form method="post">
        <td>
            <table width="100%" border="0" cellpadding="3" cellspacing="1">
                <tr>
                    <td colspan="3"><strong>Please select a username...
                            <hr />
                        </strong></td>
                </tr>
                <tr>
                    <td class="text" width="78">Username
                        <td width="6">:</td>
                        <td width="294"><input class="box" autocomplete="off" name="uname" type="text" id="uname" placeholder="Duedot43" required></td>
                    </td>
                </tr>
</tr>
<tr>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td><input class="reg" type="submit" name="Submit" value="Submit"></td>
</tr>
</table>
</td>
</form>
</tr>
</table>