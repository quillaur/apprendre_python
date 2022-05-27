import genetique_mendel

def test_allele_combi():
    assert genetique_mendel.allele_combi("rrYy") == ["rY", "ry"]
    assert genetique_mendel.allele_combi("RrYy") == ['RY', 'Ry', 'rY', 'ry']
    assert genetique_mendel.allele_combi("RRYY") == ['RY']

def test_offspring_genotypes_probabilities():
    assert genetique_mendel.offspring_genotypes_probabilities("RrYy", "RrYy") == {'RRYY': 0.0625,
                                                                                    'RRYy': 0.125,
                                                                                    'RrYY': 0.125,
                                                                                    'RrYy': 0.25,
                                                                                    'RRyy': 0.0625,
                                                                                    'Rryy': 0.125,
                                                                                    'rrYY': 0.0625,
                                                                                    'rrYy': 0.125,
                                                                                    'rryy': 0.0625}

def test_most_probable_offspring_genotype():
    assert genetique_mendel.most_probable_offspring_genotype("RrYy", "RrYy") == 'RrYy'
                                                                                