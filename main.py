import tkinter as tk
from arbre import generate_values

class MainJeu:
    def __init__(self, master):
        # création de la fenêtre
        self.master = master
        self.master.title("jeu")
        self.master.geometry("1280x720")
        self.master.minsize(1024,768)
        self.master.config(background="#253f4b")
    
    def correct_label_size(self,texte,ratio):
        """ratio correspond au rapport taille du label par rapport à la resolution"""
        police_size = round((20*int(self.master.winfo_width()))/1920)
        test_label = tk.Label(text=texte,font=("Comic Sans MS", police_size, "bold"))
        test_label.pack()
        self.master.update()
        while test_label.winfo_width()>=(ratio*self.master.winfo_width()):
            test_label.pack_forget()
            police_size-=1
            test_label = tk.Label(text=texte,font=("Comic Sans MS", police_size, "bold"))
            test_label.pack()
            self.master.update()
        test_label.pack_forget()
        return police_size 
    
    def saut_ligne_efficace(self,texte,index_g, index_d):
        """Remet en forme le texte pour : qu'il puisse rentrer dans la fenêtre (s'adapte à la résolution) en rajoutant des sauts de ligne (\n); et qu'il est une taille lisible (min 10). 
        Cet algorithme récursif fonctionne sur un principe de dichotomie.
        index_g correspond au pointeur de gauche
        index_d correspond au pointeur de droite"""
        size = self.correct_label_size(texte,5/6)
        if size >=10:

            return texte, size 
        else:
            modif_g = False
            modif_d = False
            while modif_g == False or modif_d == False:
                if modif_g == False:
                    index_g -=1
                    if (texte[index_g] == "." or texte[index_g] == "!" or texte[index_g] == "?" or texte[index_g] == "," or texte[index_g] == ":" or texte[index_g] == " ")  and texte[index_g+1]!="\"" and texte[index_g+1]!=".":
                        texte = texte[:index_g+1] + "\n" + texte[index_g+1:]
                        modif_g=True
                if modif_d == False:
                    index_d +=1
                    if (texte[index_d] == "." or texte[index_d] == "!" or texte[index_d] == "?" or texte[index_d] == "," or texte[index_d] == ":" or texte[index_g] == " ")  and texte[index_d+1]!="\"" and texte[index_d+1]!=".":
                        texte = texte[:index_d+1] + "\n" + texte[index_d+1:]
                        modif_d=True
            return self.saut_ligne_efficace(texte,index_g//2,len(texte[index_d:])//2+index_d)

    def create_menu(self):
        self.frame_menu = tk.Frame(self.master)
        self.frame_menu.pack()
        main_text = tk.Label(self.frame_menu, text="Jeu à choix",bg="#253f4b", font=("Comic Sans MS", 20, "bold"))
        main_text.pack()
        play_button = tk.Button(self.frame_menu, text="Play", command=self.intro_play)
        play_button.pack()
    
    def intro_play(self):
        self.frame_menu.destroy()
        # intro
        self.frame_intro = tk.Frame(self.master)
        self.frame_intro.pack()
        raw_text = """Samedi 9 h 67 Yvette est debout devant son miroir, elle s'habille pour aller petit déjeuner. 
        Cependant, voila le problème, il lui manque du pain. 
        Ça fait maintenant 73 ans qu'Yvette mange du pain chaque matin, c'est pas aujourd'hui que ça va changer. 
        Mais il y a un hic, Yvette n'a plus toute sa tête, et c'est vous qui allez la guider jusqu'à la boulangerie."""
        intro_text = tk.Label(self.frame_intro, text=raw_text,bg="#253f4b", font=("Comic Sans MS", 18, "bold"),bd=1,relief="sunken")
        intro_text.pack()
        next_button = tk.Button(self.frame_intro, text="suivant", command=lambda:[self.frame_intro.destroy(),self.play(node)]) 
        next_button.pack()
        
    def play(self, cur_node):
        """fonction récursive"""
        if cur_node.gauche == None and cur_node.droit == None: # si fin
            self.frame_end = tk.Frame(self.master)
            self.frame_end.pack()
            self.text_end = tk.Label(self.frame_end, text="FIN",bg="#253f4b",font=("Comic Sans MS", 18, "bold"))
            self.text_end.pack()
        else:
            self.frame_play=tk.Frame(self.master)
            self.frame_play.pack()
            texte = cur_node.get_texte()
            label_size = self.correct_label_size(texte,5/6)
            if label_size<11: # texte trop grand pour rentrer dans la fenêtre, dichotomie en ajoutant un \n au milieu (milieu --> pas le vrai milieu mais un qui est en dehors d'un mot)
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
                texte,label_size = self.saut_ligne_efficace(texte,index_g//2,len(texte[index_d:])//2+index_d) # nouveau format texte et police optimale  
            self.texte = tk.Label(self.frame_play, text=texte,bg="#253f4b",font=("Comic Sans MS",label_size, "bold"))
            self.texte.pack()
            button_gauche = tk.Button(self.frame_play, text=cur_node.gauche.get_texte_choix(), command=lambda:[self.frame_play.destroy(),self.play(cur_node.get_gauche())])
            button_gauche.pack(side="left")
            button_droit = tk.Button(self.frame_play, text=cur_node.droit.get_texte_choix(), command=lambda:[self.frame_play.destroy(),self.play(cur_node.get_droit())])
            button_droit.pack(side="right")
    

def main():
    global node
    node = generate_values()  # génère l'arbre binaire
    root = tk.Tk()
    app = MainJeu(root)
    app.create_menu()
    root.mainloop()

if __name__ == '__main__':
    main()