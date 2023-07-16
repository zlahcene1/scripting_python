import sys
import os
import shutil
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
        os.rename(input("Quel repo/fichier? "), input("QUel est son nouveau nom? "))
    except FileNotFoundError:
        print("Le nom n'existe pas")
    except OSError:
        print("Une erreur est servenue")

def creatDir(PATH):
    try:
        os.mkdir(input("Quel sera son nom? "))
    except FileExistsError:
        print("Existe déjà")
    except OSError:
        print("Une erreur est survenue")

def cpDir(PATH):
    try:
        shutil.copytree(os.getcwd() + "/" + input("Quel repo ?") + "/", input("Ou est-ce qu'on copie? "))
    except FileExistsError:
        print("Le répertoire de destination existe déjà.")
    except shutil.Error:
        print("Une erreur est survenue")

def mvDir(PATH):
    try:
        shutil.move(os.getcwd() + "/" + input("Quel repo ?") + "/", os.getcwd() + "/" + input("Où ça?"))
    except FileNotFoundError:
        print("Repertoire n'existe pas")
    except shutil.Error:
        print("Une erreur est survenue")
    

def rmDir(PATH):
    try:
        os.rmdir(os.getcwd() + "/" + input("Quel repertoir? "))
    except FileNotFoundError:
        print("N'existe pas")
    except OSError:
        print("Une erreur est survenue")

def openFile(PATH):
    try:
        with open(os.getcwd() + "/" + input("Quel fichier? "), 'r') as fd:
            print(fd.read())
    except FileNotFoundError:
        print("N'existe pas")
    except IOError:
        print("Une erreur est survenue")

def creatFile(PATH):
    try:
        open(os.getcwd() + "/" + input("Nom du fichier "), 'w')
    except IOError:
        print("Une erreur est survenue")

def cpFile(PATH):
    print("cpFile")
    sys.exit(0)

def mvFile(PATH):
    try:
        shutil.move(os.getcwd() + "/" + input("Quel fichier ?") + "/", input("Ou est-ce qu'on copie? "))
    except FileExistsError:
        print("Le fichier existe déjà.")
    except shutil.Error:
        print("Une erreur est survenue")

def rmFile(PATH):
    try:
        os.remove(os.getcwd() + "/" + input("Quel fichier?"))
    except FileNotFoundError:
        print("Fichier n'existe pas")
    except OSError:
        print("Erreur survenue")

def printer():
    print("1. Listez les repertoires")
    print("2. Se deplacer dans un répertoire")
    print("3. Renommer un répertoire/sous répertoire/fichier")
    print("4. Créer repertoire")
    print("5. Copier un répertoire")
    print("6. Déplacer un répertoire")
    print("7. Supprimer un répertoire")

    print("8. Listez les fichiers")
    print("9. Ouvrir fichier")
    print("10. Créer un fichier")
    print("11. Copier un fichier")
    print("12. Déplacer un fichier")
    print("13. Supprimer un fichier")

    print("0. Quitter")


def catchCmd():
    printer()
    cmd = input("$> ")
    if not cmd.isdigit(): catchCmd()
    cmd = int(cmd)
    if cmd > 14: catchCmd()
    elif cmd == 0: sys.exit(0)
    else: return cmd

funcTab = [lsDir, openDir, renameDir, creatDir, cpDir, mvDir, rmDir, lsFile, openFile, creatFile, cpFile, mvFile, rmFile]

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