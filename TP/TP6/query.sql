-- SQLite
CREATE TABLE "etudiant" (
    "nom"	TEXT NOT NULL,
	"prenom"	TEXT NOT NULL,
	"semestre"	TEXT NOT NULL,
	"idlogement"	INTEGER,
	FOREIGN KEY("idlogement"),
    PRIMARY KEY("idetu")
);


