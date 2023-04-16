# -*- coding: utf-8 -*-

import tkinter as tk
from arbre import generate_values
from PIL import Image, ImageTk
from time import sleep
import threading
from random import randint, choices
from text_format import better_text
from course_poursuite import MiniJeuCourse
from braquage import MiniJeuBraquage

class MainJeu:
    """Classe principale du jeu"""
    def __init__(self, master):
        # création de la fenêtre
        self.master = master
        self.master.title("Yvette's Baguette Adventure")
        self.master.geometry("1280x800")
        self.master.minsize(1024,768)
        self.master.config(background="#253f4b")  

    def create_menu(self):
        """
        Méthode permettant la création du menu
        """
        # Création de la structure
        self.frame_menu = tk.Frame(self.master,bg="#253f4b")
        self.frame_menu.pack(expand=1,fill="both")
        self.canvas_menu = tk.Canvas(self.frame_menu, width=1280, height=800, background="#253f4b", highlightthickness=0)
        self.canvas_menu.pack()

        # Création images
        logo_image = (Image.open("image/Yvette's_Baguette_Adventure_logo.png")).resize((650,650), Image.LANCZOS)
        bg_image = (Image.open("image/bakery_bg.png")).resize((1280,1280), Image.LANCZOS)
        menu_image = (Image.open("image/menu_img.png")).resize((350,350), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(logo_image)
        self.bg = ImageTk.PhotoImage(bg_image) 
        self.menu_title = ImageTk.PhotoImage(menu_image) 
        
        # Affichage image
        self.canvas_menu.create_image(640,400, image=self.bg)
        self.canvas_menu.create_image(325,430,image=self.logo)
        self.canvas_menu.create_image(1010,150, image=self.menu_title)

        # Lignes
        self.canvas_menu.create_line(920,200,920,800, fill="white", width=3)
        self.canvas_menu.create_line(920,200,1280,200, fill="white", width=3)
       
        # Buttons
        play_button = tk.Button(self.frame_menu, text="Play", command=self.intro_play,width=25,height=4,bg="orange",activebackground="grey")
        self.play_button_window = self.canvas_menu.create_window(1000,280, anchor="nw", window=play_button)
        credits_button = tk.Button(self.frame_menu, text="Credits", command=self.credits_menu,width=25,height=4,bg="orange",activebackground="grey")
        self.credits_button_window = self.canvas_menu.create_window(1000,480, anchor="nw", window=credits_button)
        exit_button = tk.Button(self.frame_menu, text="Exit", command=self.master.destroy,width=25,height=4,bg="orange",activebackground="grey")
        self.exit_button_window = self.canvas_menu.create_window(1000,680, anchor="nw", window=exit_button)
    
    def credits_menu(self):
        """
        Méthode permettant la création de la rubrique crédits
        """
        self.frame_menu.destroy()
        # Création de la structure
        self.frame_credits = tk.Frame(self.master,bg="#253f4b")
        self.frame_credits.pack(expand=1,fill="both")
        self.canvas_credits = tk.Canvas(self.frame_credits, width=1280, height=800, background="#253f4b", highlightthickness=0)
        self.canvas_credits.pack()
        
        # Background
        bg_image = (Image.open("image/blue_orange_bg.jpg")).resize((1280,1280), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image) 
        self.canvas_credits.create_image(640,400, image=self.bg)

        # Yvette
        yvette_image = (Image.open("image/Yvette/Yvette_0.png")).resize((500,500), Image.LANCZOS)
        self.yvette = ImageTk.PhotoImage(yvette_image) 
        self.canvas_credits.create_image(1150,630, image=self.yvette)

        # Titre credits
        credits_image = (Image.open("image/credits_img.png"))
        self.credits_title = ImageTk.PhotoImage(credits_image) 
        self.canvas_credits.create_image(695,80, image=self.credits_title)

        ### Catégories ###
        
        # Histoire 
        self.canvas_credits.create_text(200,200,text="Histoire",font=("MS Sans Serif", 20, "bold"), fill="black")
        self.canvas_credits.create_text(560,200,text="Raphaël Fischer (~80%)  |",font=("MS Sans Serif", 20), fill="black")
        self.canvas_credits.create_text(840,200,text="Dorian Courcelle",font=("MS Sans Serif", 20), fill="black")

        # Arborescence
        self.canvas_credits.create_text(200,300,text="Arborescence",font=("MS Sans Serif", 20, "bold"), fill="black")
        self.canvas_credits.create_text(700,300,text="Raphaël Fischer",font=("MS Sans Serif", 20), fill="black")

        # Mini-Jeux
        self.canvas_credits.create_text(200,400,text="Mini-Jeux",font=("MS Sans Serif", 20, "bold"), fill="black")
        self.canvas_credits.create_text(682,380,text="Dorian Courcelle : Course poursuite, Braquage",font=("MS Sans Serif", 20), fill="black")
        self.canvas_credits.create_text(670,420,text="Raphaël Fischer : Dealer, Portefeuille, Ticket",font=("MS Sans Serif", 20), fill="black")

        # Menu et affichage des noeuds
        self.canvas_credits.create_text(200,500,text="Menu et affichage des noeuds",font=("MS Sans Serif", 20, "bold"), fill="black")
        self.canvas_credits.create_text(700,500,text="Dorian Courcelle",font=("MS Sans Serif", 20), fill="black")
        
        # Structure/logique
        self.canvas_credits.create_text(200,600,text="Structure/logique",font=("MS Sans Serif", 20, "bold"), fill="black")
        self.canvas_credits.create_text(580,600,text="Raphaël Fischer  |",font=("MS Sans Serif", 20,), fill="black")
        self.canvas_credits.create_text(800,600,text="Dorian Courcelle",font=("MS Sans Serif", 20,), fill="black")

        # Art 
        self.canvas_credits.create_text(200,700,text="Art",font=("MS Sans Serif", 20, "bold"), fill="black")
        self.canvas_credits.create_text(585,675,text="Dorian Courcelle  |",font=("MS Sans Serif", 20,), fill="black")
        self.canvas_credits.create_text(805,675,text="Raphaël Fischer",font=("MS Sans Serif", 20,), fill="black")
        self.canvas_credits.create_text(585,725,text="DALL-E  |",font=("MS Sans Serif", 20,), fill="black")
        self.canvas_credits.create_text(745,725,text="OpenGameArt",font=("MS Sans Serif", 20,), fill="black")

        # Button retourner au menu
        button_play_again = tk.Button(self.frame_credits, text="Retour au menu" ,height=3,command=lambda: [self.frame_credits.destroy(),self.create_menu()], bg="orange",activebackground="grey")
        self.button_play_again_window = self.canvas_credits.create_window(1000,680,anchor="nw", window=button_play_again)

    def intro_play(self):
        """
        Classe permettant l'affichage de l'introduction du jeu (Présentation d'Yvette et de son objectif...) et le lancement du jeu à l'appui d'un bouton
        """
        self.frame_menu.destroy()
        # Création de la structure
        self.frame_intro = tk.Frame(self.master,bg="#253f4b")
        self.frame_intro.pack(expand=1,fill="both")

        # Optimisation du texte
        raw_text = "Samedi 9 h 57 Yvette est debout devant son miroir, elle s'habille pour aller petit déjeuner. Cependant, voila le problème, il lui manque du pain. Ça fait maintenant 73 ans qu'Yvette mange du pain chaque matin, c'est pas aujourd'hui que ça va changer. Mais il y a un hic, Yvette n'a plus toute sa tête, et c'est vous qui allez la guider jusqu'à la boulangerie."
        text, text_size, width  = better_text(raw_text,self.master,self.frame_intro, 20, "orange", 5/6, True).get_info()
        
        # Création de la structure 2
        self.canvas_intro = tk.Canvas(self.frame_intro, width=1280, height=800, background="#253f4b", highlightthickness=0)
        self.canvas_intro.pack()

        # Background
        bg_image = (Image.open("image/blue_orange_bg.jpg")).resize((1280,1280), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image) 
        self.canvas_intro.create_image(640,400, image=self.bg)

        # Décors
        decors_img = (Image.open("image/lieux/Lieu_14.png")).resize((600,400), Image.LANCZOS)
        self.decors = ImageTk.PhotoImage(decors_img) 
        self.canvas_intro.create_image(640,240, image=self.decors)

        # Yvette
        yvette_image = (Image.open("image/Yvette/Yvette_0.png")).resize((500,500), Image.LANCZOS)
        self.yvette = ImageTk.PhotoImage(yvette_image) 
        self.canvas_intro.create_image(840,280, image=self.yvette)

        # Création du texte
        intro_text_label = tk.Label(self.frame_intro, text=text,bg="#253f4b", fg="orange",font=("MS Sans Serif",text_size),borderwidth=2, relief="ridge")
        self.intro_label_window = self.canvas_intro.create_window(200,480, anchor="nw", window=intro_text_label)
        
        # Création du bouton
        next_button = tk.Button(self.frame_intro, text="suivant",width=20,height=3,command=lambda:[self.frame_intro.destroy(),self.play(node)], bg="orange",activebackground="grey") 
        self.next_button_window = self.canvas_intro.create_window(600,650, anchor="nw", window=next_button)
        
    def play(self, cur_node, chosen_junkies = [], policiers = None):
        """Méthode récursive permettant le parcours dans les différents noeuds et l'affichage qui lui est relatif 
        --> affichage des noeuds de fin, noeuds d'animations, noeuds à choix ...
        """

        # On bind la fenêtre pour permettre une navigation parmis les choix plus fluide (appuyer sur la touche flèche
        # gauche du clavier séléctionne le choix de gauche par exemple)
        self.master.bind("<Left>", lambda event, a=cur_node: self.left_pressed(a))
        self.master.bind("<Right>", lambda event, a=cur_node, b = chosen_junkies, c = policiers: self.right_pressed(a, b, c))
            
        # Commentaire Raphaël : Ici tu peux utiliser l'attribut type_noeud, le noeud est une feuille <=> type_noeud=1
        if cur_node.get_type()==1: # si fin
            # Structure
            self.frame_end=tk.Frame(self.master, bg="#253f4b")
            self.frame_end.pack(expand=1,fill="both")

            # Optimisation du texte
            text, text_size, width = better_text(cur_node.get_texte()+ "\n\nFIN",self.master, self.frame_end, 12, "orange", 5/6, True).get_info()
           
            # Création de la structure 2
            self.canvas_end = tk.Canvas(self.frame_end, width=1280, height=800, background="#253f4b", highlightthickness=0)
            self.canvas_end.pack()

            # Background
            bg_image = (Image.open("image/blue_orange_bg.jpg")).resize((1280,1280), Image.LANCZOS)
            self.bg = ImageTk.PhotoImage(bg_image) 
            self.canvas_end.create_image(640,400, image=self.bg)

            # On affiche le lieu (s'il en existe un associé au noeud)
            if not cur_node.get_lieu() is None:
                img_lieu = (Image.open(f"image/lieux/Lieu_{cur_node.get_lieu()}.png").resize((600,400), Image.LANCZOS))
                self.lieu = ImageTk.PhotoImage(img_lieu) 
                self.canvas_end.create_image(640,240, image=self.lieu) 
            
            if not cur_node.get_victoire() is None:    
                # On affiche une Yvette
                if cur_node.get_victoire() == "win":
                    img_yvette = (Image.open(f"image/Yvette/Yvette_victory.png").resize((500,500), Image.LANCZOS))
                else:
                    img_yvette = (Image.open(f"image/Yvette/Yvette_lose.png").resize((500,500), Image.LANCZOS))
                
                self.yvette = ImageTk.PhotoImage(img_yvette) 
                self.canvas_end.create_image(choices([440,840]),280, image=self.yvette)

            # Création du texte
            end_text_label = tk.Label(self.frame_end, text=text,bg="#253f4b", fg="orange",font=("MS Sans Serif",text_size),borderwidth=2, relief="ridge")
            self.end_label_window = self.canvas_end.create_window(int(182800*(1/width)),480, anchor="nw", window=end_text_label) # adapte la position en fonction de la taille du texte

            # Buttons
            button_play_again = tk.Button(self.frame_end, text="Rejouer" , width=20, height=3, command=lambda: [self.frame_end.destroy(),self.create_menu()], justify="center", bg="orange",activebackground="grey")
            self.play_again_button_window = self.canvas_end.create_window(580,650, anchor="nw", window=button_play_again)
            
            
        # Commentaire Raphaël : j'ai ajouté un if pour déclencher les mini-jeux
        elif cur_node.get_type() == 0:
            # Structure
            self.frame_play=tk.Frame(self.master, bg="#253f4b")
            self.frame_play.pack(expand=1,fill="both")

            # Optimisation du texte
            text, text_size, width = better_text(cur_node.get_texte(),self.master, self.frame_play, 12, "orange", 5/6, True).get_info()
            
            # Création de la structure 2
            self.canvas_play = tk.Canvas(self.frame_play, width=1280, height=800, background="#253f4b", highlightthickness=0)
            self.canvas_play.pack()

            # Background
            bg_image = (Image.open("image/blue_orange_bg.jpg")).resize((1280,1280), Image.LANCZOS)
            self.bg = ImageTk.PhotoImage(bg_image) 
            self.canvas_play.create_image(640,400, image=self.bg)
            
            # On affiche le lieu (s'il en existe un associé au noeud)
            if not cur_node.get_lieu() is None:
                img_lieu = (Image.open(f"image/lieux/Lieu_{cur_node.get_lieu()}.png").resize((600,400), Image.LANCZOS))
                self.lieu = ImageTk.PhotoImage(img_lieu) 
                self.canvas_play.create_image(640,240, image=self.lieu)
            
            # On affiche une Yvette
            img_yvette = (Image.open(f"image/Yvette/Yvette_{cur_node.get_yvette()}.png").resize((500,500), Image.LANCZOS))
            self.yvette = ImageTk.PhotoImage(img_yvette) 
            self.canvas_play.create_image(choices([440,840]),280, image=self.yvette)
            
            # Création du texte
            play_text_label = tk.Label(self.frame_play, text=text,bg="#253f4b", fg="orange",font=("MS Sans Serif",text_size),borderwidth=2, relief="ridge")
            self.play_label_window = self.canvas_play.create_window(int(182800*(1/width)),480, anchor="nw", window=play_text_label) # adapte la position en fonction de la taille du texte

            # Buttons
            button_gauche = tk.Button(self.frame_play, text=cur_node.get_gauche().get_texte_choix(),height=3,command=lambda:[self.frame_play.destroy(),self.play(cur_node.get_gauche())], justify="center", bg="orange",activebackground="grey")
            self.button_gauche_window = self.canvas_play.create_window(300,650, anchor="nw", window=button_gauche)
            
            button_droit = tk.Button(self.frame_play, text=cur_node.get_droit().get_texte_choix(),height=3,command=lambda:[self.frame_play.destroy(),self.play(cur_node.get_droit(), chosen_junkies, policiers)], justify="center", bg="orange",activebackground="grey")
            self.button_droit_window = self.canvas_play.create_window(900,650, anchor="nw", window=button_droit)

        else: # Si l'issue du jeu est déterminée par un mini-jeu
            
            val = cur_node.get_valeur()

            if val == 7:
                
                # Mini-jeu du portefeuille (voir la classe MiniJeuPortefeuille)
                jeu_portefeuille = MiniJeuPortefeuille(self.master, self, cur_node)
                jeu_portefeuille.create_help_frame()
                
            elif val == 26:

                # Mini-jeu du dealer : première partie
                jeu_dealer = MiniJeuDealer(self.master, self, cur_node)
                jeu_dealer.create_help_frame()
                
            elif val == 110 or val == 446:
                
                # Mini-jeu du dealer : deuxième et troisième partie
                jeu_dealer = MiniJeuDealer(self.master, self, cur_node, chosen_junkies, policiers)
                jeu_dealer.begin_game()

            elif val == 101:

                # Mini-jeu du ticket avec 2 choix gagnants (car Yvette a un meilleur karma)
                jeu_ticket = MiniJeuTicket(self.master, self, cur_node, 2)
                jeu_ticket.create_help_frame()

            elif val == 37:
                
                # Mini-jeu du ticket avec 1 choix gagnant
                jeu_ticket = MiniJeuTicket(self.master, self, cur_node, 1)
                jeu_ticket.create_help_frame()

            elif val == 23 or val == 87:
  
                # L'issue du noeud est aléatoire
                if randint(0,1):
                    self.play(cur_node.get_droit())
                else:
                    self.play(cur_node.get_gauche())
            
            elif val == 28:

                # Mini-jeu : course poursuite
                jeu_course = MiniJeuCourse(self.master,self,cur_node,"tesla")
                jeu_course.create_help_frame()
            
            elif val == 59:

                # Mini-jeu : course poursuite (braquage)
                jeu_course = MiniJeuCourse(self.master,self,cur_node,"braquage")
                jeu_course.create_help_frame()

            elif val == 60:
                
                # Mini-jeu : braquage
                jeu_braquage = MiniJeuBraquage(self.master,self,cur_node)
                jeu_braquage.create_help_frame()


    def right_pressed(self, node, chosen_junkies, policiers):
        """
        Continue le jeu à choix depuis le fils droit de noeud, comme le ferait le bouton droit. Cette fonction ne
        se déclenche que lorsque le joueur appuie sur la flèche droite.
        :param node: Instance de la classe Arbre_bin correspondant au noeud actuel
        :param chosen_junkies: tuple contenant les ID des junkies qui ont déjà été choisis si le joueur a lancé
        le mini-jeu du dealer, None sinon
        :param policiers: tuple contenant les ID des junkies qui sont en fait des policiers en civils. si le
        joueur a lancé le mini-jeu du dealer, None sinon
        """

        # On vérifie que le noeud est bien un noeud de choix, car le bind ne doit fonctionner que lorsque le noeud
        # est un noeud de choix. On vérifie également que le noeud existe (pour éviter de créer des bugs lorsque le
        # joueur appuie sur les touches dans le menu ou dans les fenêtres de fin
        if not node is None and node.get_type() == 0:
            self.frame_play.destroy()
            self.play(node.get_droit(), chosen_junkies, policiers)

    def left_pressed(self, node):
        """
        Continue le jeu à choix depuis le fils droit de noeud, comme le ferait le bouton droit. Cette fonction ne
        se déclenche que lorsque le joueur appuie sur la flèche droite.
        :param node: Instance de la classe Arbre_bin correspondant au noeud actuel
        """
        
        # On vérifie que le noeud est bien un noeud de choix, car le bind ne doit fonctionner que lorsque le noeud
        # est un noeud de choix. On vérifie également que le noeud existe (pour éviter de créer des bugs lorsque le
        # joueur appuie sur les touches dans le menu ou dans les fenêtres de fin
        if node.get_type() == 0:
            self.frame_play.destroy()
            self.play(node.get_gauche())

class MiniJeuTicket:
    """
    Classe gérant le mini-jeu relatif aux noeuds 101 et 37, dans lequel Yvette doit gratter le bon cercle
    d'un ticket à gratter pour devenir millionnaire
    """
    

    def __init__(self, master, global_game, node, nb_winning_circle):
        """
        Constructeur de la classe
        
        :param master: La fenêtre du jeu
        :param global_game: Instance de la classe MainJeu correspondant au jeu à choix
        :param node: Noeud actuel du jeu à choix
        :param nb_winning_circle: Nombre de cercles gagnants (1 ou 2) selon le noeud depuis lequel a été lancé
        """
        
        self.node = node
        self.global_game = global_game
        self.master = master

        # On génère les cercles gagnants aléatoirement, dans un premier tempps, on génère le premier cercle
        self.winning_circle = [randint(0,4)]
        
        if nb_winning_circle == 2:

            # On s'assure que chaque cercle peut être gagnant et que les probabilités qu'un cercle soit gagnant
            # policier sont indépendantes du cercle
            winning_circle_2 = randint(0,3)
            if winning_circle_2 >= self.winning_circle[0]:
                winning_circle_2 += 1
                
            self.winning_circle.append(winning_circle_2)

    def create_help_frame(self):
        """
        Crée la frame qui explique le jeu au joueur, qui contient également le bouton pour démarrer le jeu
        """
        
        self.help_frame = tk.Frame(self.master)
        self.help_frame.pack()
        
        indications_1 = tk.Label(self.help_frame, text = "Vous venez d'acheter un ticket à gratter, dans lequel vous devez")
        indications_1.pack()
        
        indications_2 = tk.Label(self.help_frame, text = "gratter un seul des cercles en cliquant dessus. Bonne chance !")
        indications_2.pack()

        next_button = tk.Button(self.help_frame, text="Commencer", command = lambda : self.begin_game())
        next_button.pack()

    def begin_game(self):
        """
        Initialise le jeu en créant la fenêtre du jeu contenant le fond (le ticket) et les boutons
        """

        self.help_frame.destroy()
        
        self.frame_jeu = tk.Frame(self.master, bg="#253f4b")
        self.frame_jeu.pack()

        # On créé l'image du ticket à gratter, que l'on place dans un label pour l'afficher
        img_fond = Image.open("image/Mini_Jeu_Ticket/ticket_gratter.png").convert("RGBA")
        photo_img_fond=ImageTk.PhotoImage(img_fond)

        label_fond = tk.Label(self.frame_jeu, image = photo_img_fond)
        label_fond.image = photo_img_fond
        label_fond.pack()

        # On ouvre l'image du cercle non-gratté maintenant pour éviter de la charger à chaque création de bouton
        img_circle = Image.open("image/Mini_Jeu_Ticket/ticket_rond_0.png").convert("RGBA")
        photo_img_cricle=ImageTk.PhotoImage(img_circle)

        # On crée les 5 boutons
        for i in range(5):
            self.create_button_circle(photo_img_cricle, i in self.winning_circle, i)

    def create_button_circle(self, img_circle, is_winning, nb_button):
        """
        Crée le bouton d'un cercle (qui est en fait un label pour éviter de déclencher une animation lorsque le
        joueur clique dessus)
        
        :param img_circle: Photo-image du cercle (mise en paramètres pour éviter de le charger à nouveau
        :param is_winning: Booléen qui indique si le cercle est un choix gagnant
        """

        # On crée le label contenant l'image, et on le bind pour déclencher la fin de mini-jeu
        label = tk.Label(self.frame_jeu, bd = -2, highlightthickness = 0, image = img_circle)
        label.image = img_circle
        label.bind("<Button-1>", lambda _: self.clic(nb_button, is_winning))

        # On calcule les positions des boutons pour qu'il s'affichent comme ceci :

        #    ***   ***   ***
        #    ***   ***   ***
        #       ***   ***
        #       ***   ***
        
        x_pos = 0.195 + (nb_button % 3)*0.295 + (nb_button // 3)*0.148
        y_pos = 0.335 + (nb_button // 3)*0.4
        
        label.place(relx = x_pos, rely = y_pos, anchor = "c")

    def clic(self, nb_button, is_winning):
        """
        Déclenche une petite animation de la pièce qui gratte, puis continue le jeu à choix à partir du noeud
        correspondant au choix du joueur : si le joueur à gratté un cercle gagnant, il gagne le mini-jeu, et on
        relance alors le jeu à choix depuis le sous arbre droit de node. Si il a gratté un cercle perdant, il a
        perdu le mini-jeu et on relance le jeu à choix depuis le sous arbre gauche de node
        
        :param nb_button: int correspondant numéro associé au bouton (compris entre 0 et 4)
        :param is_winning: bool, True si le cercle est gagnant et False sinon
        """

        # On calcule les positions comme dans la méthode create_button_circle
        x_pos = 0.195 + (nb_button % 3)*0.295 + (nb_button // 3)*0.148
        y_pos = 0.335 + (nb_button // 3)*0.4

        # On charge le fond du cercle (0€ si le joueur a perdu et 1 000 000 si le joueur a gagné
        if is_winning:
            img_fond = Image.open("image/Mini_Jeu_Ticket/fond_gagnant.png").convert("RGBA")
        else:
            img_fond = Image.open("image/Mini_Jeu_Ticket/fond_perdant.png").convert("RGBA")

        # On créé un label inutile juste pour le détruire en début de boucle
        label_anim = tk.Label(self.master)
        label_anim.pack()

        # Animation de la pièce qui gratte
        for i in range(1,13):

            # On détruit le label d'animation ici pour mettre un délai entre la création de la dernière image de
            # l'animation et sa destruction pour que le joueur ait le temps de voir le résultat
            label_anim.destroy()

            # On crée une copie de l'image de fond pour y fusionner l'image de la pièce qui gratte
            img_anim = img_fond.copy()

            img_rond = Image.open(f"image/Mini_Jeu_Ticket/ticket_rond_{i}.png").convert("RGBA")
            img_anim.paste(img_rond,(0,0),img_rond)
            photo_img_anim=ImageTk.PhotoImage(img_anim)

            # On crée le label contenant l'image et on le place aux bonnes coordonnées
            label_anim = tk.Label(self.master, bd = -2, highlightthickness = 0, image = photo_img_anim)
            label_anim.image = photo_img_anim
            label_anim.place(relx = x_pos, rely = y_pos, anchor = "c")

            # On actualise la fenêtre pour afficher l'animation (sans cette ligne, l'animation se déroulera
            # entièrement et l'image ne s'affichera qu'après
            self.master.update_idletasks()
            
            sleep(0.1)

        # On met un petit délai pour que le joueur puisse voir le résultat
        sleep(2)

        # Fin du jeu
        label_anim.destroy()
        self.frame_jeu.destroy()

        # On relance le jeu à choix depuis le bon noeud
        if is_winning:
            self.global_game.play(self.node.get_gauche())
            
        else:
            self.global_game.play(self.node.get_droit())


class MiniJeuDealer:
    """
    Classe gérant le mini-jeu relatif aux noeuds 26, 110 et 446, dans lequel Yvette essaye de vendre de la
    'farine' à des junkies, tout en évitant les policiers en civil
    """
    

    def __init__(self, master, global_game, node, chosen_junkies = [], policiers = None):
        """
        Constructeur de la classe
        
        :param master: La fenêtre du jeu
        :param global_game: Instance de la classe MainJeu correspondant au jeu à choix
        :param node: Noeud actuel du jeu à choix
        :param chosen_junkies: tuple contenant les ID des junkies qui ont déjà été choisis (il est égal à [] au
        début du jeu car aucun junkie n'a alors été choisi)
        :param policiers: tuple contenant les ID des junkies qui sont en fait des policiers en civils. Si aucune
        valeur de policier n'est précisée, c'est que le jeu est lancé pour la première fois, donc il faut générer
        aléatoirement les deux policiers.
        """
        
        self.node = node
        self.global_game = global_game
        self.master = master
        self.chosen_junkies = chosen_junkies
        
        if policiers is None:
            
            # On génère l'ID du policier 1 (entre 0 et 7) et celle du policier 2 (entre 0 et 7 et différente de celle
            # du policier 1) 
            policier_1 = randint(0,7)
            policier_2 = randint(0,6) # On ne choisis qu'entre 0 et 6 car il n'y a que 7 ID différentes de policier_1

            # On s'assure que chaque Junkie peut être un policier et que les probabilités qu'un junkie soit un
            # policier sont indépendantes du junkie
            if policier_2 >= policier_1:
                policier_2 += 1
            # On obtient donc un nombre aléatoire entre 0 et 7 différent de policier_1
            self.policiers = [policier_1, policier_2]
            
        else:
            # Si policier n'est pas None, cela signifie que les deux policiers ont déjà été générés
            self.policiers = policiers

    def create_help_frame(self):
        """
        Crée la frame qui explique le jeu au joueur, qui contient également le bouton pour démarrer le jeu
        """
        
        self.help_frame = tk.Frame(self.master)
        self.help_frame.pack()
        
        indications_1 = tk.Label(self.help_frame, text = 'Vous devez essayer de vendre la "farine" aux junkies.')
        indications_1.pack()
        
        indications_2 = tk.Label(self.help_frame, text = "Pour cela, cliquez sur un junkie. Attention, deux policiers en civil se cachent dans la foule.")
        indications_2.pack()

        # Lorsque le bouton est cliqué, il faut d'abord détruire self.help_frame car le jeu peut être appelé
        # directement avec la méthode begin_game, sans passer par la méthode create_help_frame. Dans ce cas,
        # self n'aura pas d'attribut help_frame, on ne peut donc pas détruire la fenêtre au début de begin_game
        next_button = tk.Button(self.help_frame, text="Commencer", command = lambda : [self.help_frame.destroy(), self.begin_game()])
        next_button.pack()

    def begin_game(self):
        """
        Initialise le jeu en créant la fenêtre du jeu et les boutons avec les images de junkies
        """
        
        self.frame_jeu = tk.Frame(self.master, pady=80, bg="#253f4b")
        self.frame_jeu.pack()
        
        for i in range(8):

            # Les junkies qui ont déjà été choisis ne doivent pas être réaffichés (ils sont partis)
            if i not in self.chosen_junkies:
                self.create_button_junkie(i)

    def create_button_junkie(self,num_junkie):
        """
        Crée le bouton avec l'image du junkie d'ID num_junkie
        :param num_junkie: int correspondant à l'ID du junkie (compris entre 0 et 7)
        """

        # On ouvre l'image correspondant au num_junkie-ième junkie
        img = Image.open(f"image/Mini_Jeu_Dealer/junkie_{num_junkie}.png").convert("RGBA").resize((320,320))
        photo_img=ImageTk.PhotoImage(img)

        button = tk.Button(self.frame_jeu, image=photo_img, bd=-2, highlightthickness = 0, command = lambda : self.clic(num_junkie))
        button.image = photo_img

        # On place le bouton dans une grille pour qu'il soit aligné avec les autres et qu'il reste à sa place
        # même si d'autres boutons n'ont pas été placés (si ils représentent un junkie qui a déjà été choisi)
        button.grid(column = num_junkie%4, row = num_junkie//4)

    def clic(self, num_junkie):
        """
        Continue le jeu à choix à partir du noeud correspondant au choix du joueur : si le joueur à choisi un jeune,
        il gagne le mini-jeu, et on relance alors le jeu à choix depuis le sous arbre droit de node. Si il est
        tombé sur un policier, il a perdu le mini-jeu et on relance le jeu à choix depuis le sous arbre gauche de node
        :param num_junkie: int correspondant à l'ID du junkie (compris entre 0 et 7)
        """
        
        self.frame_jeu.destroy()

        if num_junkie in self.policiers:
            self.global_game.play(self.node.get_gauche())
            
        else:
            # On ajoute l'ID du junkie choisi à self.chosen_junkies pour que si le joueur décide de retenter sa
            # chance avec ce mini-jeu, le junkie qu'il a choisi ne réapparaisse pas parmi les junkies
            self.chosen_junkies.append(num_junkie)
            self.global_game.play(self.node.get_droit(), self.chosen_junkies, self.policiers)
            

class MiniJeuPortefeuille:
    """
    Classe gérant le mini-jeu relatif au noeud 7, dans lequel Yvette essaye de dérober le porte-monnaie
    d'un honnête homme
    """

    
    def __init__(self, master, global_game, node):
        """
        Constructeur de la classe
        :param master: La fenêtre du jeu
        :param global_game: Instance de la classe MainJeu correspondant au jeu à choix
        :param node: Noeud actuel du jeu à choix
        """
        
        self.node=node
        self.global_game=global_game
        self.master = master
        
    def create_help_frame(self):
        """
        Crée la frame qui explique le jeu au joueur, qui contient également le bouton pour démarrer le jeu
        """

        # Le jeu est séparé en 3 niveux de difficultés croissantes, level prend les valeurs :
        #   - 1 durant la première partie
        #   - 2 durant la deuxième partie
        #   - 3 durant la troisième partie
        #   - 4 lorsque le joueur à fini la troisième partie, donc lorsqu'il a gagné le mini-jeu
        #   - 0 dès que le joueur fait une erreur, donc lorsqu'il a perdu le mini-jeu
        self.level=1
        
        self.help_frame = tk.Frame(self.master)
        self.help_frame.pack()
        indications_1 = tk.Label(self.help_frame, text = "Vous devez essayer de voler le portefeuille de l'homme.")
        indications_1.pack()
        indications_2 = tk.Label(self.help_frame, text = "Pour cela, appuyer sur une touche du clavier lorsque le curseur arrive dans la partie rouge.")
        indications_2.pack()
        indications_2 = tk.Label(self.help_frame, text = "Vous devez réussir 3 fois avant que votre main n'aille trop loin.")
        indications_2.pack()
        next_button = tk.Button(self.help_frame, text="Commencer", command = lambda : self.begin_game())
        next_button.pack()
        
    def begin_game(self):
        """
        Lance le jeu en utilisant le module threading pour lancer les différents éléments en même temps
        """
        
        self.help_frame.destroy()
        
        lock = threading.Lock()

        # Lance le timer (représenté par une main qui avance progressivement vers le pantalon de l'homme)
        img_pantalon,img_main = self.create_frame_timer()
        timer = threading.Thread(target = self.avancer_main, args = (lock,img_pantalon, img_main))
        timer.start()

        # Lance le jeu (le premier niveau du jeu)
        img_cadre, img_cursor, img_red = self.create_frame_level()
        cursor = threading.Thread(target = self.game_level_1, args = (lock,img_cadre, img_cursor, img_red))
        cursor.start()

    def create_frame_timer(self):
        """
        Construit le cadre contenant le timer
        :returns: Les images de la main et du pantalon chargées au cours de la fonction
        """
        
        self.frame_timer=tk.Frame(self.master, width = 1280, height=150, bg="white")
        self.frame_timer.pack(side="bottom")

        # .convert("RGBA") permet de conserver la transparence des images
        img_main=Image.open("image/Mini_Jeu_Portefeuille/main_profil.png").convert("RGBA").resize((328,200))
        img_pantalon=Image.open("image/Mini_Jeu_Portefeuille/pantalon.png").convert("RGBA").resize((1280,200))
        
        return img_pantalon,img_main

    def create_frame_level(self):
        """
        Construit le cadre contenant l'interface du mini-jeu
        :returns: Les images du cadre, du curseur et du rectangle rouge chargées au cours de la fonction
        """
        
        self.frame_jeu=tk.Frame(self.master, width = 1280, height=650, bg="white")
        self.frame_jeu.pack(side="top")
        self.frame_jeu.place(relx=.5, rely=.4,anchor="center") # Permet de centrer l'interface au milieu de la fenêtre
        
        # .convert("RGBA") permet de conserver la transparence des images
        img_cadre=Image.open("image/Mini_Jeu_Portefeuille/cadre_jeu_portefeuille.png").convert("RGBA").resize((640,38))
        img_cursor=Image.open("image/Mini_Jeu_Portefeuille/cursor.png").convert("RGBA").resize((18,28))
        img_red=Image.open("image/Mini_Jeu_Portefeuille/rouge.png").convert("RGBA").resize((80,29))
        
        return img_cadre, img_cursor, img_red

    def avancer_main(self, lock, img, img_main):
        """
        Fait avancer la main sur le timer jusqu'à ce qu'il arriveau bout
        :param lock: Le lock qui permet de lancer le timer et le mini-jeu en même temps
        :param img: Image du pantalon (qui sert également de fond
        :param img_main: Image de la main de profil
        """

        # Le try permet d'éviter des erreurs lorsqu'un widget est détruit dans une autre fonction en parallèle
        try:
            i=1080 # Abscisse de la main, qui va de 1080 (droite de l'image) à 175 (à gauche de l'image, au niveau du pantalon)

            while i>175 and self.level>0:

                # Si le joueur a gagné le jeu, on arrête le mini-jeu et on relance le jeu à choix depuis le noeud 16
                if self.level==4:
                    self.frame_jeu.destroy()
                    self.frame_timer.destroy()
                    self.global_game.play(self.node.get_droit())
                    return

                lock.acquire()
                
                img_1=img.copy() # On copie l'image pour pouvoir modifier img_1 sans changer img
                img_1.paste(img_main, (i,0), img_main) # On fusionne les deux images en plaçant img_main sur img_1
                photo_img=ImageTk.PhotoImage(img_1)

                # On crée le Label qui contient photo_img
                label=tk.Label(self.frame_timer, image=photo_img, bd=-1)
                label.image=photo_img
                label.pack(side="left")
                
                lock.release()
                
                sleep(0.06) # On met un petit délai pour éviter que l'image clignote trop
                label.destroy()
                i-=2 # On réduite l'abscisse de la main pour la faire avancer
                
            # Si le joueur a perdu le jeu, on arrête le mini-jeu et on relance le jeu à choix depuis le noeud 15
            self.level = 0
            self.frame_jeu.destroy()
            self.frame_timer.destroy()
            self.global_game.play(self.node.get_gauche())
            
        except:
            pass

    def place_cursor_and_red(self,img_cadre, img_cursor, img_red, x_cursor, x_red):
        """
        Construit le cadre du jeu (en fusionnant le curseur et le rectangle rouge sur le cadre vide)
        :param img_cadre: Image du cadre vide
        :param img_cursor: Image du curseur
        :param img_red: Image du rectangle rouge
        :param x_cursor: Abscisse à laquelle le curseur doit être placé
        :param x_red: Abscisse à laquelle le rectangle rouge doit être placé
        :returns: Le label contenant le cadre du jeu avec tous ses éléments fusionnés
        """
        
        img_total=img_cadre.copy()
        img_total.paste(img_red, (x_red,5), img_red)
        img_total.paste(img_cursor, (x_cursor,5), img_cursor)
        photo_img=ImageTk.PhotoImage(image=img_total)
        
        label=tk.Label(self.frame_jeu, image=photo_img, bd=-1)
        label.image=photo_img
        
        return label
    
    def game_level_1(self, lock, img_cadre, img_cursor, img_red):
        """
        Lance la partie 1 du jeu (grand zone rouge immobile)
        :param lock: Le lock qui permet de lancer le timer et le mini-jeu en même temps
        :param img_cadre: Image du cadre vide
        :param img_cursor: Image du curseur
        :param img_red: Image du rectangle rouge
        """
        
        # Le try permet d'éviter des erreurs lorsqu'un widget est détruit dans une autre fonction en parallèle
        try:
            cursor_state=15 # Représente la vitesse à laquelle le curseur se déplace
            x=5 # Abscisse du curseur
            
            label=tk.Label(self.frame_jeu) # On initialise label ici car on a besoin de le détruire dans le while
            
            while self.level == 1: # Tant que le joueur n'a ni gagné ni perdu

                # label_bis contient le label qui va être packé, et label est le label actuellement packé
                # On crée donc le nouveau label dans une variable différente du label précédent, pour que le label
                # précédent reste affiché pendant l'exécution de place_cursor and_red
                label_bis = self.place_cursor_and_red(img_cadre, img_cursor, img_red, x, 280)

                # On remplace le label précédent et on pack le nouveau
                lock.acquire()
                label.destroy()
                label=label_bis
                label.pack(side="left")

                # On bind la fenêtre pour détecter lorsque le joueur appuie sur une touche
                self.master.bind("<Key>",lambda event : self.end_game(x+9,280,360))
                lock.release()
                
                sleep(0.015) # On met un petit délai pour éviter que le label clignote trop

                # On augmente / réduit l'abscisse du curseur selon cursor_state
                x+=cursor_state

                # Si le curseur arrive à l'une des extrémités, on inverse cursor_state pour que le curseur change de sens
                if x>=615 or x<=5:
                    cursor_state=-cursor_state

            # On ne sort de la boucle while que si le joueur gagne ou perd le mini-jeu, s'il perd, la fonction
            # avancer_main s'occupe d'arrêter le mini-jeu. Donc dans ce cas il suffit de quitter la fonction
            if self.level == 2:

                # Si le joueur gagne, il suffit de détruire le label et de lancer la partie 2 du mini-jeu
                label.destroy()
                self.game_level_2(lock, img_cadre, img_cursor, img_red)
        except:
            pass

    def game_level_2(self, lock, img_cadre, img_cursor, img_red):
        """
        Lance la partie 2 du jeu (grand zone rouge mobile)
        :param lock: Le lock qui permet de lancer le timer et le mini-jeu en même temps
        :param img_cadre: Image du cadre vide
        :param img_cursor: Image du curseur
        :param img_red: Image du rectangle rouge
        """

        # Le try permet d'éviter des erreurs lorsqu'un widget est détruit dans une autre fonction en parallèle
        try:
            cursor_state=15 # Représente la vitesse à laquelle le curseur se déplace
            x_cursor=5 # Abscisse du curseur
            red_state = -8 # Représente la vitesse à laquelle la zone rouge se déplace
            x_red = 555 # Abscisse de la zone rouge
            
            label=tk.Label(self.frame_jeu) # On initialise label ici car on a besoin de le détruire dans le while
            
            while self.level == 2: # Tant que le joueur n'a ni gagné ni perdu

                # label_bis contient le label qui va être packé, et label est le label actuellement packé
                # On crée donc le nouveau label dans une variable différente du label précédent, pour que le label
                # précédent reste affiché pendant l'exécution de place_cursor and_red
                label_bis = self.place_cursor_and_red(img_cadre, img_cursor, img_red, x_cursor, x_red)

                # On remplace le label précédent et on pack le nouveau
                lock.acquire()
                label.destroy()
                label=label_bis
                label.pack(side="left")
                
                # On bind la fenêtre pour détecter lorsque le joueur appuie sur une touche
                self.master.bind("<Key>",lambda event : self.end_game(x_cursor+9,x_red,x_red+80))
                lock.release()
                
                sleep(0.015) # On met un petit délai pour éviter que le label clignote trop

                # On augmente / réduit l'abscisse du curseur selon cursor_state
                x_cursor+=cursor_state
                # Si le curseur arrive à l'une des extrémités, on inverse cursor_state pour que le curseur change de sens
                if x_cursor>=615 or x_cursor<=5:
                    cursor_state=-cursor_state

                # On augmente / réduit l'abscisse de la zone rouge selon cursor_state
                x_red+=red_state
                # Si la zone rouge arrive à l'une des extrémités, on inverse cursor_state pour qu'elle change de sens
                if x_red>=555 or x_red<=5:
                    red_state=-red_state

            # On ne sort de la boucle while que si le joueur gagne ou perd le mini-jeu, s'il perd, la fonction
            # avancer_main s'occupe d'arrêter le mini-jeu. Donc dans ce cas il suffit de quitter la fonction
            if self.level == 3:
                
                # Si le joueur gagne, il suffit de détruire le label et de lancer la partie 2 du mini-jeu
                label.destroy()
                self.game_level_3(lock, img_cadre, img_cursor)
        except:
            pass

    def game_level_3(self, lock, img_cadre, img_cursor):
        """
        Lance la partie 2 du jeu (grand zone rouge mobile)
        :param lock: Le lock qui permet de lancer le timer et le mini-jeu en même temps
        :param img_cadre: Image du cadre vide
        :param img_cursor: Image du curseur
        """

        # Le try permet d'éviter des erreurs lorsqu'un widget est détruit dans une autre fonction en parallèle
        try:
            # On charge à nouveau le rectangle rouge pour réduire sa taille
            img_red=Image.open("image/Mini_Jeu_Portefeuille/rouge.png").convert("RGBA").resize((40,29))
            
            cursor_state=15 # Représente la vitesse à laquelle le curseur se déplace
            x_cursor=5 # Abscisse du curseur
            red_state = 12 # Représente la vitesse à laquelle la zone rouge se déplace
            x_red = 200 # Abscisse de la zone rouge
            
            label=tk.Label(self.frame_jeu) # On initialise label ici car on a besoin de le détruire dans le while
            
            while self.level == 3:
                # label_bis contient le label qui va être packé, et label est le label actuellement packé
                # On crée donc le nouveau label dans une variable différente du label précédent, pour que le label
                # précédent reste affiché pendant l'exécution de place_cursor and_red
                label_bis = self.place_cursor_and_red(img_cadre, img_cursor, img_red, x_cursor, x_red)

                # On remplace le label précédent et on pack le nouveau
                lock.acquire()
                label.destroy()
                label=label_bis
                label.pack(side="left")

                # On bind la fenêtre pour détecter lorsque le joueur appuie sur une touche
                self.master.bind("<Key>",lambda event : self.end_game(x_cursor+9,x_red,x_red+40))
                lock.release()
                
                sleep(0.015) # On met un petit délai pour éviter que le label clignote trop
                
                # On augmente / réduit l'abscisse de la zone rouge selon cursor_state
                x_cursor+=cursor_state
                # Si le curseur arrive à l'une des extrémités, on inverse cursor_state pour que le curseur change de sens
                if x_cursor>=615 or x_cursor<=5:
                    cursor_state=-cursor_state

                # On augmente / réduit l'abscisse de la zone rouge selon cursor_state
                x_red+=red_state
                # Si la zone rouge arrive à l'une des extrémités, on inverse cursor_state pour qu'elle change de sens
                if x_red>=595 or x_red<=5:
                    red_state=-red_state

            # On ne sort de la boucle while que si le joueur gagne ou perd le mini-jeu, s'il perd, la fonction
            # avancer_main s'occupe d'arrêter le mini-jeu. Donc dans ce cas il suffit de quitter la fonction
            if self.level==4:
                
                # Si le joueur gagne, on détruit le label et toutes les frames, la fonction avancer_main s'occupe
                # de continuer le jeu à choix
                label.destroy()
                self.frame_timer.destroy()
                self.frame_jeu.destroy()
        except:
            pass

    def end_game(self, pos, min_pos, max_pos):
        """
        Détecte si le joueur a gagné ou perdu lorsqu'il appuie sur une touche et change self.level en conséquence
        :param pos: Abscisse du centre du curseur
        :param min_pos: Abscisse de l'extrémité gauche de la zone rouge
        :param max_pos: Abscisse de l'extrémité droite de la zone_rouge
        """
        
        sleep(0.2) # On met un petit délai pour que le joueur puisse voir le résultat avant de passer au niveau suivant

        # Si le centre du curseur se trouve à l'intérieur de la zone rouge, on incrémente le niveau
        if pos<=max_pos and pos>=min_pos:
            self.level+=1

        # Sinon le joueur a perdu
        else:
            self.level=0

def main():
    global node
    node = generate_values()  # génère l'arbre binaire
    root = tk.Tk()
    root.minsize(1280,800)
    root.maxsize(1280,800)
    app = MainJeu(root)
    app.create_menu()
    root.mainloop()

if __name__ == '__main__':
    main()
