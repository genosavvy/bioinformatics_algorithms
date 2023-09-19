from count import *

def test_patterncount():
    text = "GCGCG"
    pattern = "GCG"
    assert patterncount(text, pattern) == 2


def test_frequencytable():
    k = 2
    text = "ACGTTGCA"
    assert frequencytable(text, k) == {'AC': 1, 'CG': 1, 'GT': 1, 'TT': 1, 'TG': 1, 'GC': 1}

def test_frequentword():
    text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    assert frequentword(text,k) == ['GCAT', 'CATG']

    