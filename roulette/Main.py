import random as rd

users = ['Clement','Lucie']
PasLa = ['Declan','Naia']
present = []
for i in range(len(users)):
    user = users[i]  # Récupération du nom de l'utilisateur

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
        
    present.append((vu_user, wl_user))


######################################################################################################################################################
#Prog pour la wl commune de tout le monde

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

wl_commune_plusieur = []

for film_wl_p in wl_commune : 
    cpt = 0    
    for film_p in wl_commune :
        if film_p == film_wl_p :
            cpt += 1
    if cpt > 1 and film_wl_p not in wl_commune_plusieur :
        wl_commune_plusieur.append(film_wl_p) 

####################################################################################################################################
#Prog pour avoir un film dans la watchlist déja vu par quelqu'un

PasLa = ['Declan','Naia']
ListeDeFilmDejaVu = []

for i in range (len(PasLa)) :
    cpt = 0
    while(PasLa[i]!=users[cpt]) :
        cpt += 1
    for filmDejaVu in wl_commune : 
        for filmVuParPasLa in present[cpt][0] :
            if filmDejaVu == filmVuParPasLa :
                ListeDeFilmDejaVu.append(filmDejaVu)

####################################################################################################################################
print(ListeDeFilmDejaVu)
#choix_final = rd.choice(list(wl_commune))
#choix_final = rd.choice(list(wl_commune_plusieur))
#choix_final = rd.choice(list(ListeDeFilmDejaVu))

#print(choix_final)