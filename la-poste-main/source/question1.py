# ouverture du fichier en mode lecture 'r'

file= open('input/Utilisateurs.txt','r')

# lecture du fichier ligne par ligne

Lines=file.readlines()

# fermeture du fichier

file.close()

for line in Lines:
     
     liste0=line.split(";")
       
     liste1=line.split(" ")
    # print(liste1[1])
     liste2=liste1[1].split(":")
     #print(liste2[0])
     heure=int(liste2[0])
     minute=int(liste2[1])
     if  8 <= heure <= 18:
            pass
    #les if et else sont juste liés au cas specifique ou l'heure = a 19h
     elif heure==19:
            
            if minute==0:
                pass
                
            else:
                print(liste0[0:2])
                
     else:
           
            print(liste0[0:2])
            
    
     



