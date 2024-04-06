from tkinter import * 
import tkinter as tk
from pydoc import doc
from datetime import datetime, timedelta
from time import sleep
import time
import random
import pygame
class personne:
    # classe d'une personne toutes leurs informations
    def __init__(self,nom,prenom,age,sexe,travail,education,salaire,iq,bonheur,statut_social):
        bonheur=random.randint(20,60)
        iq=random.randint(70,120)
        statut_social="célibataire"
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.sexe=sexe
        self.travail=travail
        self.education=education
        self.salaire=salaire
        self.iq=iq
        self.bonheur=bonheur
        self.statut_social=statut_social

p=personne('','',18,'','chomeur',["primaire","college","secondaire",""],0,0,0,"")  #initialisation      

#NB: p est le personnage principale du jeu


# ouvrir la fenetre d'ouverture
fenetre1= Tk()
fenetre1.title('tunisian life')
fenetre1.configure(bg="lightblue")#background
fenetre1.wm_state("zoomed")#plein ecran


l1 = Label(fenetre1,text="welcome to tunisian life",bg= "lightblue")
l1.pack()

# entrer des donnees
label = Label(fenetre1,text="donner votre nom",bg= "lightblue")
label.pack()


def nom_prenom(p): # fonction pour rentrer le nom et prénom et passer à la deuxieme fenetre et commencer le son du jeu
     global res # pour utiliser le resultat de l'input dans une autre fonction
     res= myEntry.get() #recuperer le contenu de l'entry
     p.nom=res
     m=myEntry1.get()
     p.prenom=m
     play()
     fenetre1.destroy()
   
def sexe_homme(p):
   p.sexe="homme"
def sexe_femme(p):
    p.sexe="femme"

#champ pour ecrire le nom
myEntry=Entry(fenetre1, textvariable=str,width=40)
myEntry.pack(pady=20)

label = Label(fenetre1,text="donner votre prénom",bg= "lightblue")
label.pack()

#champ pour ecrire le prenom
myEntry1=Entry(fenetre1, textvariable=str,width=40)
myEntry1.pack(pady=20)

label = Label(fenetre1,text="choisir votre sexe",bg= "lightblue")
label.pack()
# 2 boutons de choix de sexe
btn = tk.Button(fenetre1, height=1, width=10, text="masculin",command=lambda:sexe_homme(p),bg='gray')
btn.pack()

btn=tk.Button(fenetre1,height=1,width=10,text="feminin",command=lambda:sexe_femme(p),bg='gray')
btn.pack()

def regles(fenetre):# fonction pour afficher les regles du jeu lors de l'appuis sur bouton
    fenetre8=tk.Toplevel(fenetre)
    fenetre8.title("règles")
    label=Label(fenetre8,text="*Tunisian life c'est un jeu qui simule la vie d'une personnage et sa famille\n*si votre budget atteint un montant inférieur à -5000 vous perdez")
    label.pack()
bouton=Button(fenetre1,height=1,width=10,text="règles",command=lambda:regles(fenetre1))
bouton.pack()

btn = tk.Button(fenetre1, height=1, width=10, text="jouer", command=lambda: nom_prenom(p),bg="white" )# pour commencer jouer et appliquer la fonction nom_prenom
btn.pack()

# insertion du son dans le jeu
pygame.mixer.init()
def play():
    pygame.mixer.music.load(r"C:\Users\mmari\Desktop\tunisian life\Y2meta.app - Board Game Night Music_ The Perfect Background Music for Your Next Game Night (128 kbps).mp3")
    pygame.mixer.music.play(loops=0)


fenetre1.mainloop()
# ouvrir fenetre 1



def ouvrir_nouvelle_fenetre(p): #fonction qui affiche les données de personne selectionner
     fenetre3= tk.Toplevel(fenetre2)
     fenetre3.title('tunisian life')
     fenetre3.geometry("300x400")
     largeur_ecran = fenetre3.winfo_screenwidth() #prend la largeur de l'ecran

     #Définir la position de la fenêtre à droite
     fenetre3.geometry(f"+{largeur_ecran - 400}+100") # on place la fenetre  droite de l'écran
     l3=tk.Label(fenetre3, text="")
     l3.pack() 
     l4=tk.Label(fenetre3,text="")
     l4.pack()
     l5=tk.Label(fenetre3,text="")
     l5.pack()
     l6=tk.Label(fenetre3,text="")
     l6.pack()
     l7=tk.Label(fenetre3,text="")
     l7.pack()
     l8=Label(fenetre3,text="") 
     l8.pack()
     l9= Label(fenetre3,text="")
     l9.pack()
     l10=Label(fenetre3,text="")
     l10.pack()
     l11=Label(fenetre3,text="")
     l11.pack()
     l12=Label(fenetre3,text="")
     l12.pack()
     l3.config(text="Nom :"+p.nom) #config pour modifier les informations
     l4.config(text="\nPrénom : "+ p.prenom)
     l5.config(text="\nSexe : "+ p.sexe)
     l6.config(text="\nAge : "+ str(p.age))
     l7.config(text="\nTravail : "+ p.travail)
     l8.config(text="\nEducation : "+p.education[0]+' '+p.education[1]+' '+p.education[2]+' '+p.education[3])
     l9.config(text="\nSalaire : "+str(p.salaire))
     l10.config(text="\nBonheur : "+str(p.bonheur))
     l11.config(text="\nIQ : "+str(p.iq))
     l12.config(text="\nStatut social : "+p.statut_social)
     


#ouvrir fenetre 2
from PIL import Image, ImageTk    
fenetre2= Tk()
fenetre2.title('tunisian life')
fenetre2.geometry("1080x720")
fenetre2.wm_state("zoomed") #plein ecran


from tkinter import *
import datetime

fenetre2.config(bg='lightblue')
from pydoc import doc
from datetime import datetime, timedelta
from time import sleep
import time
import random
# Créer une fonction pour mettre à jour l'heure
def update_time():
    # Obtenir la date et l'heure actuelles
           now = datetime.now()
    # Afficher la date et l'heure dans le label
        # Formater la date et l'heure
           heure = now.strftime("%H:%M:%S")
           date = now.strftime("%d/%m")
           label.config(text=f"{heure} - {date} ")
           
           
    # Mettre à jour l'heure toutes les secondes
           fenetre2.after(1000, update_time)
           


# Créer un label date et heure
label = Label(fenetre2, text="Date et heure",bg='lightblue') 
#pack dans la ligne 222

def annee (): # incrementer  l'annee de 1 et l'age chaque 30 secondes
     global annee_actuelle
     annee_actuelle+=1
     p.age+=1
     for e in list_pers:
         e.age+=1
     for e in list_enfant :
         e.age+=1   
     annee_label.config(text=f"année :  {annee_actuelle}")
     fenetre2.after(30000, annee)

def increment_budget(): #incrementer budget de la famille chaque 2 secondes et si budget inferieur à -5000 alors le joueur perd
    global budget
    budget+=p.salaire
    for e in list_pers :
       budget+=e.salaire
    # Mettre à jour le texte du label
    budget_label.config(text=f"budget : {budget}")

    if budget<=-5000:
     fenetre10=tk.Tk()
     fenetre10.title('tunisian life')
     fenetre10.geometry("1080x720")
     fenetre10.wm_state("zoomed")
     fenetre10.config(bg='black')
     label=Label(fenetre10,text='GAME OVER',font=("courier",100),fg='red',bg='black')
     label.pack()
     fenetre2.destroy()

    # Rappeler la fonction après 2 seconde
    fenetre2.after(2000, increment_budget)

# Initialiser le budget
budget=100
# Créer un label pour afficher l'année
annee_actuelle=2023 #intialisation année
annee_label= tk.Label(fenetre2, text=f"Année : {annee_actuelle}", bg='lightblue')
annee_label.pack()
# Créer un label pour afficher le budget
budget_label = tk.Label(fenetre2, text=f"Budget : {budget}",bg='lightblue')
budget_label.pack()


# Afficher le label
label.pack()

#importer background
bgimg= tk.PhotoImage(file =r"C:\Users\mmari\Desktop\tunisian life\garden_generated.png")
limg= Label(fenetre2, i=bgimg)
limg.pack()

#list de personne et les enfants du jeu
list_pers=[]
list_enfant=[]

from PIL import Image, ImageTk   
# importer photo de l'homme et de la femme
if p.sexe=='homme':
    image_pil = Image.open(r"C:\Users\mmari\Desktop\tunisian life\man (3).png")
elif p.sexe=='femme':
    image_pil = Image.open(r"C:\Users\mmari\Desktop\tunisian life\femme.png")

# placer l'image dans un label   
image_tk = ImageTk.PhotoImage(image_pil)
label_image = tk.Label(fenetre2, height=80, width=80, image=image_tk,bg="lightblue")
label_image.place(x=700, y=70)

#bouton qui affiche les données de la personne 
bou = Button(fenetre2, height=1, width=10,text = "mes données",command=lambda: ouvrir_nouvelle_fenetre(p),bg='light blue')
bou.place(x=700, y=160)

# mettre à jour le temps le budget et l'année
update_time()  
increment_budget()  
annee()


def ne_pas_travailler(p,fenetre): # correspnd au choix s'il ne veux pas travailler : les consequences de ce choix
     p.iq-=5
     fenetre5=tk.Toplevel(fenetre) #fenetre 5 au dessus de la fenetre principale
     fenetre5=tk.Tk()
     fenetre5.title("")
     lab1=tk.Label(fenetre5, text="IQ -5",fg='red')
     lab1.pack()
     lab2=tk.Label(fenetre5,text="Il est difficile d'échouer mais il est encore plus difficile de ne pas avoir essayé de réussir")
     lab2.pack()
     fenetre.destroy()

def travailler(p,fenetre)    :# correspnd au choix s'il veux travailler : les consequences de ce choix
     p.iq+=5
     p.bonheur+=10
     p.salaire+=300
     p.travail='ouvrier' 
     fenetre5=tk.Toplevel(fenetre)
     fenetre5=tk.Tk()
     fenetre5.title("")
     lab2=tk.Label(fenetre5,text="Bonheur +10\nSalaire =300 TND\nIQ +5",fg= 'green')
     lab2.pack()
     lab=tk.Label(fenetre5, text="vous etes maintenant un ouvrier avec un salaire de 300 dinars")
     lab.pack()
     lab1=tk.Label(fenetre5,text="**n'oubliez pas Le succès est la somme de petits efforts, répétés jour après jour**")
     lab1.pack()
     fenetre.destroy()

def demander(p,fenetre):# correspnd au choix s'il veux demander de l'argent: les consequences de ce choix
      global budget
      p.iq-=2
      budget+=10
      fenetre5=tk.Toplevel(fenetre)
      fenetre5=tk.Tk()
      fenetre5.title=("")
      lab1=tk.Label(fenetre5,text="IQ -2",fg="red")
      lab1.pack()
      lab2=tk.Label(fenetre5,text='BUDGET +10',fg='green')
      lab2.pack()
      lab=tk.Label(fenetre5, text="tu as reçu 10 dinars n'oublie jamais que le travail pense, la paresse songe")
      lab.pack()
      fenetre.destroy()
      
def refuser_formation(p,fenetre):# correspnd au choix s'il refuse la formation : les consequences de ce choix
     p.iq-=5
     p.salaire=0
     p.bonheur-=10
     p.travail='chomeur'
     fenetre5=tk.Toplevel(fenetre)
     fenetre5=tk.Tk()
     fenetre5.title=("")
     lab1=tk.Label(fenetre5,text="IQ -5\nSALAIRE=0\nBONHEUR -10",fg='red')
     lab1.pack()
     lab=tk.Label(fenetre5, text="grâce à la formation tes collègues ont développé leurs acquis , toi ton chef décide de te virer\n_n'oublie jamais apprendre c'est avoir un projet, c'est se projeter différent dans l'avenir__")
     lab.pack()
     fenetre.destroy()

def accepter_formation(p,fenetre):# correspnd au choix s' il accepte la formation : les consequences de ce choix
     p.iq+=5
     p.salaire+=100  
     fenetre5=tk.Toplevel(fenetre)
     fenetre5=tk.Tk()
     fenetre5.title=("")
     lab1=tk.Label(fenetre5, text='IQ +5\nSALAIRE +100',fg='green')
     lab1.pack()
     lab=tk.Label(fenetre5, text="suite à votre persévérance t'as reçu une promotion de travail et votre salaire augmente de 100 dinars \n__ Apprendre c'est avoir un projet, c'est se projeter différent dans l'avenir __")    
     lab.pack()
     fenetre.destroy()

def accepter_chef(p,fenetre)   : # correspnd au choix s'il accepte de travailler des heures sup : les consequences de ce choix
     global budget
     p.iq+=1
     budget+=100
     p.bonheur+=3
     fenetre5=tk.Toplevel(fenetre)
     fenetre5=tk.Tk()
     fenetre5.title=("")
     lab1=tk.Label(fenetre5,text="IQ 1\nBUDGET 100\nBONHEUR 3",fg='green')
     lab1.pack()
     lab=tk.Label(fenetre5, text="suite à votre travail, ton chef a décidé de vous donner une prime de 100 dinars\n**TRAVAILLER DUR EN SILENCE LAISSEZ PARLER VOTRE SUCCÈS**\n")
     lab.pack()
     fenetre.destroy()

def refuser_chef(p,fenetre):# correspnd au choix s'il refuse de travailler des heures sup : les consequences de ce choix
     p.salaire=0
     p.travail="chomeur"
     p.bonheur-=10
     fenetre5=tk.Toplevel(fenetre)
     fenetre5=tk.Tk()
     fenetre5.title=("")
     lab1=tk.Label(fenetre5,text="BONHEUR -10\n SALAIRE 0" ,fg='red')
     lab1.pack()
     lab=tk.Label(fenetre5, text="ton chef a décidé de vous virer\n**CELUI QUI N'A JAMAIS APPRIS À OBÉIR NE PEUT PAS ÊTRE UN BON COMMANDANT**")
     lab.pack()
     fenetre.destroy()

def donner5(p,fenetre): # correspnd au choix s'il donne 5d : les consequences de ce choix
     global budget
     p.bonheur+=6
     budget-=5
     fenetre5=tk.Toplevel(fenetre)
     fenetre5=tk.Tk()
     fenetre5.title=("")
     lab1=tk.Label(fenetre5,text="BONHEUR +6",fg='green')
     lab1.pack()
     lab2=tk.Label(fenetre5,text=" BUDGET -5",fg='red')
     lab2.pack()
     lab=tk.Label(fenetre5, text="LA VALEUR D UNE PERSONNE SE VOIT QUAND ELLE AIDE LES AUTRES TOUT EN SACHANT QU ELLE NE VA RIEN RECEVOIR EN RETOUR")
     lab.pack()
     fenetre.destroy()

def refuser_donner(p,fenetre):#correspnd au choix s'il refuse  donner  : les consequences de ce choix
     fenetre5=tk.Toplevel(fenetre)
     fenetre5=tk.Tk()
     fenetre5.title=("")
     lab=tk.Label(fenetre5, text='CELUI QUI NE VEUT PAS AIDER NE PEUT ETRE AIDE PAR PERSONNE')
     lab.pack()
     fenetre.destroy()

def donner2(p,fenetre): #correspnd au choix s'il donne 5d : les consequences de ce choix
     global budget
     p.bonheur+=2
     budget-=2
     fenetre5=tk.Toplevel(fenetre)
     fenetre5=tk.Tk()
     fenetre5.title=("")
     lab1=tk.Label(fenetre5,text="BONHEUR +2",fg='green')
     lab1.pack()
     lab2=tk.Label(fenetre5,text="BUDGET -2",fg='red')
     lab2.pack()
     lab=tk.Label(fenetre5, text="LA VALEUR D UNE PERSONNE SE VOIT QUAND ELLE AIDE LES AUTRES TOUT EN SACHANT QU ELLE NE VA RIEN RECEVOIR EN RETOUR")
     lab.pack()
     fenetre.destroy()

def accepter_idée(p,fenetre):#correspnd au choix s'il accepter l'idee de son collegue : les consequences de ce choix
    p.iq+=3
    p.bonheur+=2
    fenetre5=tk.Toplevel(fenetre)
    fenetre5=tk.Tk()
    fenetre5.title=("")
    lab1=tk.Label(fenetre5,text="IQ +3\nBONHEUR +2",fg='green')
    lab1.pack()
    lab=tk.Label(fenetre5, text="L'ingédient le plus important dans la formule du succés est de savoir comment s'entendre avec les gens.")
    lab.pack()
    fenetre.destroy()

def refuser_idée(p,fenetre):#correspnd au choix s'il refuse l'idee de son collegue : les consequences de ce choix
    p.iq-=3
    fenetre5=tk.Toplevel(fenetre)
    fenetre5=tk.Tk()
    fenetre5.title=("")
    lab1=tk.Label(fenetre5,text="IQ -3",fg='red')
    lab1.pack()
    lab=tk.Label(fenetre5, text="Les gens qui ne prennent pas en compte l'avis des autres sont destinés à perdre leur relation avec la réalité.")
    lab.pack()
    fenetre.destroy()

def voiture_populaire(p,fenetre):#correspnd au choix s'il accepte avoir une voiture : les consequences de ce choix
    global budget
    p.bonheur+=10
    budget-=30000
    fenetre5=tk.Toplevel(fenetre)
    fenetre5=tk.Tk()
    fenetre5.title=("")
    lab1=tk.Label(fenetre5,text='BONHEUR +10',fg='green')
    lab1.pack()
    lab2=tk.Label(fenetre5,text="BUDGET -30000",fg='red')
    lab2.pack()
    fenetre.destroy()

def voiture_luxueuse(p,fenetre):#correspnd au choix s'il accepte avoir une voiture : les consequences de ce choix
    global budget
    p.bonheur+=20
    budget-=120000
    fenetre5=tk.Toplevel(fenetre)
    fenetre5=tk.Tk()
    fenetre5.title=("")
    lab1=tk.Label(fenetre5,text='BONHEUR +20',fg='green')
    lab1.pack()
    lab2=tk.Label(fenetre5,text="BUDGET -120000",fg='red')
    lab2.pack()
    fenetre.destroy()

def aleapersonne(s):  #fonctin de creation de personnage aléatoire et s le sexe de la personne
   liste_nom=['Trabelsi','Benali','Mejbri']
   liste_prenomf=['Zeineb','Kmar','Saousen']
   liste_prenomh=['Mohamed','Ali','Youssef']
   liste_travail=['Plombier','Ingénieur','Coiffeur','Médecin']
   liste_education=[["primaire","college","secondaire",''],["primaire","college","secondaire","univeritaire"],["primaire","college","secondaire",''],["primaire","college","secondaire","universitaire"]]
   liste_salaire=[700,1200,850,1300]
   w=random.randint(0,2)
   m=random.randint(0,2)
   d=random.randint(0,3)
   if s=='femme':
       x=personne(liste_nom[w],liste_prenomf[m],random.randint(18,55),'femme',liste_travail[d],liste_education[d],liste_salaire[d],0,0,'')
       return x
   else:
       y=personne(liste_nom[w],liste_prenomh[m],random.randint(18,55),'homme',liste_travail[d],liste_education[d],liste_salaire[d],0,0,'')
       return y
   


def non_mariage(p,fenetre,label_image1,bouton) : #s'il refuse de se marier
    fenetre6=tk.Toplevel(fenetre)
    fenetre6=tk.Tk()
    fenetre6.title=("")
    p.bonheur-=10
    lab=tk.Label(fenetre6,text="BONHEUR -10",fg='red')
    lab.pack()
    label_image1.destroy()
    bouton.destroy()
    fenetre.destroy()





def oui_mariage(p,fenetre,fm,list_pers) :#s'il accepte de se marier pour p homme
   global budget
   list_pers.append(fm)
   fenetre6=tk.Toplevel(fenetre)
   fenetre6=tk.Tk()
   
   fenetre6.title=("")
   
   budget-=6000
   p.statut_social='marié'
   fm.statut_social='mariée'
   p.bonheur+=10 
   lab1=tk.Label(fenetre6,text='BONHEUR +10',fg='green')
   lab1.pack()
   lab2=tk.Label(fenetre6,text="BUDGET -6000",fg='red')
   lab2.pack()
   lab3=tk.Label(fenetre6,text="felicitation!!,vous êtes mariés")
   lab3.pack()
   fenetre.destroy()
    

def oui_mariage2(p,fenetre,fm,list_pers) : #s'il accepte de se marier pour p femme
   global budget
   list_pers.append(fm)
   fenetre6=tk.Toplevel(fenetre)
   fenetre6=tk.Tk()
   
   fenetre6.title=("")
   
   budget-=6000
   p.statut_social='mariée'
   fm.statut_social='marié'
   p.bonheur+=10 
   lab1=tk.Label(fenetre6,text='BONHEUR +10',fg='green')
   lab1.pack()
   lab2=tk.Label(fenetre6,text="BUDGET -6000",fg='red')
   lab2.pack()
   lab3=tk.Label(fenetre6,text="felicitation!!,vous êtes marriés")
   lab3.pack()
   fenetre.destroy()

#initialisation du partenaire fm
fm=personne('','',0,'','',[],0,0,0,"")  

#fonctin de creation de personnage aléatoire et s le sexe de la personne
def aleaenfant()  :
   global list_enfant
   liste_prenomf=['Zeineb','Kmar','Saousen']
   liste_prenomh=['Mohamed','Ali','Youssef']
   w=random.randint(0,2)
   s=random.randint(0,1)
   if s==0:
       x=personne(p.nom,liste_prenomf[w],0,'femme','chomeur',['','','',''],0,0,0,'célibataire')
       list_enfant.append(x)
       return x
   else:
       y=personne(p.nom,liste_prenomh[w],0,'homme','chomeur',['','','',''],0,0,0,'célibataire')
       list_enfant.append(y)
       return y



h=200 #pour ajouter les photos des enfants dans la sens contraire si il depasse la limite de la fentre du coté droite
i=0 #intitialisatin de i pour la position de l'enfant
def oui_enfant(p,fenetre,fm):#correspnd au choix s'il accepte avoir un enfant : les consequences de ce choix  avec fm paretenaire et p la personnage principale
    global budget #obligatirement des variables globale
    global i
    global h
    p.bonheur+=20
    fm.bonheur+=20
    budget-=5000
    k=aleaenfant()
    image_pil = Image.open(r"C:\Users\mmari\Desktop\tunisian life\bebe.png")#image enfant
    image_tk= ImageTk.PhotoImage(image_pil)
    label_image= tk.Label(fenetre2,height=80,width=80,image=image_tk,bg="lightblue")
    label_image.image_pil=image_tk
    label_image.pack()
    if i==600: #si on depasse la limite droite  on le met à gauche
        label_image.place(x=800-h,y=200)
        
    else:
       label_image.place(x=800+i, y=200)

    fenetre6=tk.Toplevel(fenetre)
    fenetre6=tk.Tk()
    fenetre6.title=("")
    lab1=tk.Label(fenetre6,text='BONHEUR +20',fg='green')
    lab1.pack()
    lab2=tk.Label(fenetre6,text="BUDGET -5000",fg='red')
    lab2.pack()
    lab3=tk.Label(fenetre6,text="felicitation!!")
    lab3.pack()
    bouton6=Button(fenetre2,height=1,width=10,text='Données',command=lambda:ouvrir_nouvelle_fenetre(k),bg='lightblue')#données enfant
    bouton6.pack()
    
    if i==600:
        bouton6.place(x=800-h,y=285)
        h+=200
    else:
        bouton6.place(x=800+i,y=285)
        i+=200
    fenetre.destroy()
    return i

def cadeau_voiture(p,fenetre,fm):#correspnd au choix s'il accepte offrire une voiture : les consequences de ce choix
    global budget
    budget-=70000
    p.bonheur+=10
    fm.bonheur+=30
    fenetre6=tk.Toplevel(fenetre)
    fenetre6=tk.Tk()
    fenetre6.title=("")
    label=Label(fenetre6,text="bonheur +10 :"+p.prenom,fg='green')
    label.pack()
    label1=Label(fenetre6,text="bonheur +30 :"+fm.prenom,fg='green')
    label1.pack()
    label2=Label(fenetre6,text="budget -70000:",fg='red')
    label2.pack()
    fenetre.destroy()

def cadeau_bouquet(p,fenetre,fm):#correspnd au choix s'il accepte offrire un bouquet : les consequences de ce choix
    global budget
    budget-=100    
    fm.bonheur+=5
    fenetre6=tk.Toplevel(fenetre)
    fenetre6=tk.Tk()
    fenetre6.title=("")
    label = Label(fenetre6, text='Bonheur +5',fg='green')
    label.pack()
    label1=Label(fenetre6,text='Budget -100',fg='red')
    label1.pack()
    fenetre.destroy()

def ne_pas_offrir(p,fenetre,fm):#correspnd au choix s'il refuse offrire : les consequences de ce choix
    fm.bonheur-=20
    p.bonheur-=20
    fenetre6=tk.Toplevel(fenetre)
    fenetre6=tk.Tk()
    fenetre6.title=("")
    label = Label(fenetre6, text='bonheur -20',fg='red')
    label.pack()
    fenetre.destroy()


def parler(p,fenetre,fm):#correspnd au choix s'il parle avec son partenaire : les consequences de ce choix
    p.bonheur+=10
    fm.bonheur+=10
    fenetre6=tk.Toplevel(fenetre)
    fenetre6=tk.Tk()
    fenetre6.title=("")
    
    label1=Label(fenetre6,text="Bonheur +10",fg='green')
    label1.pack()
    label=Label(fenetre6,text="vous avez resolu vos problèmes")
    label.pack()
    fenetre.destroy()

def divorcer(p,fenetre,label_image,bouton_mariage):# s'il veut se divorcer
    p.bonheur-=20
    label_image.destroy()
    bouton_mariage.destroy()
    p.statut_social='célibataire'
    fenetre6=tk.Toplevel(fenetre)
    fenetre6=tk.Tk()
    fenetre6.title=("")
    label1=Label(fenetre6,text='Bonheur -20 \nStatut social Célibataire',fg='red')
    label1.pack()
    label=Label(fenetre6,text="Vous êtes maintenant célibataire")
    label.pack()
    fenetre.destroy()

def demissioner(p,fenetre):#correspnd au choix s'il demissione : les consequences de ce choix
    p.salaire=0
    p.travail='chomeur'
    p.bonheur-=20
    fenetre5=tk.Toplevel(fenetre)
    fenetre5=tk.Tk()
    fenetre5.title('')
    label=Label(fenetre5,text='Vous êtes chômeur\n Bonheur -20\nSalaire 0',fg='red')
    label.pack()
    fenetre.destroy()

def ne_rien_faire(p,fenetre):#correspnd au choix de rien faire : les consequences de ce choix
    p.bonheur-=20
    fenetre5=tk.Toplevel(fenetre)
    fenetre5=tk.Tk()
    fenetre5.title('')
    label=Label(fenetre5,text='Bonheur -20',fg='red')    
    label.pack()
    fenetre.destroy()

def parler_chef(p,fenetre): #correspnd au choix de parler avec le chef : les consequences de ce choix
    p.bonheur+=5
    fenetre5=tk.Toplevel(fenetre)
    fenetre5=tk.Tk()
    fenetre5.title('')
    label=Label(fenetre5,text='Bonheur +5',fg='green')
    label.pack()
    label1=Label(fenetre5,text='vous avez  parlé à votre chef et vous avez résolu le conflit')
    label1.pack()
    fenetre.destroy()

def oui_maison(p,fenetre):#correspnd au choix de renover la maison : les consequences de ce choix
    global budget
    budget-=120000
    p.bonheur+=20
    for e in list_pers: #augmenter  le bonheur pour toute la famille
        e.bonheur+=20
    for e in list_enfant:
        e.bonheur+=20
    fenetre5=tk.Toplevel(fenetre)
    fenetre5.title('')
    label=Label(fenetre5,text='Bonheur +20',fg='green')
    label.pack()
    label1=Label(fenetre5,text='Budget -120000',fg='red')
    label1.pack()
    fenetre.destroy()

def oui_universite(p,fenetre): #correspnd au choix de finir ces etudes : les consequences de ce choix
    global budget
    budget-=10000
    p.salaire=700
    p.bonheur+=20
    p.iq+=10
    p.travail='technicien supérieur'
    p.education[3]='Université'
    fenetre5=tk.Toplevel(fenetre)
    fenetre5=tk.Tk()
    fenetre5.title('')
    label1=Label(fenetre5,text='IQ +10\nBonheur+=20\nSalaire=700',fg='green')
    label1.pack()
    label2=Label(fenetre5,text='Budget -10000',fg='red')
    label2.pack()
    label=Label(fenetre5,text="vous avez reçu votre diplome universitaire et vous etes devenu un technicien supérieur")
    label.pack()
    fenetre.destroy()


def non_universite(p,fenetre):#correspnd au choix de ne pas finir ces etudes : les consequences de ce choix
    p.iq-=15
    fenetre5=tk.Toplevel(fenetre)
    fenetre5=tk.Tk()
    fenetre5.title('')
    label1=Label(fenetre5,text='IQ -15',fg='red')
    label1.pack()
    fenetre.destroy()

k=0 # pour intialiserle compteur de type de question dans la fonction question si mod3=1 questions de travail si =2 question sociale si non des questions de mariage

import threading
import random
def question(p): # fonction qui gere les questions
    global k
    global fenetre4
    fenetre4= tk.Toplevel(fenetre2)
    fenetre4.title("Question ?")
    
    fenetre4.geometry("500x500")
    fenetre4.protocol("WM_DELETE_WINDOW", on_closing)  # Gérer la fermeture de la fenêtre si elle est  refermée par l’utilisateur on closing est definit plus tard
    fenetre4.bind("<Destroy>", on_destroy) # Gérer la fermeture de la fenêtre si elle est  fermée par la fonction on destroy est est definit plus tard
   
    if k%3==0:
        k+=1
        if (p.travail=='chomeur'):
           Label1=tk.Label(fenetre4,text="choisir tes choix de vie : ")
           Label1.pack()
           bouton1=Button(fenetre4,height=4,width=40,text="ne pas travailler",command=lambda:ne_pas_travailler(p,fenetre4))
           bouton1.pack() 
           bouton2=Button(fenetre4, height=4,width=40,text="postuler pour un travail",command=lambda:travailler(p,fenetre4)) 
           bouton2.pack()
           bouton3=Button(fenetre4, height=4,width=40,text="Demander l'argent dans les rues",command=lambda:demander(p,fenetre4)) 
           bouton3.pack()

        else :
           m=random.randint(1,4)
           match m:
              case 1:
                 label=tk.Label(fenetre4,text="tu as eu l'opportunité de faire une formation :")
                 label.pack()
                 bouton1=Button(fenetre4,height=4,width=40,text="je ne veux pas ,c'est une perte de temps",command=lambda:refuser_formation(p,fenetre4))
                 bouton1.pack() 
                 bouton2=Button(fenetre4, height=4,width=40,text="oui ,je veux apprendre",command=lambda:accepter_formation(p,fenetre4)) 
                 bouton2.pack()
              case 2:
                 label=tk.Label(fenetre4,text="votre chef t'a donné un ordre de bosser pendant le week end")
                 label.pack()
                 bouton1=Button(fenetre4,height=4,width=40,text="accepter de travailler",command=lambda:accepter_chef(p,fenetre4))
                 bouton1.pack() 
                 bouton2=Button(fenetre4, height=4,width=40,text="refuser de travailler",command=lambda:refuser_chef(p,fenetre4)) 
                 bouton2.pack()
              case 3 :  
                 label=tk.Label(fenetre4,text="votre collégue a une autre vision concernant le travail")
                 label.pack()
                 bouton1=Button(fenetre4,height=4,width=40,text="Discuter avec lui sa propre idée",command=lambda:accepter_idée(p,fenetre4))
                 bouton1.pack() 
                 bouton2=Button(fenetre4, height=4,width=40,text="Refuser de l'entendre",command=lambda:refuser_idée(p,fenetre4)) 
                 bouton2.pack() 
              case 4 :
                   if p.education[3]=='':
                     label=Label(fenetre4,text='voulez-vous continuer vos études universitaires')
                     label.pack()
                     bouton1=Button(fenetre4,text="oui" ,height=4,width=40,command=lambda:oui_universite(p,fenetre4))
                     bouton1.pack()
                     bouton2=Button(fenetre4,text="non",height=4,width=40, command=lambda:non_universite(p,fenetre4))
                     bouton2.pack() 
                   else:  
                     label=Label(fenetre4,text='votre chef vous insulte toujours')
                     label.pack()
                     bouton1=Button(fenetre4,height=4,width=40,text='Démissioner',command=lambda:demissioner(p,fenetre4))
                     bouton1.pack()
                     bouton2=Button(fenetre4,height=4,width=40,text='ne rien faire',command=lambda:ne_rien_faire(p,fenetre4))
                     bouton2.pack()
                     bouton3=Button(fenetre4,height=4,width=40,text='parler avec lui',command=lambda:parler_chef(p,fenetre4))
                     bouton3.pack()
              
                    
    elif k%3==1:
            k+=1
            r=random.randint(1,3)
            match r :
                case 1 :
                   label=tk.Label(fenetre4,text="Vous avez trouvé un enfant qui demande de l'argent pour ses etudes")
                   label.pack() 
                   bouton1=Button(fenetre4,height=4,width=40,text=" lui Donner 5 dinars",command=lambda:donner5(p,fenetre4))
                   bouton1.pack() 
                   bouton2=Button(fenetre4, height=4,width=40,text="L'ignorer",command=lambda:refuser_donner(p,fenetre4)) 
                   bouton2.pack()
                   bouton3=Button(fenetre4, height=4,width=40,text="lui donner 2 dinars",command=lambda:donner2(p,fenetre4)) 
                   bouton3.pack()
                case 2 :
                    label=tk.Label(fenetre4,text="tu veux acheter une nouvelle voiture")
                    label.pack()
                    bouton1=Button(fenetre4, height=4,width=40,text="une voiture populaire  30k",command=lambda:voiture_populaire(p,fenetre4)) 
                    bouton1.pack() 
                    bouton2=Button(fenetre4, height=4,width=40,text="une voiture luxueuse  120k",command=lambda:voiture_luxueuse(p,fenetre4)) 
                    bouton2.pack()
                    bouton3=Button(fenetre4,height=4,width=40,text='je ne veux pas', command=fenetre4.destroy)
                    bouton3.pack()
                case 3 :
                    label=tk.Label(fenetre4,text='voulez vous rénover votre maison')
                    label.pack()
                    bouton1=Button(fenetre4,height=4,width=40,text='non',command=lambda:fenetre4.destroy())
                    bouton1.pack()
                    bouton2=Button(fenetre4,height=4,width=40,text='oui 122k',command=lambda:oui_maison(p,fenetre4))
                    bouton2.pack()

    elif k%3==2 :
                    k+=1   
                    if p.statut_social=="célibataire"  :
                        if p.sexe=='homme':
                            f='femme'
                            fm=aleapersonne(f) 
                            image_pil = Image.open(r"C:\Users\mmari\Desktop\tunisian life\femme.png")
                            global l
                            image_tk= ImageTk.PhotoImage(image_pil)
                            l= tk.Label(fenetre2,height=80,width=80,image=image_tk,bg="lightblue")
                            l.image_pil=image_tk
                            l.pack()
                            l.place(x=900, y=70)
                            global bouton_mariage
                            bouton_mariage=Button(fenetre2,height=1,width=10,text='données',command=lambda:ouvrir_nouvelle_fenetre(fm),bg='lightblue')
                            bouton_mariage.pack()
                            bouton_mariage.place(x=900,y=160)
                            label=tk.Label(fenetre4,text="Tu as fait la rencontre d'une femme et vous avez passé une longue période ensemble\nvoulez vous se marier")
                            label.pack()
                            bouton1=Button(fenetre4, height=4,width=40,text="oui 6k",command=lambda:oui_mariage(p,fenetre4,fm,list_pers)) 
                            bouton1.pack() 
                            bouton2=Button(fenetre4, height=4,width=40,text="non",command=lambda:non_mariage(p,fenetre4,l,bouton_mariage))
                            bouton2.pack()
                        else : 
                            h='homme'
                            fm=aleapersonne(h) 
                            image_pil = Image.open(r"C:\Users\mmari\Desktop\tunisian life\man (3).png")
                            image_tk= ImageTk.PhotoImage(image_pil)
                            l= tk.Label(fenetre2,height=80,width=80,image=image_tk,bg="lightblue")
                            l.image_pil=image_tk
                            l.pack()
                            l.place(x=900, y=70)
                            bouton_mariage=Button(fenetre2,height=1,width=10,text='données',command=lambda:ouvrir_nouvelle_fenetre(fm),bg='lightblue')
                            bouton_mariage.pack()
                            bouton_mariage.place(x=900,y=160)
                            label=tk.Label(fenetre4,text="Tu as fait la rencontre d'un homme et vous avez passé une longue période ensemble\nvoulez vous se marier")
                            label.pack()
                            bouton1=Button(fenetre4, height=4,width=40,text="oui  6k",command=lambda:oui_mariage2(p,fenetre4,fm,list_pers)) 
                            bouton1.pack() 
                            bouton2=Button(fenetre4, height=4,width=40,text="non",command=lambda:non_mariage(p,fenetre4,l,bouton_mariage))
                            bouton2.pack()
                    else :
                            m=random.randint(1,3)
                        
                            match m :
                                case 1 :
                
                                  label=tk.Label(fenetre4,text="Voulez vous avoir un enfant")
                                  label.pack()
                                  bouton55=Button(fenetre4, height=4,width=40,text="oui 5k",command=lambda: oui_enfant(p,fenetre4,list_pers[0])) 
                                  bouton55.pack() 
                                  bouton2=Button(fenetre4, height=4,width=40,text="non",command=lambda:fenetre4.destroy())
                                  bouton2.pack()
                                  
                                case 2 :
                                    label=tk.Label(fenetre4,text="aujourd'hui, c'est l'anniversaire de votre partenaire " )
                                    label.pack()
                                    bouton1=Button(fenetre4,height=4,width=40,text="L'offrir une voiture 70k",command=lambda: cadeau_voiture(p,fenetre4,list_pers[0]))
                                    bouton1.pack()
                                    bouton2=Button(fenetre4,height=4,width=40,text="L'offrir un bouquet de fleur 100",command=lambda:cadeau_bouquet(p,fenetre4,list_pers[0]))
                                    bouton2.pack()
                                    bouton3=Button(fenetre4,height=4,width=40,text="ne pas offrir",command=lambda:ne_pas_offrir(p,fenetre4,list_pers[0]))
                                    bouton3.pack()

                                case 3 :
                                    label=tk.Label(fenetre4,text="Vous avez des problèmes avec votre partenaire" )
                                    label.pack()
                                    bouton1=Button(fenetre4,height=4,width=40,text="parler avec votre partenaire",command=lambda:parler(p,fenetre4,list_pers[0]))
                                    bouton1.pack()
                                    bouton2=Button(fenetre4,height=4,width=40,text='Divorcer',command=lambda:divorcer(p,fenetre4,l,bouton_mariage))
                                    bouton2.pack()

            
        


def on_destroy(event): #fonction qui s'execute lorsque la fenetre est refermee 
          if event.widget == fenetre4:
             thread = threading.Thread(target=m)
             thread.start()

def on_closing():#fonction qui s'execute lorsque la fenetre est refermee par l'utilisateur
    fenetre4.withdraw()  # Cacher la fenêtre
    thread = threading.Thread(target=m)
    thread.start()  # Démarrer un nouveau thread pour créer la fenêtre après un délai de 15 secondes   
    
               
def m(): #fonction qui réaffiche une question chaque 15 secondes
     time.sleep(15)
     question(p)
     

l1=[0,200,400,600]
def enfant_photo(): #fonction qui gere la photo des enfants selon leurs ages
     
     for j in range(len(list_enfant)):
         if (list_enfant[j].age>=6) and list_enfant[j].sexe=='homme':
             image_tk= ImageTk.PhotoImage(image_pil10)
             label_image= tk.Label(fenetre2,height=80,width=80,image=image_tk,bg="lightblue")
             label_image.image_pil10=image_tk
             label_image.pack()
             label_image.place(x=800+l1[j], y=200)
             
         elif (list_enfant[j].age>=6) and list_enfant[j].sexe=='femme':
             image_tk= ImageTk.PhotoImage(image_pil20)
             label_image= tk.Label(fenetre2,height=80,width=80,image=image_tk,bg="lightblue")
             label_image.image_pil20=image_tk
             label_image.pack()
             label_image.place(x=800+l1[j], y=200) 
     fenetre2.after(1000,enfant_photo)
def enfant_education() :#fonction qui gere la photo des enfants selon leurs ages
    global budget
    
    for j in range(len(list_enfant)):
        if list_enfant[j].age>=6  and list_enfant[j].education==['','','',''] :
            list_enfant[j].education[0]='primaire'
            budget-=1000
        elif list_enfant[j].age>=12 and list_enfant[j].age<15 and  list_enfant[j].education==['primaire','','','']:
            list_enfant[j].education[1]='collége'
            budget-=3000
        elif list_enfant[j].age>=15 and list_enfant[j].age<19 and list_enfant[j].education==[ 'primaire','collége','','']:
            list_enfant[j].education[2]='secondaire'
            budget-=5000  
    fenetre2.after(1000,enfant_education)

enfant_education()     
#photo d'une fille et un garçon       
image_pil10 = Image.open(r"C:\Users\mmari\Desktop\tunisian life\bien.png")
image_pil20 = Image.open(r"C:\Users\mmari\Desktop\tunisian life\fille.png")
enfant_photo()

thread=threading.Thread(target=m)
thread.start()

        
fenetre2.mainloop()




