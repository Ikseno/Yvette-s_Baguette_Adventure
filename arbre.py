class Arbre_bin:
    def __init__(self, val=None, type_noeud = 0, texte_choix = ""):
        # Type de noeud : 0 -> noeud de choix ; 1 -> noeud de fin ; 2 -> noeud de probabilité
        self.valeur=val
        self.gauche=None
        self.droit=None
        self.type_noeud = type_noeud
        self.texte_choix = texte_choix
        self.texte = ""
        
    def insert_gauche(self, valeur, type_noeud, texte_choix = ""):
        if self.gauche==None:
            self.gauche=Arbre_bin(valeur, type_noeud, texte_choix)
        else:
            arbre_gauche=Arbre_bin(valeur, type_noeud, texte_choix)
            arbre_gauche.gauche=self.gauche
            self.gauche=arbre_gauche
            
    def insert_droit(self,valeur, type_noeud, texte_choix = ""):
        if self.droit==None:
            self.droit=Arbre_bin(valeur, type_noeud, texte_choix)
        else:
            arbre_droit=Arbre_bin(valeur, type_noeud, texte_choix)
            arbre_droit.droit=self.droit
            self.droit=arbre_droit
            
    def set_texte(self, texte = ""):
        self.texte = texte
    
    def get_texte(self):
        return self.texte
    
    def get_texte_choix(self):
        return self.texte_choix

    def get_valeur(self):
        return self.valeur
    
    def get_droit(self):
        return self.droit
    
    def get_gauche(self):
        return self.gauche

    def hauteur(self):
        if self.droit==None and self.gauche==None:
            return 1
        elif self.droit==None:
            return 1+self.gauche.hauteur()
        elif self.gauche==None:
            return 1+self.droit.hauteur()
        return 1+max(self.droit.hauteur(),self.gauche.hauteur())
    
    def __str__(self):
        lignes=["" for i in range(self.hauteur()*2-1)]
        struct = self.structure(lignes,0)
        for i in struct:
            print(i)
        return ""
    
    def structure(self, lignes, rang):
        
        if self.droit==None and self.gauche==None:
            return [str(self.valeur)]
            
        if self.gauche==None:
            lignes_droit=self.droit.structure(lignes,rang+2)
            long=0
            while lignes_droit[0][long]==" ":
                long+=1
            long-=1
            
            for i in range(len(lignes_droit)):
                lignes_droit[i]=" "+" "*len(str(self.valeur))+lignes_droit[i]
            
            lignes=[str(self.valeur)+"_"*long," "*(long+len(str(self.valeur)))+" \\"]
            lignes+=lignes_droit

            liste_long=[]
            for j in lignes:
                liste_long.append(len(j))

            max_long=max(liste_long)
            
            for i in range(len(lignes)):
                lignes[i]=lignes[i]+(max_long-len(lignes[i]))*" "

        elif self.droit==None:
            lignes_gauche=self.gauche.structure(lignes,rang+2)
            long=0
            while lignes_gauche[0][-long-1]==" ":
                long+=1
            long-=1
            
            for i in range(len(lignes_gauche)):
                lignes_gauche[i]=lignes_gauche[i]+" "*len(str(self.valeur))+" "
            
            lignes=["_"*long+str(self.valeur),"/ "+" "*(long+len(str(self.valeur)))]
            lignes+=lignes_gauche

            liste_long=[]
            for j in lignes:
                liste_long.append(len(j))

            max_long=max(liste_long)
            
            for i in range(len(lignes)):
                lignes[i]=(max_long-len(lignes[i]))*" "+lignes[i]

        else:
            lignes_droit=self.droit.structure(lignes,rang+2)
            lignes_gauche=self.gauche.structure(lignes,rang+2)
            
            long_dr=0
            while lignes_droit[0][long_dr]==" ":
                long_dr+=1
            long_dr-=1

            long_ga=0
            while lignes_gauche[0][-long_ga-1]==" ":
                long_ga+=1
            long_ga-=1
            
            for i in range(len(lignes_droit)):
                lignes_droit[i]=" "+" "*len(str(self.valeur))+lignes_droit[i]
            
            lignes1=[str(self.valeur)+"_"*long_dr," "*(long_dr+len(str(self.valeur)))+" \\"]
            lignes1+=lignes_droit

            liste_long=[]
            for j in lignes1:
                liste_long.append(len(j))

            max_long=max(liste_long)
            
            for i in range(len(lignes1)):
                lignes1[i]=lignes1[i]+(max_long-len(lignes1[i]))*" "
            
            
            for i in range(len(lignes_gauche)):
                lignes_gauche[i]=lignes_gauche[i]+" "*len(str(self.valeur))+" "
            
            lignes2=["_"*long_ga+str(self.valeur),"/ "+" "*(long_ga+len(str(self.valeur)))]
            lignes2+=lignes_gauche

            liste_long=[]
            for j in lignes2:
                liste_long.append(len(j))

            max_long=max(liste_long)
            
            for i in range(len(lignes2)):
                lignes2[i]=(max_long-len(lignes2[i]))*" "+lignes2[i]

            maxi=max(len(lignes1),len(lignes2))
            mini=min(len(lignes1),len(lignes2))


            lignes=[]
            for i in range(mini):
                lignes.append(lignes2[i][:-len(str(self.valeur))]+lignes1[i])

            if maxi==len(lignes1):
                for i in range(mini,maxi):
                    lignes.append(len(lignes2[0])*" "+lignes1[i][len(str(self.valeur)):])
            else:
                for i in range(mini,maxi):
                    lignes.append(lignes2[i][:-len(str(self.valeur))]+len(lignes1[0])*" ")

        return lignes

def generate_values():
    node_0 = Arbre_bin(0, 0)
    node_0.set_texte("Vous vous dirigez péniblement vers la porte d'entrée, mais avant de sortir, vous jugez préférable de prendre quelque chose ...")
    node_0.insert_gauche(1, 0 , "Prendre une canne")
    node_0.insert_droit(2, 0, "Prendre un foulard")

    node_1 = node_0.get_gauche()
    node_1.set_texte("Votre bonne vieille canne ! Voila ce qui vous manquait. Votre cardialogue vous en remercie. Après avoir bien fermé la porte, vous avancez dans la Grand'Rue. Cependant, après quelques minutes, vous vous rendez compte que vous êtes à découvert. Décidement, Yvette est très tête en l'air... Alors que vous continuez votre chemin en maudissant le système Capitaliste, vous apercevez un banc. ")
    node_1.insert_gauche(3, 0 , "S'asseoir")
    node_1.insert_droit(4, 0, "Continuer")

    node_2 = node_0.get_droit()
    node_2.set_texte("")
    node_2.insert_gauche(5, 0 , "")
    node_2.insert_droit(6, 0, "")

    node_3 = node_1.get_gauche()
    node_3.set_texte("Ah ... Un pause s'impose. Pendant que vous réfléchissiez à une façon de trouver de l'argent, un homme habillé de soie s'approche. Il semble avoir les poches bien remplies, et vous remarquez un portefeuille qui dépasse de sa poche arrière. Vous pourriez ... Je n'insinue rien mais le vol est une manière comme une autre de se faire de l'argent ...")
    node_3.insert_gauche(7, 2 , "Tenter de lui voler son portefeuille")
    node_3.insert_droit(8, 0, "Calmer ses pulsions cleptomanes")

    node_4 = node_1.get_droit()
    node_4.set_texte("Vous continuez à marcher, un peu d'exercice ne vous fera pas de mal. Au croisement d'une rue, vous entendez un homme crier, et vous voyez une femme courir en votre direction avec un portefeuille dans la main.")
    node_4.insert_gauche(9, 0 , "La laisser passer")
    node_4.insert_droit(10, 0, "La taper avec votre canne")

    node_5 = node_2.get_gauche()
    node_5.set_texte("Evidemment, votre foulard. Comment survivre dans le froid de l'hiver sans votre bon vieux châle ? Vous vérifiez avoir bien fermé la porte, et vous déambulez dans la rue en direction de la boulangerie. Après quelques minutes, vous êtes un peu essouflée, et vous décidez de prendre une pause sur un banc. Un homme habillé comme l'as de pique passe devant vous et vous regarde bizzarement.")
    node_5.insert_gauche(11, 0 , "Mettre le foulard autours de la tête")
    node_5.insert_droit(12, 0, "Loucher")

    node_7 = node_3.get_gauche()
    node_7.set_texte("")
    node_7.insert_gauche(15, 1 , "")
    node_7.insert_droit(16, 0, "")

    node_8 = node_3.get_droit()
    node_8.set_texte("Inspirer, Respirer. Voila, vous vous calmez, vous le laissez passer. Vous vous relevez et décidez de persister malgré le froid, le pain n'attend pas ! Après quelques minutes de marche, vous trouvez un billet dans un tas de terre à coté. Après avoir vérifié que personne ne vous a vu, vous prenez le billet et le rangez dans votre porte-monnaie. Cependant, il commence à faire vraiment froid, vous apercevez un tabac ouvert.")
    node_8.insert_gauche(17, 1 , "Rentrer à la maison")
    node_8.insert_droit(18, 0, "Se réfugier dans le tabac (le bâtiment)")

    node_9 = node_4.get_gauche()
    node_9.set_texte("Vous décidez de ne rien faire. Le pacifisme est une vertu. Alors qu'elle passe devant vous, un billet s'échappe du portefeuille.")
    node_9.insert_gauche(19, 1, "Prendre le billet")
    node_9.insert_droit(20, 1, "Le laisser par terre")

    node_10 = node_4.get_droit()
    node_10.set_texte("Vous décidez de taper la femme avec votre canne. On ne va pas laisser la jeunesse corrompue commettre des crimes sans rien dire, après tout. Elle lève les mains au niveau de la tête comme pour se protéger, et laisse donc tomber le portefeuille. Elle s'enfuit (après avoir reçu quelques coups tout de même). Vous voyez deux billets dépasser du portefeuille, vous le ramassez. Un homme arrive en courant.")
    node_10.insert_gauche(21, 0 , "Cacher le portefeuille")
    node_10.insert_droit(22, 0, "Lui tendre le portefeuille")

    node_11 = node_5.get_gauche()
    node_11.set_texte("Vous enroulez le foulard autours de votre tête et le fixez. Il semble embété, et commence à fouiller dans son sac. Puis, il vous tend un billet. Vous ressemblez visiblement beaucoup à une mendiante avec votre foulard.")
    node_11.insert_gauche(23, 2 , "Décliner")
    node_11.insert_droit(24, 0, "Accepter")

    node_12 = node_5.get_droit()
    node_12.set_texte("Vous commencez à fixer l'homme en louchant. Il semble intrigué et s'arrète. Il vous observe quelques secondes, puis s'avance vers vous. Il vous dis qu'il a un 'deal' à vous proposer. Vous devez vendre des petits sachets de 'farine' à des jeunes, contre un billet chacun. Il vous prévient cependant que de deux policiers en civils se sont incrustés dans la foule de jeunes.")
    node_12.insert_gauche(25, 1 , "Refuser et prévenir la police")
    node_12.insert_droit(26, 2, "Accepter")

    node_15 = node_7.get_gauche()
    node_15.set_texte("Oups, vous ratez et lui mettez une main au c*l. Il se retourne brusquement et vous surprend la main dans le sac (ou plutôt dans la poche). Il se met à vous crier dessus dans la rue. Quelle humiliation... Devant tout le monde en plus. Vous ne pourrez plus sortir dans la rue après ça.")

    node_16 = node_7.get_droit()
    node_16.set_texte("Hop là,  vous récupérez en toute discrétion le magot. Après tout, avec votre expérience, ce n'est pas un petit larcin qui vous perdra. Fière de votre petit butin, vous arrivez devant la boulangerie. Vous remarquez qu'un nouveau boulanger a ouvert. Juste devant la boulangerie de Mme Phillipe en plus !")
    node_16.insert_gauche(33, 0 , "Aller chez le nouveau boulanger")
    node_16.insert_droit(34, 0, "Aller chez cette bonne vieille Mme Phillipe")

    node_17 = node_8.get_gauche()
    node_17.set_texte("Vous rentrez chez vous. Cependant, en fermant la porte, vous avez la sensation d'avoir oublié quelque chose... Le pain évidemment ! Votre tête vous fait défaut ! En plus, la boulangerie va bientôt fermer, vous n'evez pas le temps d'y retourner.")

    node_18 = node_8.get_droit()
    node_18.set_texte("décidez d'y rentrer. Après tout le pain peut attendre. En entrant, vous voyez le buraliste ranger des tickets de grattage")
    node_18.insert_gauche(37, 2 , "Acheter un ticket de grattage")
    node_18.insert_droit(38, 1, "Aller à la boulangerie")

    node_19 = node_9.get_gauche()
    node_19.set_texte("Vous récupérez le billet, et un homme arrive en courant vers vous. Il vous passe devant et ne semble même pas vous remarquer. Vous continuez votre chemin et arrivez à la boulangerie. Vous achetez une baguette")

    node_20 = node_9.get_droit()
    node_20.set_texte("Un homme arrive essouflé. Il s'arrête devant vous et ramasse le billet. Il continue sa course. Vous arrivez finalement à la boulangerie, mais vous n'avez pas d'argent. Vous êtes obligée de rentrer bredouille.")

    node_21 = node_10.get_gauche()
    node_21.set_texte("L'homme continue à courir et semble ne même pas vous voir. Vous vous félécitiez de votre petit butin, lorsque vous arrivez devant la boulangerie. Vous remarquez qu'un nouveau boulanger a ouvert. Juste devant la boulangerie de Mme Phillipe en plus !")
    node_21.insert_gauche(43, 0 , "Aller chez le nouveau boulanger")
    node_21.insert_droit(44, 1, "Aller chez cette bonne vieille Mme Phillipe")

    node_22 = node_10.get_droit()
    node_22.set_texte("lorsqu'il arrive à votre niveau, vous lui tendez le portefeuille. Il vous gratifie d'un grand sourire. Pour vous remercier de votre honnêteté, il vous propose de vous offrir un truc à boire au café du coin.")
    node_22.insert_gauche(45, 0 , "Accepter")
    node_22.insert_droit(46, 1, "Refuser poliment")

    node_23 = node_11.get_gauche()
    node_23.set_texte("Comment déclinez vous ?")
    node_23.insert_gauche(47, 1 , "L'insulter")
    node_23.insert_droit(48, 0, "Refuser poliement")

    node_24 = node_11.get_droit()
    node_24.set_texte("Ahh, il faut profiter des bonnes occasions (et des bonnes poires surtout). Vous acceptez son billet, et après quelques secondes, vous repartez en direction de la boulangerie avec votre argent durement gagné. Sur le chemin, vous vous faites accoster par des enfants qui vous font les yeux doux. Ils vous demandent de leur prêter votre foulard pour jouer à la corde à sauter.")
    node_24.insert_gauche(49, 1 , "Refuser")
    node_24.insert_droit(50, 0, "Accepter")

    node_25 = node_12.get_gauche()
    node_25.set_texte("Vous n'êtes pas dupe. Non non non, on vous la fait pas à vous. Vous savez que la farine est probablement périmée. Vous appelez un policier qui passait par là, qui arrête directement le vaurien. Vous devenez réputée auprès du quartier comme une justicière masquée qui combat le mal (et le trafic farine périmée)")

    node_26 = node_12.get_droit()
    node_26.set_texte("")
    node_26.insert_gauche(53, 1 , "tomber sur un policier")
    node_26.insert_droit(54, 0, "tomber sur un jeune")

    node_33 = node_16.get_gauche()
    node_33.set_texte("Vous décidez de faire profiter la concurrence. On peut faire de bonnes découvertes. En poussant la porte de la boulangerie, vous êtes accueillie par un regard accusateur. Le boulanger vous dit : Je vous ai vu faire, ça ne se fait pas de voler. Je ne vend pas aux fripouilles. Sortez de mon magasin !")
    node_33.insert_gauche(67, 0 , "Sortir un livre de loi")
    node_33.insert_droit(68, 2, "Le menacer avec votre canne")

    node_34 = node_16.get_droit()
    node_34.set_texte("Ah, le rictus de cette bonne vieille Mme Phillipe vous manque, c'est ça ? En poussant la porte, cette dernière vous accueille avec un grand sourire. Elle vous informe qu'actuellement, la clientèle se fait rare. Pour se démarquer de la concurrence, elle a mis en, place une offre choc ! Elle vous offre un pain, même si vous n'achetez rien")
    node_34.insert_gauche(69, 2, "Prendre le pain gratuit et garder son argent")
    node_34.insert_droit(70, 2, "Prendre le pain et en acheter un autre")

    node_37 = node_18.get_gauche()
    node_37.set_texte("")
    node_37.insert_gauche(75, 1 , "")
    node_37.insert_droit(76, 1, "")

    node_38 = node_18.get_droit()
    node_38.set_texte("Vous vous rendez à la boulangerie et achetez une baguette de pain.")

    node_43 = node_21.get_gauche()
    node_43.set_texte("Vous décidez de faire profiter la concurrence. On peut faire de bonnes découvertes. En poussant la porte de la boulangerie, vous êtes accueillie par un regard accusateur. Le boulanger vous dit : Je vous ai vu faire, ça ne se fait pas de voler. Je ne vend pas aux fripouilles. Sortez de mon magasin !")
    node_43.insert_gauche(87, 2 , "Le soudoyer en payant deux fois plus cher")
    node_43.insert_droit(88, 1, "Aller chez Mme Phillipe")

    node_44 = node_21.get_droit()
    node_44.set_texte("Vous ouvrez la porte de la boulangerie de madame Phillipe, mais cette dernière vous lance un regard haineux. Elle affirme vous avoir vu et refuse de vous vendre du pain. Vous rentrez chez vous sans pain, et probablement avec une mauvaise réputation")

    node_45 = node_22.get_gauche()
    node_45.set_texte("Vous accepter, et vous vous rendez ensemble au café du coin. Vous discutez pendant de longues heures et vous vous découvrez des passions communes. Vous gardez contact et continuez à vous voir fréquemment. Vous vous êtes fait un bon ami.")

    node_46 = node_22.get_droit()
    node_46.set_texte("Il semble un peu embarrassé, et vous offre quand même 2 billets que vous ne pouvez pas refuser. Vous vous rendez à la boulangerie de Mme Phillipe, et vous envisagez d'acheter 2 baguettes.")
    node_46.insert_gauche(93, 1 , "Acheter une baguette")
    node_46.insert_droit(94, 1, "Acheter deux baguettes")

    node_47 = node_23.get_gauche()
    node_47.set_texte("Vous lui dites 'Feur, flop, ratio, csc'. L'homme impressionné par votre répartie repart en pleurant. Mais il repart avec son argent. Vous arrivez donc à la boulangerie. La boulangère vous demande 'Vous voulez quoi ?', vous lui répondez 'feur' et partez")

    node_48 = node_23.get_droit()
    node_48.set_texte("Vous commencez à rougir de honte et lui dites que vous ne faites pas la manche, que vous avez juste un peu froid. L'homme se confond en excuse, et il vous propose de vous offrir deux billets pour s'excuser. Vous acceptez (le pauvre petit vous fait trop de peine), et vous vous rendez à la boulangerie. Vous avez donc deux billets, et vous vous dites que vous pourriez acheter deux baguettes au lieu d'une (profiter que vous soyez déjà à la boulangerie pour faire les stocks de la semaine).")
    node_48.insert_gauche(97, 1 , "Acheter une baguette")
    node_48.insert_droit(98, 1, "Acheter deux baguettes")

    node_49 = node_24.get_gauche()
    node_49.set_texte("C'est pas des mioches qui vont vous séparer de votre bon vieux foulard. Non mais ho ! En plus il fait froid. On dirait qu'ils veulent vous faire mourir de froid. Vous vous rendez à la boulangerie et achetez une baguette de pain (pain de campagne).")

    node_50 = node_24.get_droit()
    node_50.set_texte("Ooh, ces petits bouts de choux vous font de la peine. Vous leur donnez votre foulard, et ils repartent en courant, tout guillerets. Vous continuez votre route avec le sourir au lèvres. Cependant, vous sentez le temps se refroidir, et préferez rentrer dans un tabac que vous voyez ouvert. En rentrant, vous voyez le buraliste ranger des jeux d'argent dans une étagère.")
    node_50.insert_gauche(101, 2 , "Acheter un ticket à gratter")
    node_50.insert_droit(102, 1, "Se réchauffer et repartir")

    node_53 = node_26.get_gauche()
    node_53.set_texte("Pas de bol. L'homme est un policier en civil, il vous interroge sur le contenu de ce que vous vendez. Même si vous affirmez qu'il s'agit simplement de farine, il vous place quand même en garde à vue.")

    node_54 = node_26.get_droit()
    node_54.set_texte("Il s'agit d'un jeune, qui accepte d'acheter votre farine.")
    node_54.insert_gauche(109, 1 , "Arrêter la vente et aller à la boulangerie")
    node_54.insert_droit(110, 0, "Continuer à vendre")

    node_67 = node_33.get_gauche()
    node_67.set_texte("Vous fouillez votre sac et sortez un exemplaire du Code de la consommation. Vous feuilletez le large livre jusqu'à trouver l'article L121-11 que vous commencez à lire : Est interdit le fait de refuser à un consommateur la vente d'un produit ou la prestation d'un service... L'homme vous répond : ça va ça va, j'ai compris, je vais vous le vendre votre pain")
    node_67.insert_gauche(135, 2 , "Poursuivre le boulanger en justice")
    node_67.insert_droit(136, 2, "Acheter le pain")

    node_68 = node_33.get_droit()
    node_68.set_texte("Vous commencez à soulever votre canne et à esquisser votre plus belle grimace. Le boulanger cache son visage avec ses mains, et de peur, il vous tend une baguette en disant : wo wo wo, prenez-le votre pain ! Je veux pas d'embrouille moi !")

    node_69 = node_34.get_gauche()
    node_69.set_texte("Vous prenez le pain gratuit et remerciez la boulangère.")

    node_70 = node_34.get_droit()
    node_70.set_texte("Vous jugez qu'acheter deux baguettes peut être intéressant, on ne peut pas louper l'occasion. Faites attention cependant, il faut mieux acheter le pain frais car il peut devenir mou si vous le stockez.")

    node_75 = node_37.get_gauche()
    node_75.set_texte("En grattant, vous découvrez que votre ticket est gagnant, vous avez gagné 1 000 000 d'euros !!!")

    node_76 = node_37.get_droit()
    node_76.set_texte("En grattant, vous découvrez que votre ticket est perdant. Vous n'avez plus d'argent, et vous rentrez chez vous bredouille.")

    node_87 = node_43.get_gauche()
    node_87.insert_gauche(175, 0 , "")
    node_87.insert_droit(176, 0, "")

    node_88 = node_43.get_droit()
    node_88.set_texte("Vous vous rendez chez Mme Phillipe, et achetez deux baguettes avec vos deux billets. Faites attention cependant, il faut mieux acheter le pain frais car il peut devenir mou si vous le stockez.")

    node_93 = node_43.get_droit()
    node_93.set_texte("Vous vous rendez chez Mme Phillipe (la boulangère), et achetez une baguettes.")

    node_94 = node_43.get_droit()
    node_94.set_texte("Vous vous rendez chez Mme Phillipe (la boulangère), et achetez deux baguettes avec vos deux billets. Faites attention cependant, il faut mieux acheter le pain frais car il peut devenir mou si vous le stockez.")

    node_97 = node_48.get_gauche()
    node_97.set_texte("Vous choisissez de n'acheter qu'une baguette. Vous pourrez faire meilleur usage de cet argent supplémentaire.")

    node_98 = node_48.get_droit()
    node_98.set_texte("Vous décidez d'acheter deux baguettes avec vos deux billets. Faites attention cependant, il faut mieux acheter le pain frais car il peut devenir mou si vous le stockez.")

    node_101 = node_50.get_gauche()
    node_101.set_texte("")
    node_101.insert_gauche(203, 1 , "")
    node_101.insert_droit(204, 1, "")

    node_102 = node_50.get_droit()
    node_102.set_texte("Vous restez quelques temps au chaud, puis vous repartez en direction de la boulangerie de Mme phillipe. Après avoir poussé la porte et dit boujour à Mme Phillipe, vous lui demandez une baguette (pain de campagne), et vous repartez avec votre pain.")

    node_203 = node_101.get_gauche()
    node_203.set_texte("En grattant, vous découvrez que votre ticket est gagnant, vous avez gagné 1 000 000 d'euros !!!")

    node_204 = node_101.get_droit()
    node_204.set_texte("En grattant, vous découvrez que votre ticket est perdant. Vous n'avez plus d'argent, et vous rentrez chez vous bredouille.")

    node_109 = node_54.get_gauche()
    node_109.set_texte("Vous décidez d'arrêter de vendre de la farine, sinon vous aller faire de la concurrence à la boulangerie de Mme Phillipe. En parlant de Mme Phillipe, vous vous rendez à sa boulangerie, et vous achetez une baguette.")

    node_110 = node_54.get_droit()
    node_110.set_texte("")
    node_110.insert_gauche(221, 1 , "Tomber sur un policier en civil")
    node_110.insert_droit(222, 0, "Tomber sur un jeune")

    node_135 = node_67.get_gauche()
    node_135.set_texte("Vous allez porter plainte au commissariat de la ville, la police arrête le boulanger. Plusieurs jours plus tard, un procès est ouvert, et vous l'emportez évidemment. Vous gagnez 13 Millions d'Euros de dédommagement, et vous déménagez dans une villa à Malte.")

    node_136 = node_67.get_droit()
    node_136.set_texte("Vous lui lancez un regard menaçant et lui dites : mouais, je vais vous l'acheter votre pain, mais vous avez pas intérêt à recommencer, hein !")

    node_175 = node_87.get_gauche()
    node_175.set_texte("Il accepte finalement de vous vendre pour deux billets, et vous lui faites promettre de n'en parler à personne.")

    node_176 = node_87.get_droit()
    node_176.set_texte("Il refuse, et vous demande de partir de sa boulangerie, à deux doigts de vous insulter. Dépitée, vous vous rendez chez Mme Phillipe. En poussant la porte, vous êtes acueillie par un regard agressif. Vous comprenez que, tout comme le nouveau boulanger, Mme Phillipe vous a vu faire. Décidement, on dirait que le sort vous en veut. Vous décidez alors de rentrer chez vous, sans pain ni réputation.")

    node_221 = node_110.get_gauche()
    node_221.set_texte("Pas de bol. L'homme est un policier en civil, il vous interroge sur le contenu de ce que vous vendez. Même si vous affirmez qu'il s'agit simplement de farine, il vous place quand même en garde à vue.")

    node_222 = node_110.get_droit()
    node_222.set_texte("Il s'agit d'un jeune, qui accepte d'acheter votre farine.")
    node_222.insert_gauche(445, 1 , "Arrêter la vente et aller à la boulangerie")
    node_222.insert_droit(446, 0, "Continuer à vendre")

    node_445 = node_222.get_gauche()
    node_445.set_texte("Vous décidez d'arrêter de vendre de la farine, sinon vous aller faire de la concurrence à la boulangerie de Mme Phillipe. En parlant de Mme Phillipe, vous vous rendez à sa boulangerie, et puisque vous avez obtenu deux billets, vous envisagez d'acheter deux baguettes plutôt qu'une (afin de faire un peu de stock.")
    node_445.insert_gauche(891, 1 , "Acheter une baguette")
    node_445.insert_droit(892, 1, "Acheter deux baguettes")

    node_446 = node_222.get_droit()
    node_446.set_texte("")
    node_446.insert_gauche(893, 1 , "Tomber sur un policier en civil")
    node_446.insert_droit(894, 1, "Tomber sur un jeune")

    node_891 = node_445.get_gauche()
    node_891.set_texte("Vous choisissez de n'acheter qu'une baguette. Vous pourrez faire meilleur usage de cet argent supplémentaire.")

    node_892 = node_445.get_gauche()
    node_892.set_texte("Vous décidez d'acheter deux baguettes avec vos deux billets. Faites attention cependant, il faut mieux acheter le pain frais car il peut devenir mou si vous le stockez.")

    node_893 = node_446.get_gauche()
    node_893.set_texte("Pas de bol. L'homme est un policier en civil, il vous interroge sur le contenu de ce que vous vendez. Même si vous affirmez qu'il s'agit simplement de farine, il vous place quand même en garde à vue.")

    node_894 = node_446.get_gauche()
    node_894.set_texte("Vous vendez votre troisième sachet de farine, et l'homme qui vous a proposé ce business revient vers vous. Il dit être très impressionné, et vous propose de rejoindre son gang. Vous devenez alors une des plus grande Baronne du trafic de farine en Europe.")
    return node_0


##for i in range(64):
##    if i%2==0:
##        print(f"node_{i} = node_{(i+1)//2-1}.get_droit()")
##    else:
##        print(f"node_{i} = node_{(i+1)//2-1}.get_gauche()")
##
##    print(f'node_{i}.set_texte("")')
##    
##    print(f'node_{i}.insert_gauche({2*i+1}, 0 , "")')
##    print(f'node_{i}.insert_droit({2*i+2}, 0, "")')
##
##    print("")