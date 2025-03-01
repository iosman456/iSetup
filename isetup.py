#!/usr/bin/env python3

import os

# ANSI color codes for rainbow effect
colors = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Purple
    "\033[0m"    # Reset
]

def color_print(text):
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(f"{color}{char}", end="")
    print(colors[-1])  # Reset at the end

def update_system():
    color_print("İOS Update Oluyor...")
    os.system("apk update")
    color_print("Oldu!")

def upgrade_system():
    color_print("İOS Upgrade Oluyor...")
    os.system("apk upgrade")
    color_print("Oldu!")

def install_python2():
    color_print("Python2 Kuruluyor...")
    os.system("apk add python2")
    color_print("Python2 Kuruldu!")

def install_python3():
    color_print("Python3 Kuruluyor...")
    os.system("apk add python3")
    color_print("Python3 Kuruldu!")

def install_php():
    color_print("PHP Kuruluyor...")
    os.system("apk add php")
    color_print("PHP Kuruldu!")

def install_neofetch():
    color_print("neofetch Kuruluyor...")
    os.system("apk add neofetch")
    color_print("neofetch Kuruldu!")
    os.system("neofetch")

def install_tmux_htop():
    color_print("TMUX ve HTOP Kuruluyor...")
    os.system("apk add tmux htop")
    color_print("TMUX ve HTOP Kuruldu!")

def install_nano():
    color_print("nano Kuruluyor...")
    os.system("apk add nano")
    color_print("nano Kuruldu!")

def install_vim():
    color_print("Vim Kuruluyor...")
    os.system("apk add vim")
    color_print("Vim Kuruldu!")

def install_all():
    color_print("Bütün Paketler Toplanıyor...")
    update_system()
    upgrade_system()
    install_python2()
    install_python3()
    install_php()
    install_neofetch()
    install_tmux_htop()
    install_nano()
    install_vim()
    color_print("Tüm Paketler Kuruldu, Görüşürüz!")

def main_menu():
    while True:
        color_print("\nAna Menü")
        color_print("1. Sistem Güncelle")
        color_print("2. Sistem Yükselt")
        color_print("3. Python2 Kur")
        color_print("4. Python3 Kur")
        color_print("5. PHP Kur")
        color_print("6. neofetch Kur")
        color_print("7. TMUX ve HTOP Kur")
        color_print("8. nano Kur")
        color_print("9. Vim Kur")
        color_print("10. Hepsini Aynı Anda Kur")
        color_print("11. Çıkış")

        color_printchoice = input("Bir seçenek giriniz: ")

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
            color_print("Çıkış yapılıyor...")
            break
        else:
            color_print("Geçersiz seçenek, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main_menu()