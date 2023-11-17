from tkinter import ttk

import pandas as pds
from tkinter import  *
from functools import partial
import numpy as np
df0=pds.read_csv("pokemon.csv",index_col="Name")
df0["Type 2"]=df0["Type 2"].replace(np.nan, "Pas de type")
print(df0)




def recherchernom(df,name):
        try:

            return(df.loc[name])
        except KeyError :
            return ("")

def recherchertypes(df,type1,type2):
        try:

            if (type1 in df["Type 1"].values) or (type2 in df["Type 2"].values):
                if (type1 in df["Type 1"].values) and (type2 in df["Type 2"].values):
                    return(df[(df["Type 1"] == type1) & (df["Type 2"]==type2)])
                elif (type1 in df["Type 1"].values) and (type2 not in df["Type 2"].values):
                    return (df[(df["Type 1"] == type1)])

            else:
                raise KeyError
        except KeyError:
            return("")

def rechercherlegendaire(df,c):
    try:
        if c=="Oui":
            return(df[df["Legendary"]==True])
        elif c=="Non":
            return (df[df["Legendary"] == False])
        else:
            raise KeyError
    except KeyError:
        return("")


def recherchergeneration(df,c):
    try:
        if c in [str(x) for x in list(set(df0["Generation"].values))] :
            return(df[df["Generation"]==int(c)])
        else:
            raise KeyError
    except KeyError:
        return("")



def rechercherpdv(df,resis):
    try:
        if resis=="Peu résistant":
            return (df[(df["HP"]>=0) & (df["HP"]<40)])
        elif resis == "Moyennement résistant":
            return (df[(df["HP"]>=40) & (df["HP"]<80)])
        elif resis == "Résistant":
            return (df[(df["HP"]>=80) & (df["HP"]<120)])
        elif resis== "Très résistant":
            return(df[df["HP"]>=120])
        else:
            raise KeyError
    except KeyError:
        return("")





def update_label_recherche(lbl,df,name,c,d,e,f,g):
    global a
    try:
        if name.get()=="":
            res=rechercherlegendaire(df,c.get())
            res1=recherchergeneration(df,d.get())
            res2=recherchertypes(df,e.get(),f.get())
            res3=rechercherpdv(df,g.get())


            if (any(res) is False) or (any(res1) is False) or (any(res2) is False) or (any(res3) is False):
                if any(res) is False and (any(res1) is True) and (any(res2) is True) and (any(res3) is True):
                    res2=recherchertypes(res1,e.get(),f.get())
                    a=rechercherpdv(res2,g.get())
                elif any(res1) is False and (any(res) is True) and (any(res2) is True) and (any(res3) is True):
                    res2=recherchertypes(res,e.get(),f.get())
                    a=rechercherpdv(res2,g.get())
                elif any(res2) is False and (any(res) is True) and (any(res1) is True) and (any(res3) is True):
                    res1=recherchergeneration(res,d.get())
                    a=rechercherpdv(res1,g.get())
                elif any(res3) is False and (any(res) is True) and (any(res1) is True) and (any(res2) is True):
                    res1 = recherchergeneration(res, d.get())
                    a = recherchertypes(res1, e.get(), f.get())

            else:
                res1=recherchergeneration(res,d.get())
                res2=recherchertypes(res1,e.get(),f.get())
                a=rechercherpdv(res2,g.get())

            lbl.config(text=str(a.index.values) + "\n" + "Le nombre de pokémon est :" + str(len(a.index.values)))

        else:
            pok=recherchernom(df,name.get())
            k=""
            if any(pok) is False:
                    lbl.config(text="Pokémon inexistant")
            else:
                for i in range (len(df0.columns.values)):
                        k+= str(df0.columns.values[i]) + ": " + str(pok.values[i]) +"\n"
                lbl.config(text= str(k))
    except :
       lbl.config(text="Veuillez faire une action ou faire minimum trois recherches")

def pokemon ():
    root=Tk()
    root.title("Pokemon")
    root.iconbitmap("pokeball.ico")
    #label
    label1=Label(root,text="Recherche")
    label1.grid(column=0, row=0)
    label2=Label(root,text="Resultat")
    label2.grid(column=1, row=0)
    #zone de recherche
    Recherche_pok=StringVar(root)
    entry_pok=Entry(root,textvariable=Recherche_pok)
    entry_pok.grid(column=0, row=1)
    labelResultat = Label(root, text="")
    labelResultat.grid(row=2, column=1)

    # radiobutton

    fleg = Frame(root, bd=1, relief=SUNKEN)
    fleg.grid(row=3, column=0)
    lblleg0 = Label(fleg, text="Voulez vous que votre pokémon soit légendaire ?")
    lblleg0.grid(row=1, column=0)

    choixleg = StringVar(fleg, "choix leg")
    lblleg1 = Label(fleg, text="Oui")
    rtbtn1 = Radiobutton(fleg, variable=choixleg, value="Oui")
    lblleg1.grid(row=2, column=0)
    rtbtn1.grid(row=2, column=1)
    lblleg2 = Label(fleg, text="Non")
    rtbtn2 = Radiobutton(fleg, variable=choixleg, value="Non")
    lblleg2.grid(row=2, column=2)
    rtbtn2.grid(row=2, column=3)

    fpdv = Frame(root, bd=1, relief=SUNKEN)
    fpdv.grid(row=6, column=0)
    lblpdv0 = Label(fpdv, text="Quelle intervalle de pdv souhaitez vous ?")
    lblpdv0.grid(row=1, column=0)

    choixpdv = StringVar(fpdv, "choix pdv")
    lblpdv1 = Label(fpdv, text="Peu résistant entre 0 et 39")
    rtbtn3 = Radiobutton(fpdv, variable=choixpdv, value="Peu résistant")
    lblpdv1.grid(row=2, column=0)
    rtbtn3.grid(row=2, column=1)
    lblpdv2 = Label(fpdv, text="Moyennement résistant entre 40 et 79")
    rtbtn5 = Radiobutton(fpdv, variable=choixpdv, value="Moyennement résistant")
    lblpdv2.grid(row=3, column=0)
    rtbtn5.grid(row=3, column=1)
    lblpdv3 = Label(fpdv, text="Résistant entre 80 et 119")
    rtbtn6 = Radiobutton(fpdv, variable=choixpdv, value="Résistant")
    lblpdv3.grid(row=4, column=0)
    rtbtn6.grid(row=4, column=1)
    lblpdv4 = Label(fpdv, text="Très résistant plus de 120")
    rtbtn7 = Radiobutton(fpdv, variable=choixpdv, value="Très résistant")
    lblpdv4.grid(row=5, column=0)
    rtbtn7.grid(row=5, column=1)
    #dropbox
    fgen=Frame(root,bd=1, relief=SUNKEN)
    fgen.grid(row=4,column=0)
    lblgen=Label(fgen,text="Quelle Génération de Pokémon cherchez vous ?")
    lblgen.grid(row=0, column=0)
    list_gen = [str(x) for x in list(set(df0["Generation"].values))]
    list_gen.append("Je ne veux pas choisir")
    clickgen=StringVar()
    clickgen.set(list_gen[0])
    dropboxgen=OptionMenu(fgen,clickgen,*list_gen)
    dropboxgen.grid(row=0,column=1)

    ftype=Frame(root,bd=1,relief=SUNKEN)
    ftype.grid(row=5,column=0)
    lbltype=Label(ftype,text="Veuillez choisir le ou les types : ")
    lbltype.grid(row=0,column=0)
    list_type2 = [x for x in list(set(df0["Type 2"].values))]
    list_type2.append("Je ne veux pas choisir")
    list_type1 = [x for x in list_type2 if x != "Pas de type"]
    clicktyp1=StringVar()
    clicktyp1.set(list_type1[0])
    dropboxtyp1=OptionMenu(ftype,clicktyp1,*list_type1)
    dropboxtyp1.grid(row=1,column=0)
    clicktyp2 = StringVar()
    clicktyp2.set(list_type2[0])
    dropboxtyp2=OptionMenu(ftype,clicktyp2,*list_type2)
    dropboxtyp2.grid(row=1,column=1)




    #button
    btnrech=Button(root,text="Recherche")
    btnrech.grid(column=0,row=2)
    btnrech.config(command=partial(update_label_recherche,lbl=labelResultat,df=df0,name=Recherche_pok,c=choixleg,d=clickgen,e=clicktyp1,f=clicktyp2,g=choixpdv))

    root.mainloop()


#print(df0[(df0["Type 1"]=="Normal") & (df0["Legendary"]==True)])
#df1=rechercherlegendaire(df0,"")
#print(df1)
#df2=recherchergeneration(df1,5)
#print(df2)
pokemon()

