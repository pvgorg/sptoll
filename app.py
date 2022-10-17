import requests,os
import sys
from traceback import print_tb

def logo () :
    print("""""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝""");


def menu() :
    os.system('clear');
    logo();
    print("+----------------+");
    print("  Mᴇɴᴜ Pɪʟɪʜᴀɴ");
    print("+----------------+");
    print("[1] Menu Tools Termux");
    print("[2] Keluar Menu");
    nmr = input("Pilih Sesuai Nomor :");

    if nmr =="1":
        print("  [X]==============================================[X]");
        print("                         TOOLS TERMUX");
        print("[1] Install Tombol Termux");  
        print("[2] KELUAR DARI SEMUA MENU !!!");
        print("  [X]==============================================[X]");
        gme = input("Pilih Sesuai Nomor :");

        # Setting Bagian Tools 
        if gme =="1":
            os.system("pkg update && pkg upgrade");
            os.system("pkg install python2 -y");
            os.system("pkg install git -y");
            os.system("git clone https://github.com/kumpulanremaja/termuxtbb");

        elif gme =="2":
            sys.exit();
    

    # Bagian Menu Pilihan Nomor 2
    elif nmr =="2":
        sys.exit();

menu();