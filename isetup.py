import os
import subprocess
import pyfiglet

def figlet_yaz(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

def tool():
    figlet_yaz("iSetup")

    try:
        print("Python2 Kuruluyor...")
        os.system("apk add python2")
        print("Python2 Kuruldu!")

        print("Python3 Kuruluyor...")
        os.system("apk add python3")
        print("Python3 Kuruldu!")

        print("PHP Kuruluyor...")
        os.system("apk add php")
        print("PHP Kuruldu!")
    except Exception as e:
        print(f"Hata oluştu: {e}")
        subprocess.run(["python3", "fix.py"])

if __name__ == "__main__":
    tool()
