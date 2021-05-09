from tkinter import *
from tkinter import ttk as onglet
from tkinter import filedialog as dossier
import sqlite3

conn = sqlite3.connect('admin.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     UnknowDirectory TEXT,
     MoveDirectory TEXT
)
""")
# cursor.execute("INSERT INTO admin(id,UnknowDirectory, MoveDirectory) VALUES('1','testok', 'test')")

conn.commit()


def Unknowschoixrep():
    global rep
    rep = dossier.askdirectory(initialdir="/", title='Choisissez un repertoire')
    if len(rep) > 0:
        UnknowDirectory.delete(0, "end")
        UnknowDirectory.insert(0, rep)
        print("vous avez choisi le repertoire %s" % rep)


def Movechoixrep():
    global rep
    rep = dossier.askdirectory(initialdir="/", title='Choisissez un repertoire')
    if len(rep) > 0:
        MoveDirectory.delete(0, "end")
        MoveDirectory.insert(0, rep)
        print("vous avez choisi le repertoire '%s'" % rep)


def savechoixrep():
    unknowdirectoryvaleur = UnknowDirectory.get()
    movedirectoryvaleur = MoveDirectory.get()
    print("'%s'" % unknowdirectoryvaleur)
    print("'%s'" % movedirectoryvaleur)
    cursor.execute("UPDATE admin SET UnknowDirectory = '%s' , MoveDirectory = '%s' WHERE id= 1" %(unknowdirectoryvaleur,movedirectoryvaleur,))
    conn.commit()


fenetre = Tk()
fenetre.title("Security by Marescowww")
fenetre.geometry("500x300")

n = onglet.Notebook(fenetre)  # Création du système d'onglets
n.pack()
o1 = onglet.Frame(n, width=490, height=280)  # Ajout de l'onglet 1
o1.pack()
o2 = onglet.Frame(n, width=490, height=280)  # Ajout de l'onglet 2
o2.pack()
o3 = onglet.Frame(n, width=490, height=280)  # Ajout de l'onglet 3
o3.pack()

n.add(o1, text='Configuration')  # Nom de l'onglet 1
n.add(o2, text='Reconnaissance')  # Nom de l'onglet 2
n.add(o3, text='Détéction')  # Nom de l'onglet 3

Titre = Label(o1, text='Répertoire des sources')
Titre.pack()
BDD = Label(o1, text='Base de données en local')
BDD.pack()
VotreChoix1 = Label(o1, text='Répertoire de sortie de l\'inconnu')
VotreChoix1.pack()

rep = ''
UnknowDirectory = Entry(o1)
UnknowDirectory.pack()
btnchoixUnknow = Button(o1, text='Votre choix', command=Unknowschoixrep)
btnchoixUnknow.pack()

VotreChoix2 = Label(o1, text='Répertoire de sortie du mouvement')
VotreChoix2.pack()
MoveDirectory = Entry(o1)
MoveDirectory.pack()
btnchoixrepMove = Button(o1, text='Votre choix', command=Movechoixrep)
btnchoixrepMove.pack()

btnsave = Button(o1, text='Sauvegarder', command=savechoixrep)
btnsave.pack()

btnquitter = Button(o1, text='Quitter', command=o1.destroy)
btnquitter.pack()

fenetre.mainloop()
