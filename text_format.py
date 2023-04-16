import tkinter as tk

class better_text:
    """
    Classe permettant un meilleur affichage du texte sur tkinter (centré et plus grande taille de police possible), fonctionne sur un principe de dichotomie et s'adapte en fonction de la résolution d'écran
    """
    def __init__(self, texte, master, frame, min_size, color, ratio, border=False):
            self.master = master
            self.frame = frame
            self.min_size = min_size
            self.color = color
            self.ratio = ratio
            self.border = border
            self.width = 0
            label_size, width = self.correct_label_size(texte,self.ratio)
            if label_size<self.min_size+1: # texte trop grand pour rentrer dans la fenêtre, dichotomie en ajoutant un \n au milieu (milieu --> pas le vrai milieu mais un qui est en dehors d'un mot)
                modif_g = False
                modif_d = False
                index_g = len(texte)//2
                index_d = int(index_g)
                while modif_g==False and modif_d==False:
                    if modif_g == False:
                        index_g -=1
                        if (texte[index_g] == "." or texte[index_g] == "!" or texte[index_g] == "?" or texte[index_g] == "," or texte[index_g] == ":" or texte[index_g] == " ")  and texte[index_g+1]!="\"" and texte[index_g+1]!=".":
                            texte = texte[:index_g+1] + "\n" + texte[index_g+1:]
                            modif_g=True
                    if modif_d == False:
                        index_d +=1
                        if (texte[index_d] == "." or texte[index_d] == "!" or texte[index_d] == "?" or texte[index_d] == "," or texte[index_d] == ":")  and texte[index_d+1]!="\"" and texte[index_d+1]!=".":
                            texte = texte[:index_d+1] + "\n" + texte[index_d+1:]
                            modif_d=True 
                self.better_texte,self.better_label_size, self.width = self.saut_ligne_efficace(texte,index_g//2,len(texte[index_d:])//2+index_d)
            else:
                self.better_texte,self.better_label_size, self.width = texte,label_size, width
    
    
    def correct_label_size(self,texte,ratio):
        """Méthode renvoyant la taille la plus optimisée du texte, sur l'écran, ratio correspond au rapport taille du label par rapport à la resolution"""
        police_size = (self.min_size//10)*round((20*int(self.master.winfo_width()))/1920)
        test_label = tk.Label(text=texte,font=("MS Sans Serif", police_size))
        test_label.pack()
        self.master.update()
        while test_label.winfo_width()>=(ratio*self.master.winfo_width()) and police_size>0:
            test_label.pack_forget()
            police_size-=1
            test_label = tk.Label(text=texte,font=("MS Sans Serif", police_size))
            test_label.pack()
            self.master.update()
        test_label.pack_forget()
        self.master.update()
        return police_size,test_label.winfo_width() 


    def saut_ligne_efficace(self,texte,index_g, index_d):
        """Remet en forme le texte pour : qu'il puisse rentrer dans la fenêtre (s'adapte à la résolution) en rajoutant des sauts de ligne (\n); et qu'il est une taille lisible (min 10). 
        Cet algorithme récursif fonctionne sur un principe de dichotomie.
        index_g correspond au pointeur de gauche
        index_d correspond au pointeur de droite"""
        size, width = self.correct_label_size(texte,self.ratio)
        if size >=self.min_size or (index_g<1 or index_d>len(texte)-1):
            return texte, size, width 
        else:
            modif_g = False
            modif_d = False
            while (modif_g == False or modif_d == False) and (index_g>1 and index_d<len(texte)-1):
                if modif_g == False:
                    index_g -=1
                    if texte[index_g] in (".","!","?",",",":") and texte[index_g+1]==" ":
                        texte = texte[:index_g+1] + "\n" + texte[index_g+1:]
                        modif_g=True
                    elif texte[index_g] == " ":
                        texte = texte[:index_g] + "\n" + texte[index_g+1:]
                        modif_g=True
                if modif_d == False:
                    index_d +=1
                    if texte[index_d] in (".","!","?",",",":"," ")  and texte[index_d+1]==" ":
                        texte = texte[:index_d+1] + "\n" + texte[index_d+1:]
                        modif_d=True
                    elif texte[index_d] == " ":
                        texte = texte[:index_d] + "\n" + texte[index_d+1:]
                        modif_d=True
            return self.saut_ligne_efficace(texte,int(0.8*(index_g//2)),int(1.2*(len(texte[index_d:])//2+index_d)))
        
    def get_info(self):
        """
        Permet de renvoyer le texte modifié (avec sauts de lignes en plus), sa taille optimale, et sa largeur sur l'écran 
        """
        return self.better_texte,self.better_label_size, self.width
    
    
    def get_label(self):
        """
        Renvoie directement le label optimal
        """
        if self.border:
            return tk.Label(self.frame, text=self.better_texte,bg="#253f4b", fg=self.color,font=("MS Sans Serif",self.better_label_size),borderwidth=2, relief="ridge")
        else:
            return tk.Label(self.frame, text=self.better_texte,bg="#253f4b", fg=self.color,font=("MS Sans Serif",self.better_label_size))