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
        police_size = 20
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
            label_size = self.correct_label_size(texte,2/3)
            
            while label_size <=8:
                for index in range(len(texte)-1):
                    if (texte[index] == "." or texte[index] == "!" or texte[index] == "?" or texte[index] == "(")  and texte[index+1]!="\"" and texte[index+1]!=".":
                        texte = texte[:index+1] + "\n" + texte[index+1:]
                label_size = self.correct_label_size(texte,2/3)

            self.texte = tk.Label(self.frame_play, text=texte,bg="#253f4b",font=("Comic Sans MS",label_size, "bold"))
            self.texte.pack()
            button_gauche = tk.Button(self.frame_play, text=cur_node.gauche.get_texte_choix(), command=lambda:[self.frame_play.destroy(),self.play(cur_node.get_gauche())])
            button_gauche.pack(side="left")
            button_droit = tk.Button(self.frame_play, text=cur_node.droit.get_texte_choix(), command=lambda:[self.frame_play.destroy(),self.play(cur_node.get_droit())])
            button_droit.pack(side="right")
    

def main():
    global node
    node = generate_values()  # génère l'arbre bina
    root = tk.Tk()
    app = MainJeu(root)
    app.create_menu()
    root.mainloop()

if __name__ == '__main__':
    main()