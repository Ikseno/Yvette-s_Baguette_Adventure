import tkinter as tk
from arbre import Arbre_bin

class MainJeu:
    def __init__(self, master):
        # création de la fenêtre
        self.master = master
        self.master.title("jeu")
        self.master.geometry("1280x720")
        self.master.minsize(1024,768)
        self.master.config(background="#253f4b")
        self.arbre_choix = Arbre_bin()

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
        raw_text = """Samedi 9 h 67 \
        Yvette est debout devant son miroir, elle s'habille pour aller petit déjeuner. Cependant, voila le problème, il lui manque du pain. Ça fait maintenant 73 ans qu'Yvette mange du pain chaque matin, c'est pas aujourd'hui que ça va changer. Mais il y a un hic, Yvette n'a plus toute sa tête, et c'est vous qui allez la guider jusqu'à la boulangerie."""
        intro_text = tk.Label(self.frame_intro, text=raw_text,bg="#253f4b", font=("Comic Sans MS", 20, "bold"))
        intro_text.pack()
        next_button = tk.Button(self.frame_intro, text="suivant")
        next_button.pack()
        # ouvrir fonction recursive
        
    def play(self):
        """fonction récursive"""
        pass

    def dialogue(self):
        pass

    def choix(self):
        pass

def main():
    root = tk.Tk()
    app = MainJeu(root)
    app.create_menu()
    root.mainloop()

if __name__ == '__main__':
    main()

