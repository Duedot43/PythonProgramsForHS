<?php
if (isset($_GET['selection'])){
    $win = exec("cat " . $_GET['selection'] . "/win");
    exec("rm -rf " . $_GET['selection'] . "/moves && cd " . $_GET['selection'] . " && rm trdy1 && rm win && rm trdy2");
    if ($win == "1"){
        echo("Player X wins!");
        //header("Location: clean.php?selection=" . $selection);
        $game = "0";
        echo("User info deleted");
        exit;
    }
    if ($win == "2"){
        echo("Player O wins!");
        //header("Location: clean.php?selection=" . $selection);
        $game = "0";
        echo("User info deleted");
        exit;
    }
    if ($win == "0"){
        echo("Tie!");
        //header("Location: clean.php?selection=" . $selection);
        $game = "0";
        echo("User info deleted");
        exit;
    }

}