import os

print("İOS Update Oluyor...")
os.system("apk update")
print("Oldu!")

print("İOS Upgrade Oluyor...")
os.system("apk upgrade")
print("Oldu!")

print("Bütün Paketler Toplanıyor...")
print("Toplandı!")
print("Bütün Paketler Başlatılıyor...")
os.system("python backups.py")
print("Başlatıldı!")
print("GitHub: https://github.com/iosman456/iSetup.git

print("Python2 Kuruluyor...")
os.system("apk add python2")
print("Python2 Kuruldu!")

print("Python3 Kuruluyor...")
os.system("apk add python3")
print("Python3 Kuruldu!")

print("PHP Kuruluyor...")
os.system("apk add php")
print("PHP Kuruldu!")

print("neofetch Hazılanıyor...")
os.system("apk add neofetch")
print("neofetch Hazırlandı! Hatta Görünümüde Böyle.")
os.system("neofetch")

print("TMUX HTOP Kuruluyor...")
os.system("apk add tmux htop")

print("Tüm Paketler bitti, Görüsürüz")