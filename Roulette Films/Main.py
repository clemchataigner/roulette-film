import random as rd

# USERS
    # Récupération de WL et VU
    #Clément
users = ['Clément', 'Naïa', 'Déclan', 'Lucie']

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
    
    if user == 'Clément' :
        clement = (vu_user, wl_user)
        users.append(clement)
    elif user == 'Naïa' :
        naia = (vu_user, wl_user)
        users.append(naia)
    elif user == 'Déclan' :
        declan = (vu_user, wl_user)
        users.append(declan)
    else :
        lucie = (vu_user, wl_user)
        users.append(lucie)

######################################################################################################################################################
# initialistion 
wl_commune = set()

# trouve un utilisateur
for source_wl in users:
    # prend 1 film de la watchlist de source_wl
    for film_wl in source_wl[1]:
        est_trouve = False
        user_id = -1
        # prend un utilisateur
        while est_trouve == False :
            if user_id == len(users)-1 :
                break
            user_id += 1
            id_film_vu = -1        
            # parcours les films vu d'un user
            while est_trouve == False :
                id_film_vu += 1
                if film_wl == users[user_id][0][id_film_vu]:
                    est_trouve = True
                    break 
                if id_film_vu == len(users[user_id][0])-1 :
                    break

        if est_trouve == False : # si on a pas trouvée le film_wl dans les films vu d'un user
            wl_commune.add(film_wl)

choix_final = rd.choice(list(wl_commune))
print(choix_final)