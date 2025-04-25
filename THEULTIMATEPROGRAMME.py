import random as rd
#initialisation
arret = False
gens = ['Naia','Clement','Declan','Lucie','Baguette']

##################################SOUS PROGRAMME#######################################################

def importationPresent( La ) :
    present = []

    for i in range(len(La)):
        user = La[i]  # Récupération du nom de l'utilisateur

        # Correction du chemin avec f-string
        file_path = f'Data/{user}/watched.csv'
        with open (str(file_path),'r') as infile :
            vu_brut_user = infile.readlines()
        vu_user = []
        del(vu_brut_user[0])
        for i in vu_brut_user :
            ligne = i.split(',')
            print(ligne[1],"CACACACACACACACA")
            film = ligne[1]
            vu_user.append(film)

        with open (f'Data/{user}/watchlist.csv','r') as infile :
            wl_brut_user = infile.readlines()
        wl_user = []
        del(wl_brut_user[0])
        for i in wl_brut_user :
            ligne = i.split(',')
            film = ligne[1]
            wl_user.append(film)
            
        present.append((vu_user, wl_user))
    return present

def importationPasPresent( PasLa ) :
    pasPresent = []
    for i in range(len(PasLa)):
        user = PasLa[i]  # Récupération du nom de l'utilisateur

        # Correction du chemin avec f-string
        file_path = f'Data/{user}/watched.csv'
        with open (str(file_path),'r') as infile :
            vu_brut_user = infile.readlines()
        vu_user = []
        del(vu_brut_user[0])
        for i in vu_brut_user :
            ligne = i.split(',')
            film = ligne[1]
            vu_user.append(film)

        with open (f'Data/{user}/watchlist.csv','r') as infile :
            wl_brut_user = infile.readlines()
        wl_user = []
        del(wl_brut_user[0])
        for i in wl_brut_user :
            ligne = i.split(',')
            film = ligne[1]
            wl_user.append(film)

        pasPresent.append((vu_user, wl_user))
    return pasPresent

def filmRandom( present ) :
    # initialistion 
    wl_commune = []

    # trouve un utilisateur
    for source_wl in range(len(present)):
        for film_wl in present[source_wl][1]:
            est_trouve = False
            user_id = 0
            # prend un utilisateur
            while est_trouve == False :
                if user_id == len(present) :
                    break
                id_film_vu = 0
                # parcours les films vu d'un user
                while est_trouve == False :
                    if film_wl == present[user_id][0][id_film_vu] :
                        est_trouve = True
                        break
                    if id_film_vu == len(present[user_id][0])-1 :
                        break
                    id_film_vu += 1
                user_id += 1         
            if est_trouve == False : # si on a pas trouvée le film_wl dans les films vu d'un user
                wl_commune.append(film_wl)
    return wl_commune

def watchlistCommune( present ):
    wl_commune = filmRandom( present )
    wl_commune_plusieur = []
    
    for film_wl_p in wl_commune : 
        cpt = 0    
        for film_p in wl_commune :
            if film_p == film_wl_p :
                cpt += 1
        if cpt >= 2 and film_wl_p not in wl_commune_plusieur :
            wl_commune_plusieur.append(film_wl_p)

    return wl_commune_plusieur

def dejaVu( present, pasPresent) :
    pasPresent = profilPasPresent
    wl_commune = filmRandom(profilPresent)
    ListeDeFilmDejaVu = []
    
    for i in range (len(pasPresent)) :
        for filmDejaVu in pasPresent[i][0] :
            if filmDejaVu in wl_commune and filmDejaVu not in ListeDeFilmDejaVu :
                        ListeDeFilmDejaVu.append(filmDejaVu)
        
    for i in range (len(ListeDeFilmDejaVu)) :    
        for i in range (len(profilPresent)):
            for filmVu in profilPresent[i][0]:
                if ListeDeFilmDejaVu[i] == filmVu :
                    ListeDeFilmDejaVu.pop(i)
            
    return ListeDeFilmDejaVu
##################################PROGRAMME############################################################
    
present = []
absent = []
for CACA in gens :
    pres = input(("Est ce que",CACA,"est là ? y/n"))
    if pres == "y" :
        present.append(CACA)
    else :
        absent.append(CACA)
profilPresent = importationPresent(present)

while (True) :
    prog = int(input("""1 film random
2 watchlist commune
3 Film déjà vu par un absent
Quelle programme? :"""))
    
    if prog == 1 :
        while (True) :
            print(rd.choice(filmRandom( profilPresent )))
            rep = input("Encore ? y/n")
            if rep == "n" :
                break
    if prog == 2 :
        while (True) :
            print(rd.choice(watchlistCommune( profilPresent )))
            rep = input("Encore ? y/n")
            if rep == "n" :
                break
    if prog == 3:
        profilPasPresent = importationPasPresent( absent )
        while (True) :
            print(rd.choice(dejaVu(profilPresent, profilPasPresent)))
            rep = input("Encore ? y/n")
            if rep == "n" :
                break
    
    reponse = input ("Changer de programme ?y/n")
    if reponse != "y" :
        print("Bye Bye <3")
        break
