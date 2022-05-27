def allele_combi(p:str) -> list:
    """
    Retourne les combinaisons d’allèles possibles à partir d'un génotype donné.
    
    Args:
        p: génotype du parent.
    
    Return:
        Toutes les combinaisons d'allèles possibles (liste de str)
    """
    # Je veux faire : rrYy -> rY et ry
    
    # Initiliser la liste des combinaisons possibles.
    possibilities = []
    # Boucler sur les 2 premier elements du génotype (ici: rr)
    for r in p[:2]:
        # Boucler sur les 2 derniers elements du génotype (ici: Yy)
        for y in p[2:]:
            # Fusionner les allèles (rY au premier tour, puis ry, etc.)
            gene_comp = r+y
            # Si je n'ai pas déjà vue cette possibilité,
            if gene_comp not in possibilities:
                # L'ajouter à la liste.
                possibilities.append(r+y)   

    return possibilities


def offspring_genotypes_probabilities(p1:str, p2:str) -> dict:
    """
    Retourne tous les génotypes possibles des enfants produit par les génotypes des parents donnés 
    ainsi que leur probabilité d'apparition.
    
    Args:
        p1: génotype du premier parent.
        p2: génotype du deuxième parent.
    
    Return:
        Tous les génotypes possibles des enfants (dict de str -> int)
    """
    # Déterminer les allèles que chaque parents peuvent donner.
    p1_alleles = allele_combi(p1)
    p2_alleles = allele_combi(p2)

    # Initialisation du dictionaire des génotypes possibles des enfants.
    # On utilise un dictionnaire ici car nous voulons mémoriser non seulement le génotype, 
    # mais également le nombre de fois que nous l'avons généré.
    genotypes = {}
    
    # N'oublions pas que nous voulons des probabilités. 
    # Il nous faut donc diviser le nombre d'apparition de chaque génotype stocké dans le dictionaire genotypes 
    # par le total d'apparitions pour avoir cette notion de probabilité.
    total = 0
    
    # Pour chaque possibilité du premier parent
    for p1_allele in p1_alleles:
        # Combiner avec les possibilité du deuxième parent
        for p2_allele in p2_alleles:            
            # Combiner les 2 possibilité allèle par allèle 
            # (la première allèle de p1 avec la première de p2 puis la deuxième).
            # Exemple: si p1 = RY et p2 = ry alors on obtient: RrYy
            
            # Initialisation du genotype possible
            geno = ""
            for x, y in zip(p1_allele, p2_allele):
                # Par convention, on écrit toujours l'allèle dominante en premier.
                t = x+y if x.isupper() else y+x
                # Ajouter la combinaison au génotype
                geno += t
            
            # Si ce génotype n'a pas encore été vue, initialiser sa probabilité à 1
            if geno not in genotypes:
                genotypes[geno] = 1
            else:
                # Sinon, incrémenter sa probabilité de 1
                genotypes[geno] += 1
            
            # Incrémenter le nombre total de possibilités vues.
            total += 1
    
    # Afficher toutes les possibilités avec leur probabilité d’apparition.
    for key, value in genotypes.items():
        print(key, ":", value, "/", total)
        genotypes[key] = value / total
    
    return genotypes


def most_probable_offspring_genotype(p1:str, p2:str) -> str:
    """
    Retourne le génotype le plus probable produit par les génotypes des parents donnés.
    
    Args:
        p1: génotype du premier parent.
        p2: génotype du deuxième parent.
    
    Return:
        Le génotype le plus probable.
    """
    # Quels sont les génotypes possibles des enfants ?
    genotypes = offspring_genotypes_probabilities(p1, p2)
    
    # Conserver le plus probable
    max_proba = 0
    most_probable_geno = ""
    for genotype, probability in genotypes.items():
        if probability > max_proba:
            max_proba = probability
            most_probable_geno = genotype
    
    return most_probable_geno

if __name__ == '__main__':
    for ex in ["RrYy", "RRYY", "rrYy"]:
        print(allele_combi(ex))

    print("Most probable genotype:", most_probable_offspring_genotype("RrYy", "RrYy"))