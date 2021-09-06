# ouverture du fichier en mode lecture 'r'

file= open('input/warning.txt','r')

# lecture du fichier ligne par ligne

suspect_lines=file.readlines()

# fermeture du fichier

file.close()

file= open('input/Utilisateurs.txt','r')

# lecture du fichier ligne par ligne

lines=file.readlines()

# fermeture du fichier

file.close()

#création de la liste des suspects
Liste_suspect=[]
for line2 in suspect_lines:
    # Pour retirer les retours chariots'\n' à la fin de chaque ligne

     
     Liste_suspect.append(line2.strip('\n'))

#c'est une ligne qui parcourt les ligne du fichier utilisateur

liste_des_connectés_IP_suspects=[]

for line in lines: 
    # split transforme un texte en liste à l'aide des séparateurs 
    line1=line.split(";") 
    ip=line1[0]

    for ip_suspect in  Liste_suspect:
        if ip==ip_suspect:
           liste_des_connectés_IP_suspects.append(line1[1])
        else:
            pass
print(liste_des_connectés_IP_suspects)       

# set permet d'enlever les doublons dans la liste afin de ne pas imprimer plusieurs fois le même texte

f = open('output/suspect.txt','w')

for nom in set(liste_des_connectés_IP_suspects):

    nombre_de_fois=liste_des_connectés_IP_suspects.count(nom)

    #\n pour passer à la ligne suivante à chaque écriture dans le fichier des suspects

    f.write("{},{}\n".format(nom,nombre_de_fois))

    print("{},{}".format(nom,nombre_de_fois))
f.close()
   

