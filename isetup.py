import os

def show_disk_usage():
    print("Disk Kullanımı Gösteriliyor...")
    os.system("df -h")
    print("Disk Kullanımı Gösterildi!")

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
        print("8. Disk Kullanımını Göster")
        print("9. Çıkış")

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
            show_disk_usage()
        elif choice == '9':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")