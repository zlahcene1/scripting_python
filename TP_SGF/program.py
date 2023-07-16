import sys
import os
import ftplib as ftp

def lsDir(PATH):
    file = os.listdir(PATH)
    for f in file:
        print(f)

def lsFile(PATH):
    file = os.listdir(PATH)
    for f in file:
        fpath = os.path.join(PATH, f)
        if os.path.isfile(fpath):
            print(f)

def openDir(PATH):
    try:
        rep = input("quel repertoire? ")
        PATH = os.path.join(os.getcwd(), rep)
        os.chdir(PATH)
        return PATH
    except FileNotFoundError:
        print("Repertoire non existant")
    except PermissionError:
        print("Pas les droits.")


def renameDir(PATH):
    try:
        os.rename(input("Quel repo/fichier? "), input("QUel est sont nouveau nom? "))
    except OSError:
        print("Erreur lors du renommage")
    except FileNotFoundError:
        print("N'existe pas")


def creatDir(PATH):
    print("creatDir")
    sys.exit(0)

def cpDir(PATH):
    print("cpDir")
    sys.exit(0)

def mvDir(PATH):
    print("mvDir")
    sys.exit(0)

def rmDir(PATH):
    
    sys.exit(0)

def openFile(PATH):
    print("openFile")
    sys.exit(0)

def renameFile(PATH):
    print("renameFile")
    sys.exit(0)

def creatFile(PATH):
    print("creatFile")
    sys.exit(0)

def cpFile(PATH):
    print("cpFile")
    sys.exit(0)

def mvFile(PATH):
    print("mvFile")
    sys.exit(0)

def rmFile(PATH):
    print("rmFile")
    sys.exit(0)

def printer():
    print("1. Listez les repertoires")
    print("2. Se deplacer dans un répertoire")
    print("3. Renommer un répertoire/sous répertoire")
    print("4. Créer repertoire")
    print("5. Copier un répertoire")
    print("6. Déplacer un répertoire")
    print("7. Supprimer un répertoire")

    print("8. Listez les fichiers")
    print("9. Ouvrir fichier")
    print("10. Renommer un fichier")
    print("11. Créer un fichier")
    print("12. Copier un fichier")
    print("13. Déplacer un fichier")
    print("14. Supprimer un fichier")

    print("0. Quitter")


def catchCmd():
    printer()
    cmd = input("$> ")
    if not cmd.isdigit(): catchCmd()
    cmd = int(cmd)
    if cmd > 14: catchCmd()
    elif cmd == 0: sys.exit(0)
    else: return cmd

funcTab = [lsDir, openDir, renameDir, creatDir, cpDir, mvDir, rmDir, lsFile, openFile, renameFile, creatFile, cpFile, mvFile, rmFile]

def cli(PATH):
    cmd = catchCmd()
    PATH = funcTab[cmd - 1](PATH)
    cli(PATH)

def main():
    print("Bienvenu jeune Padawan\nEs tu prêt pour l'aventure ?")
    input("O/n: ")
    cli(os.getcwd())

if __name__ == "__main__":
    main()