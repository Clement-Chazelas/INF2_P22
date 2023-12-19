def somme_ligne(mat, i) :
    return sum(mat[i])

def somme_colone(mat,j) :
    s = 0
    for i in range(len(mat)) :
        s = s + mat[j][i]    
    return s

def somme_diag1(mat) :
    s = 0
    for i in range(len(mat)) :
        s = s + mat[i][i]
    return s

def somme_diag2(mat) :
    s = 0
    for i in range(len(mat)) :
        s = s + mat[len(mat)-i-1][len(mat)-i-1]
    return s

def magique(mat_c) :
    Magique = True
    for i in range(len(mat_c)) :
        if somme_diag1(mat_c) != somme_colone(mat_c,i) :
            Magique = False
        if somme_diag1(mat_c) != somme_diag2(mat_c) :
            Magique = False
        if somme_diag1(mat_c) != somme_ligne(mat_c,i) :
            Magique = False
    return Magique

def carre_magique_normal(mat_c) :
    magique_normal = True
    somme_totale = 0
    for i in range(len(mat_c)) :
        for j in range(len(mat_c)) :
            somme_totale = somme_totale + mat_c[i][j]
    if somme_totale != ((len(mat_c)**2)*((len(mat_c)**2)+1))/2 :
        magique_normal = False
    return magique_normal