from sqlite3 import *

fichier_bdd= "C:/Users/clemc/Desktop/UTC/TC02/INF2/TD/TD10/BDD-exo4.sqlite"
connexion = connect(fichier_bdd)
curseur = connexion.cursor()

curseur.execute('''Select c.nom, c.prenom FROM client as c JOIN numero_telephone as t ON c.id = t.client_id JOIN operateur as o ON t.operateur_id = o.id WHERE o.nom = 'SuperTelecom' ''')
for i in curseur :
    print(i)

curseur.execute('''Select c.nom, c.prenom FROM client as c JOIN numero_telephone as t ON c.id = t.client_id LEFT JOIN operateur as o ON t.operateur_id = o.id''')
for i in curseur :
    print(i)

curseur.execute('''INSERT INTO ville (nom, code_departement, code_postal) values ('Toulon', 83, 83000)''')

curseur.execute('''update numero_telephone set est_demarche = True WHERE numero = '03.11.22.33.44' ''')

curseur.execute('''update numero_telephone set operateur_id = 4 WHERE numero = '03.11.22.33.44' ''')

curseur.execute('''update numero_telephone set operateur_id = (SELECT id FROM operateur WHERE nom = 'SuperTelecom') WHERE numero = '03.11.22.33.44' ''')

curseur.execute('''DELETE FROM numero_telephone WHERE client_id = 1''')     #Sauf si cascade dans la base client NF92 t'a capté 
curseur.execute('''DELETE FROM client WHERE id = 1''')




connexion.commit()
curseur.close()
connexion.close()
