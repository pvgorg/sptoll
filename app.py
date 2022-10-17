import os,sys

def logo () :
    print("""
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
    print("  TOOLS TERMUX");
    print("+----------------+");
    print("[1] Install Tombol Termux");
    print("[2] Keluar Menu");
    nmr = input("Pilih Sesuai Nomor :");

    # Setting Bagian Tools 
    if nmr =="1":
        os.system("pkg update && pkg upgrade");
        os.system("pkg install python2 -y");
        os.system("pkg install git -y");
        os.system("git clone https://github.com/kumpulanremaja/termuxtbb");

    elif nmr =="2":
        sys.exit();

menu();