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
        frame_menu = tk.Frame(self.master)
        frame_menu.pack()
        main_text = tk.Label(frame_menu, text="title",bg="#253f4b")
        main_text.pack()
        play_button = tk.Button(frame_menu, text="Play")
        play_button.pack()
    
    def change_frame(self):
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

