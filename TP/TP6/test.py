import sqlite3 as sq
import pandas as pd
 
#fonction pour ajouter un nouveau logeur dans la bdd
def new_logeur(nom,prenom,numero_rue,nom_rue,code_postal,ville):
    connection = sq.connect("BDD.sqlite") #connection à la base de données
    curseur = connection.cursor() #création d'un curseur
    query = f"""
            INSERT INTO logeur (nom, prenom, numero_rue, nom_rue, code_postal, ville)
            VALUES
            ('{nom}','{prenom}','{numero_rue}','{nom_rue}','{code_postal}','{ville}');
            """ #requête sql permettant d'ajouter un nouveau logeur
    curseur.execute(query) #exécution de la requête
    connection.commit() #enregistrement de la requête
    curseur.close() #fermeture de connection avec la bdd
    connection.close()
 
#fonction pour ajouter un nouveau logement dans la bdd
def new_log(numero_rue,nom_rue,code_postal,ville,label,nom,prenom,type_logement):
    #recherche en amont du logeur pour obtenir son id et l'ajouter dans la base
    connection=sq.connect("alesc.db")
    curseur = connection.cursor()
    query = f"""
            SELECT id_logeur FROM logeur WHERE prenom='{prenom}' AND nom='{nom}';
            """
    curseur.execute(query)
    id_logeur = curseur.fetchall()[0][0]
    curseur.close()
    #ajout du logement dans la db
    curseur = connection.cursor()
    query= f"""
            INSERT INTO logement (id_logeur,numero_rue,nom_rue,ville,code_postal,type,label)
            VALUES
            ('{id_logeur}','{numero_rue}','{nom_rue}','{ville}','{code_postal}','{type_logement}','{label}');
            """
    curseur.execute(query)
    connection.commit()
    curseur.close()
    connection.close()
 
#fonction pour ajouter un étudiant dans la bdd
def new_etu(nom,prenom,semestre,numero_rue,nom_rue,code_postal):
    #recherche en amont de l'id du logement habité en fonction de l'adresse
    connection=sq.connect("alesc.db")
    curseur = connection.cursor()
    query = f"SELECT id_logement FROM logement WHERE (numero_rue={int(numero_rue)} AND nom_rue='{nom_rue}' AND code_postal={int(code_postal)});"
    curseur.execute(query)
    id_logement = curseur.fetchall()[0][0]
    curseur.close
    #ajout de l'étudiant dans la db
    curseur = connection.cursor()
    query= f"""
            INSERT INTO etudiant (nom,prenom,semestre,id_logement)
            VALUES
            ('{nom}','{prenom}','{semestre}','{id_logement}');
            """
    curseur.execute(query)
    connection.commit()
    curseur.close()
    connection.close()
 
#fonction pour retrouver un étudiant dans la bdd en fonction de son logement
def get_etudiants(id_logement):
    connection=sq.connect("alesc.db") #connection à la base
    curseur=connection.cursor() #création du curseur
    query = f"""
            SELECT * FROM etudiant WHERE id_logement={int(id_logement)};
            """ #requête pour retrouver les étudiants en fonction de leur logement
    curseur.execute(query) #exécution de la requête
    etus = curseur.fetchall()
    curseur.close()
    etus_clean = [] #création de la liste qui sera retourné par la fonction
    #Boucle pour créer des dictionnaires, un dictionnaire correspondant à un étudiant
    for etu in etus:
        etu_clean={} #création du dictionnaire vide
        etu_clean["nom"]=etu[0] #ajout du nom
        etu_clean["prenom"]=etu[1] #ajout du prénom
        etu_clean["semestre"]=etu[2] #ajout du dictionnaire
        etus_clean.append(etu_clean) #ajout de l'étudiant dans la liste des étudiant du logement
    connection.close() #fermeture de la connection avec la bdd
    return etus_clean #on retourne la liste obtenue
 
#fonction pour retrouver le logements d'un logeur ainsi que ses occupants
def get_logements(nom_logeur,prenom_logeur):
    connection=sq.connect("alesc.db") #connection à la bdd
    curseur = connection.cursor() #création du curseur
    query = f"""
            SELECT id_logeur FROM logeur WHERE prenom='{prenom_logeur}' AND nom='{nom_logeur}';
            """ #requête SQL pour retrouver l'id du logeur qui nous permettra de retrouver les logements lui appartenant par la suite
    curseur.execute(query) #exécution de la requête
    id_logeur = curseur.fetchall()[0][0] #On est censés trouver un unique résultat, contenant une seule valeur que l'on récupère
    curseur.close()
    curseur=connection.cursor()
    query = f"""
            SELECT * FROM logement WHERE id_logeur={int(id_logeur)};
            """ #Requête pour retrouver tous les logements à partir de l'id logeur
    curseur.execute(query) #exécution de la requête
    logements = curseur.fetchall()
    curseur.close()
    logements_clean = [] #création de la liste contenant toutes les informations de chaque logements appartenant au logeur
    #Boucle pour créer des dictionnaires, un dictionnaire correspondant à un logement
    for logement in logements:
        logement_clean={} #création du dictionnaire vide
        logement_clean["numero_rue"]=logement[2] #ajout du numéro de rue du logement
        logement_clean["nom_rue"]=logement[3] #ajout du nom de la rue
        logement_clean["ville"]=logement[4] #ajout du nom de la ville
        logement_clean["code_postal"]=logement[5] #ajout  ajout du code postal
        logement_clean["type"]=logement[6] #ajout ajout du type de logement
        logement_clean["label"]="*"*int(logement[7]) #ajout ajout du label sous forme de nombre de caractère "*" et non d'entier pour une meilleure visualisation par l'utilisateur
        logement_clean["etu"]=get_etudiants(logement[0]) #ajout des information des étudiants habitant dans le logement a partir de la fonction définie plu haut
        logements_clean.append(logement_clean) #ajout du logement dans la liste des logement du logeur
    connection.close() #fermeture de la connection avec la bdd
    return logements_clean #on retourne la liste obtenue
 
 
 
if __name__ == "__main__":
    df = pd.read_excel('C:/Users/clemc/Desktop/UTC/TC02/INF2/TP/TP6/logeurs.xlsx')
    for logeur in df.values.tolist():
        new_logeur(logeur[0], logeur[1], logeur[2], logeur[3], logeur[4], logeur[5])
 
    df = pd.read_excel("logements.xlsx")
    for logement in df.values.tolist():
        new_log(logement[0], logement[1], logement[2], logement[3], logement[4], logement[5], logement[6], logement[7])
 
 
    df = pd.read_excel("etudiants.xlsx")
    for etudiant in df.values.tolist():
        new_etu(etudiant[0], etudiant[1], etudiant[2], etudiant[3], etudiant[4], etudiant[5])
 
 
    nom_logeur= input("Nom du logeur : ")
    prenom_logeur = input("Prenom du logeur : ")
    logements = get_logements(nom_logeur, prenom_logeur)
    num=1
    for logement in logements:
        print(f"Logement {num}")
        print(f"{logement['numero_rue']} {logement['nom_rue']} {logement['code_postal']} {logement['ville']} {logement['label']} {logement['type']}")
        for etu in logement["etu"]:
            print(f"Nom etudiant : {etu['nom']} {etu['prenom']}")
    num+=1