import random as rd

# USERS
    # Récupération de WL et VU
    #Clément
users = ['Clément','Déclan','Lucie']
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
# initialistion 
wl_commune = set()

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
            wl_commune.add(film_wl)

choix_final = rd.choice(list(wl_commune))
print(choix_final)