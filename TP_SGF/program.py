import sys
import os
import ftplib as ftp

PATH = os.getcwd()

def lsDir():
    print("lsDir")
    sys.exit(0)

def openDir():
    print("openDir")

    PATH = os.getcwd()
    sys.exit(0)

def renameDir():
    print("renameDir")
    sys.exit(0)

def creatDir():
    print("creatDir")
    sys.exit(0)

def cpDir():
    print("cpDir")
    sys.exit(0)

def mvDir():
    print("mvDir")
    sys.exit(0)

def rmDir():
    print("rmDir")
    sys.exit(0)

def lsFile():
    print("lsFile")
    sys.exit(0)

def openFile():
    print("openFile")
    sys.exit(0)

def renameFile():
    print("renameFile")
    sys.exit(0)

def creatFile():
    print("creatFile")
    sys.exit(0)

def cpFile():
    print("cpFile")
    sys.exit(0)

def mvFile():
    print("mvFile")
    sys.exit(0)

def rmFile():
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

def cli():
    cmd = catchCmd()
    funcTab[cmd - 1]()

    cli()

def main():
    print("Bienvenu jeune Padawan\nEs tu prêt pour l'aventure ?")
    input("O/n: ")
    cli()

if __name__ == "__main__":
    main()