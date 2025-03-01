#!/usr/bin/env python3

import os

def update_system():
    print("İOS Update Oluyor...")
    os.system("apk update")
    print("Oldu!")

def upgrade_system():
    print("İOS Upgrade Oluyor...")
    os.system("apk upgrade")
    print("Oldu!")

def install_python2():
    print("Python2 Kuruluyor...")
    os.system("apk add python2")
    print("Python2 Kuruldu!")

def install_python3():
    print("Python3 Kuruluyor...")
    os.system("apk add python3")
    print("Python3 Kuruldu!")

def install_php():
    print("PHP Kuruluyor...")
    os.system("apk add php")
    print("PHP Kuruldu!")

def install_neofetch():
    print("neofetch Kuruluyor...")
    os.system("apk add neofetch")
    print("neofetch Kuruldu!")
    os.system("neofetch")

def install_tmux_htop():
    print("TMUX ve HTOP Kuruluyor...")
    os.system("apk add tmux htop")
    print("TMUX ve HTOP Kuruldu!")

def install_nano():
    print("nano Kuruluyor...")
    os.system("apk add nano")
    print("nano Kuruldu!")

def install_vim():
    print("Vim Kuruluyor...")
    os.system("apk add vim")
    print("Vim Kuruldu!")

def install_all():
    print("Bütün Paketler Toplanıyor...")
    update_system()
    upgrade_system()
    install_python2()
    install_python3()
    install_php()
    install_neofetch()
    install_tmux_htop()
    install_nano()
    install_vim()
    print("Tüm Paketler Kuruldu, Görüşürüz!")

def main_menu():
    while True:
        print("\nAna Menü")
        print("1. Sistem Güncelle")
        print("2. Sistem Yükselt")
        print("3. Python2 Kur")
        print("4. Python3 Kur")
        print("5. PHP Kur")
        print("6. neofetch Kur")
        print("7. TMUX ve HTOP Kur")
        print("8. nano Kur")
        print("9. Vim Kur")
        print("10. Hepsini Aynı Anda Kur")
        print("11. Çıkış")

        choice = input("Bir seçenek giriniz: ")

        if choice == '1':
            update_system()
        elif choice == '2':
            upgrade_system()
        elif choice == '3':
            install_python2()
        elif choice == '4':
            install_python3()
        elif choice == '5':
            install_php()
        elif choice == '6':
            install_neofetch()
        elif choice == '7':
            install_tmux_htop()
        elif choice == '8':
            install_nano()
        elif choice == '9':
            install_vim()
        elif choice == '10':
            install_all()
        elif choice == '11':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main_menu()