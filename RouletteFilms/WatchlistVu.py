import random as rd

present = ['Clément','Déclan','Lucie','Naïa']

users = ['Clément','Déclan','Lucie','Naïa']
lalaou = []
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
        
    lalaou.append((vu_user, wl_user))


######################################################################################################################################################
# initialistion 
wl_commune = []
wl_communeVu = []
# trouve un utilisateur
for source_wl in range(len(lalaou)):
    for film_wl in lalaou[source_wl][1]:
        est_trouve = False
        user_id = 0
        # prend un utilisateur
        while est_trouve == False :
            if user_id == len(lalaou) :
                break
            id_film_vu = 0
            # parcours les films vu d'un user
            while est_trouve == False :
                if film_wl == lalaou[user_id][0][id_film_vu] :
                    est_trouve = True
                    break
                if id_film_vu == len(lalaou[user_id][0])-1 :
                    break
                id_film_vu += 1
            user_id += 1         
        if est_trouve == False : # si on a pas trouvée le film_wl dans les films vu d'un user
            wl_commune.append(film_wl)

for source_wl in range(len(lalaou)):
    for film_wl in lalaou[source_wl][1]:
        est_trouve = False
        user_id = 0
        # prend un utilisateur
        while est_trouve == False :
            if user_id == len(lalaou) :
                break
            id_film_vu = 0
            # parcours les films vu d'un user
            while est_trouve == False :
                if film_wl in wl_commune :
                    est_trouve = True
                    break
                if id_film_vu == len(lalaou[user_id][0])-1 :
                    break
                id_film_vu += 1
            user_id += 1         
        if est_trouve == False : # si on a pas trouvée le film_wl dans les films vu d'un user
            wl_communeVu.append(film_wl)

choix_final = rd.choice(list(wl_communeVu))
print(choix_final)