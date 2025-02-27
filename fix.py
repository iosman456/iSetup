import os

def fix_tool():
    print("İOS Update Oluyor...")
    os.system("apk update")
    print("İOS Update Oldu!")
    print("İOS Upgrade Oluyor...")
    os.system("apk upgrade")
    print("İOS Upgrade Oldu!")
    print("Python2 Yeniden Kuruluyor...")
    os.system("apk add python2 --no-cache")
    print("Python2 Yeniden Kuruldu!")

    print("Python3 Yeniden Kuruluyor...")
    os.system("apk add python3 --no-cache")
    print("Python3 Yeniden Kuruldu!")

    print("PHP Yeniden Kuruluyor...")
    os.system("apk add php --no-cache")
    print("PHP Yeniden Kuruldu!")

if __name__ == "__main__":
    fix_tool()
