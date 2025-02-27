import os
def figlet_yaz(text):
    os.system(f'figlet {text}')

figlet_yaz("iSetup")

print("Python2 Kuruluyor...")
os.system("apk add python2")
print("Python2 Kuruldu!")

print("Python3 Kuruluyor...")
os.system("apk add python3")
print("Python3 Kuruldu!")

print("PHP Kuruluyor...")
os.system("apk add php")
print("PHP Kuruldu!")
