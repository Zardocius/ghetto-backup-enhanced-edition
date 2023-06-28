import os
import shutil


targetDir = "c:/users/iirov/desktop/vienti"

backUpLista = [
    "C:/Users/iirov/Desktop/testikansio",
    "C:/users/iirov/PC",
    "C:/Users/iirov/3D objects",
    "C:/users/iirov/Saved games/DCS",
    "C:/Users/iirov/Pictures",
    "C:/users/iirov/videos",
    "C:/users/iirov/AppData/Roaming/.minecraft"
]


# Function which returns last word
def lastWord(string):
    # split by space and converting
    # string to list and
    lis = list(string.split("/"))

    # length of list
    length = len(lis)

    # returning last element in list
    return lis[length - 1]




def kansionHaku():
    for dir in backUpLista:
        try:
            if(os.path.exists(dir) == True):
                print("Kansio '" + dir + "´ on olemassa")
            elif(os.path.exists(dir) == False):
                print("Kansiota '" + dir + "´ ei löytynyt")
                backUpLista.pop(backUpLista.index(dir))
            else:
                print("Kansiota '" + dir + "´ ei löytynyt")
        except FileNotFoundError:

            print("Onkelmia " + FileNotFoundError)

def vientiKansionLuonti():
    try:
        if(os.path.exists(targetDir) == False):
            try:
                os.mkdir(targetDir)
            except FileExistsError:
                print(FileExistsError)
    except FileNotFoundError:
        print(FileNotFoundError)

def siirto():
    for f in backUpLista:

        kansio = lastWord(f)
        print(kansio)
        print(f + ", " + targetDir)
        print(f + ", " + targetDir + "/" + kansio)
        try:
            print("Testi")
            shutil.move(f, targetDir + "/" + kansio)
        except FileNotFoundError:
            print(FileNotFoundError)
def main():
    print("Starting process")

if __name__ == '__main__':

    isRunning = True

    while isRunning:
        print(backUpLista)
        main()
        kansionHaku()
        vientiKansionLuonti()
        print("Aloitetaan siirto")
        siirto()
        isRunning = False
        print(backUpLista)