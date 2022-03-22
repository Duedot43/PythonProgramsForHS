<?php
function algor(){
    $selection = $_GET['selection'];
    $a1 = exec("cat " . $selection . "/moves/a1");
    $a2 = exec("cat " . $selection . "/moves/a2");
    $a3 = exec("cat " . $selection . "/moves/a3");
    $b1 = exec("cat " . $selection . "/moves/b1");
    $b2 = exec("cat " . $selection . "/moves/b2");
    $b3 = exec("cat " . $selection . "/moves/b3");
    $c1 = exec("cat " . $selection . "/moves/c1");
    $c2 = exec("cat " . $selection . "/moves/c2");
    $c3 = exec("cat " . $selection . "/moves/c3");
    $win = "_";
    //branch left
    if ($a1 == "O"){
        if ($a2 == "O"){
            if ($a3 == "O"){
                $win = "O";
            }
        }
        if ($b2 == "O"){
            if ($c3 == "O"){
                $win = "O";
            }
        }
        if ($b1 == "O"){
            if ($c1 == "O"){
                $win = "O";
            }
        }
    }
    //branch right
    if ($c1 == "O"){
        if ($c2 == "O"){
            if ($c3 == "O"){
                $win = "O";
            }
        }
        if ($b2 == "O"){
            if ($a3 == "O"){
                $win = "O";
            }
        }
    }
    //middle up down
    if ($b1 == "O"){
        if ($b2 == "O"){
            if ($b3 == "O"){
                $win = "O";
            }
        }
    }
    //middle left right
    if ($a2 == "O"){
        if ($b2 == "O"){
            if ($c2 == "O"){
                $win = "O";
            }
        }
    }
    //bottom left right
    if ($a3 == "O"){
        if ($b3 == "O"){
            if ($c3 == "O"){
                $win = "O";
            }
        }
    }


    //branch left
    if ($a1 == "X"){
        if ($a2 == "X"){
            if ($a3 == "X"){
                $win = "X";
            }
        }
        if ($b2 == "X"){
            if ($c3 == "X"){
                $win = "X";
            }
        }
        if ($b1 == "X"){
            if ($c1 == "X"){
                $win = "X";
            }
        }
    }
    //branch right
    if ($c1 == "X"){
        if ($c2 == "X"){
            if ($c3 == "X"){
                $win = "X";
            }
        }
        if ($b2 == "X"){
            if ($a3 == "X"){
                $win = "X";
            }
        }
    }
    //middle up down
    if ($b1 == "X"){
        if ($b2 == "X"){
            if ($b3 == "X"){
                $win = "X";
            }
        }
    }
    //middle left right
    if ($a2 == "X"){
        if ($b2 == "X"){
            if ($c2 == "X"){
                $win = "X";
            }
        }
    }
    //bottom left right
    if ($a3 == "X"){
        if ($b3 == "X"){
            if ($c3 == "X"){
                $win = "X";
            }
        }
    }
    $wincalc1 = "0";
    $wincalc2 = "0";
    $wincalc3 = "0";
    $wincalc4 = "0";
    $wincalc5 = "0";
    $wincalc6 = "0";
    $wincalc7 = "0";
    $wincalc8 = "0";
    $wincalc9 = "0";

    if ($a1 != "_"){
        $wincalc1 = "3";
    }
    if ($a2 != "_"){
        $wincalc2 = "3";
    }
    if ($a3 != "_"){
        $wincalc3 = "3";
    }
    if ($b1 != "_"){
        $wincalc4 = "3";
    }
    if ($b2 != "_"){
        $wincalc5 = "3";
    }
    if ($b3 != "_"){
        $wincalc6 = "3";
    }
    if ($c1 != "_"){
        $wincalc7 = "3";
    }
    if ($c2 != "_"){
        $wincalc8 = "3";
    }
    if ($c3 != "_"){
        $wincalc9 = "3";
    }
    $tieround = $wincalc1+$wincalc2+$wincalc3+$wincalc4+$wincalc5+$wincalc6+$wincalc7+$wincalc8+$wincalc9;
    $tieround = $tieround;
    if ($tieround == "27"){
        $win = "T";
    }
    if ($tieround != "27"){
        $wins = "N";
    }

    //algorithm

    if ($win == "X"){
        $win = "1";
        $win = $win;
    }
    if ($win == "O"){
        $win = "2";
        $win = $win;
    }
    if ($win == "_"){
        $win = "3";
        $win = $win;
    }
    if ($win == "T"){
        $win = "0";
        $win = $win;
    }
    if ($win == "1"){
        exec("echo 1 >> " . $selection . "/win");
    }
    if ($win == "2"){
        exec("echo 2 >> " . $selection . "/win");
    }
    if ($win == "3"){
        exec("echo 3 >> " . $selection . "/win");
    }
    if ($win == "0"){
        exec("echo 0 >> " . $selection . "/win");
    }
    return $win;
}
function ckwin(){
    $selection = $_GET['selection'];
    $win = exec("cat " . $selection . "/win");
    if ($win == "1"){
        echo("Player X wins!");
        header("Location: clean.php?selection=" . $selection);
        $game = "0";
        exit;
    }
    if ($win == "2"){
        echo("Player O wins!");
        header("Location: clean.php?selection=" . $selection);
        $game = "0";
        exit;
    }
    if ($win == "0"){
        echo("Tie!");
        header("Location: clean.php?selection=" . $selection);
        $game = "0";
        exit;
    }
    if ($win == "3"){
        echo("Continue");
        exec("rm " . $selection . "/trdy" . $_GET['client'] . " && echo 0 >> " . $selection . "/trdy" . $_GET['client']);
    }
}
function ckfrtrn(){
    $selection = $_GET['selection'];
    if ($_GET['client'] == "1"){
        $dot = ".";
        $turn = exec("cat " . $selection . "/trdy2");
            $turn = exec("cat " . $selection . "/trdy2");
            echo("Wating for Player 2");
            exec("sleep 1s");
            if ($turn == "1"){
                return "1";
            } else{
                return "0";
            }
        //echo("Player 2 moved!");
    }else{
        if ($_GET['client'] == "2"){
            $turn = exec("cat " . $selection . "/trdy1");
            
                $turn = exec("cat " . $selection . "/trdy1");
                echo("Wating for Player 1");
                exec("sleep 1s");
                if ($turn == "1"){
                    return "1";
                } else{
                    return "0";
                }
            //echo("Player 1 moved!");
        }
    }
}
function mkboard(){
    $selection = $_GET['selection'];
    $a1 = exec("cat " . $selection . "/moves/a1");
    $a2 = exec("cat " . $selection . "/moves/a2");
    $a3 = exec("cat " . $selection . "/moves/a3");
    $b1 = exec("cat " . $selection . "/moves/b1");
    $b2 = exec("cat " . $selection . "/moves/b2");
    $b3 = exec("cat " . $selection . "/moves/b3");
    $c1 = exec("cat " . $selection . "/moves/c1");
    $c2 = exec("cat " . $selection . "/moves/c2");
    $c3 = exec("cat " . $selection . "/moves/c3");
    $board = ("    A     B     C  \n       |     |     \n1   " . $a1 . "  |  " . $b1 . "  |  " . $c1 . "  \n  _____|_____|_____\n       |     |     \n2   " . $a2 . "  |  " . $b2 . "  |  " . $c2 . "   \n  _____|_____|_____\n       |     |     \n3   " . $a3 . "  |  " . $b3 . "  |  " . $c3 . "  \n       |     |     ");
    return $board;
}
function ckfrusr(){
    $selection = $_GET['selection'];
    if ($_GET['client'] == "1"){
        $dot = ".";
        $turn = "0";
        //$turn = exec("cat " . $selection . "/trdy2");
            //$turn = exec("cat " . $selection . "/trdy2");
            if (file_exists($selection . "/trdy2")){
                echo("Wating for Player 2");
                exec("sleep 1s");   
            } else{
                $turn = "0";
            }
        
        echo("Player 2 moved!");
        return "1";
    }else{
        if ($_GET['client'] == "2"){
            $dot = ".";
            $turn = "0";
                //$turn = exec("cat " . $selection . "/trdy2");
                if (file_exists($selection . "/trdy1")){
                    echo("Wating for Player 1");
                    exec("sleep 1s");   
                } else{
                    $turn = "0";
                }
            
            echo("Player 1 moved!");
            return "1";
        }
    }
}
if (isset($_GET['setup'])) {
    $setup = $_GET['setup'];
    if ($setup == "1"){
        //exec("ls setup triggered");
        exec("mkdir '" . $_GET['selection'] . "/players/" . $_GET['uname'] . "'");
        exec("cd " . $_GET['selection'] . "/moves && echo _ >> a1 && echo _ >> a2 && echo _ >> a3");
        exec("cd " . $_GET['selection'] . "/moves && echo _ >> b1 && echo _ >> b2 && echo _ >> b3");
        exec("cd " . $_GET['selection'] . "/moves && echo _ >> c1 && echo _ >> c2 && echo _ >> c3");
        if ($_GET['client'] == "1"){
            exec("cd " . $_GET['selection'] . " && echo 1 >> trdy1");
        }
        if ($_GET['client'] == "2"){
            exec("cd " . $_GET['selection'] . " && echo 0 >> trdy2");
        }
    } else{
        exit;
    }
} 
if (isset($_GET['uname'])){
    if (isset($_GET['selection'])){
        if (isset($_GET['client'])) {
            $selection = $_GET['selection'];
            exec("sleep 2s");
            $cktrn = ckfrtrn();
            exec($cktrn);
            if ($cktrn != "1"){
                echo("reload");
                header("Location: /rooms/play.php?uname=" . $_GET['uname'] . "&selection=" . $_GET['selection'] . "&client=" . $_GET['client']);
            }
            echo("skip reload");
            algor();
            //ckwin();
            $board = mkboard();
            echo($board);
        } 
    }
}
?>