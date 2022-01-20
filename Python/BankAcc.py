from datetime import date
from ast import While
import os.path
import subprocess
today = date.today()
date = today.strftime("%m/%d/%Y %H:%M:%S");
uname = input("Please enter your username\n");
passwd = input("Please enter your password\n");
ckuname = os.path.exists("share/bnkusrs/" + uname);
ckpasswd = os.path.exists("share/bnkpsd/" + passwd);
if ckuname == True:
    if ckpasswd == True:
        login = 1
        while login == 1:
            fname1 = open('share/bnkusrs/' + uname + '/fname', 'rt');
            mname1 = open('share/bnkusrs/' + uname + '/mname', 'rt');
            lname1 = open('share/bnkusrs/' + uname + '/lname', 'rt');
            cbalnc1 = open('share/bnkusrs/' + uname + '/cbalnc', 'rt');
            fname = fname1.read()
            mname = mname1.read()
            lname = lname1.read()
            cbalnc = cbalnc1.read()
            #fname = str(fname);
            #mname = str(mname);
            #lname = str(lname);
            #cbalnc = int(cbalnc);
            print(f"Welcome, {fname}! What can i do for you today?");
            print("(1) Check your balance.");
            print("(2) Deposit funds.");
            print("(3) Withdraw funds.");
            print("(4) Logout");
            print("(5) Delete account");
            selection = input(":");
            #print(selection);
            if selection == "1":
                print("Yout balance is: " + cbalnc);
            if selection == "2":
                print("How much would you like to deposit?\n");
                inbal = int(input("?"));
                cbalnctmp = int(cbalnc);
                inbalofic = cbalnctmp + inbal
                inbalofic = str(inbalofic);
                os.system("cd share/bnkusrs/" + uname  + " && rm cbalnc && sleep 2 && echo '" + inbalofic + "' > cbalnc");
            if selection == "3":
                print("How much would you like to withdraw?\n");
                inbal = int(input("?"));
                cbalnctmp = int(cbalnc);
                inbalofic = cbalnctmp - inbal
                inbalofic = str(inbalofic);
                os.system("cd share/bnkusrs/" + uname  + " && rm cbalnc && echo '" + inbalofic + "' > cbalnc");
            if selection == "4":
                exit();
            if selection == "5":
                os.system("rm -rf share/bnkusrs/" + uname + " && rm share/bnkpsd/" + passwd);
                exit();
    if ckpasswd == False:
        print("Wrong password");
        os.system("python Python/BankAcc.py");
        exit();
if ckuname == False:
    if ckpasswd == True:
        print("Wrong username");
        os.system("python Python/BankAcc.py");
        exit();
    if ckpasswd == False:
        print("Welcome! please create an account.");
        fname = input("Whats your legal first name?\n");
        mname = input("Whats your legal middle name?\n");
        lname = input("What is your legal last name?\n");
        reguname = input("What is the desired username?\n");
        cbalnc = input("Please input current balance\n");
        regpasswd = input("What is your desired password?\n");
        regpasswdconf = input("Please confirm your password\n");
        if regpasswdconf != regpasswd:
            print("Passwords are diffrent please try again");
            os.system("python Python/BankAcc.py");
            exit();
        if regpasswdconf == regpasswd:
            print("Success! regestering your account please wait...\n");
            os.system("cd share/ && mkdir 'bnkusrs/" + reguname + "' && echo '" + fname + "' > 'bnkusrs/" + reguname + "/fname' && echo '" + mname + "' > 'bnkusrs/" + reguname + "'/mname && echo '" + lname + "' > 'bnkusrs/" + reguname + "/lname' && echo '" + cbalnc + "' > 'bnkusrs/" + reguname + "/cbalnc' && echo '" + date + "' > 'bnkusrs/" + reguname + "/log' && echo 'Account created' >> 'bnkusrs/" + reguname + "/log'");
            print("Info done regestering password...");
            os.system("cd share/bnkpsd/ && echo '" + regpasswd + "' > '" + regpasswd + "'");

            

