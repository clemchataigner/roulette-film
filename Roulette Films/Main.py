import random as rd

# USERS
    # Récupération de WL et VU
    #Clément
with open ('Data/Clément/watched.csv','r') as infile :
    vu_brut_clement = infile.readlines()
vu_clement = []
del(vu_brut_clement[0])
for i in vu_brut_clement :
    ligne = i.split(',')
    film = ligne[1]
    vu_clement.append(film)

with open ('Data/Clément/watchlist.csv','r') as infile :
    wl_brut_clement = infile.readlines()
wl_clement = []
del(wl_brut_clement[0])
for i in wl_brut_clement :
    ligne = i.split(',')
    film = ligne[1]
    wl_clement.append(film)
clement = (vu_clement,wl_clement)

        #Naïa
with open ('Data/Naïa/watched.csv','r') as infile :
    vu_brut_naia = infile.readlines()
vu_naia = []
del(vu_brut_naia[0])
for i in vu_brut_naia:
    ligne = i.split(',')
    film = ligne[1]
    vu_naia.append(film)

with open ('Data/Naïa/watchlist.csv','r') as infile :
    wl_brut_naia = infile.readlines()
wl_naia = []
del(wl_brut_naia[0])
for i in wl_brut_naia :
    ligne = i.split(',')
    film = ligne[1]
    wl_naia.append(film)
naia = (vu_naia,wl_naia)

        # Déclan
with open ('Data/Déclan/watched.csv','r') as infile :
    vu_brut_declan = infile.readlines()
vu_declan = []
del(vu_brut_declan[0])
for i in vu_brut_declan :
    ligne = i.split(',')
    film = ligne[1]
    vu_declan.append(film)

with open ('Data/Déclan/watchlist.csv','r') as infile :
    wl_brut_declan = infile.readlines()
wl_declan = []
del(wl_brut_declan[0])
for i in wl_brut_declan :
    ligne = i.split(',')
    film = ligne[1]
    wl_declan.append(film)
declan = (vu_declan,wl_declan)

        #Lucie
with open ('Data/Lucie/watched.csv','r') as infile :
    vu_brut_lucie = infile.readlines()
vu_lucie = []
del(vu_brut_lucie[0])
for i in vu_brut_lucie :
    ligne = i.split(',')
    film = ligne[1]
    vu_lucie.append(film)

with open ('Data/Lucie/watchlist.csv','r') as infile :
    wl_brut_lucie = infile.readlines()
wl_lucie = []
del(wl_brut_lucie[0])
for i in wl_brut_lucie :
    ligne = i.split(',')
    film = ligne[1]
    wl_lucie.append(film)
lucie = (vu_lucie,wl_lucie)


users = [
    clement,naia,declan,lucie,
]

# Choix des participants
print("Qui n'est pas là ce soir ? 0 quand fini.")
PasLa = ''
while PasLa != '0' :
    PasLa = input()
    users.remove(PasLa)
print(users)


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