from count import *

def test_patterncount():
    text = "GCGCG"
    pattern = "GCG"
    assert patterncount(text, pattern) == 2


def test_frequencytable():
    text = "ACGTTGCATTGTAAT"
    k =12
    assert frequencytable(text, k) == {'ACGTTGCATTGT': 1, 'CGTTGCATTGTA': 1, 'GTTGCATTGTAA': 1, 'TTGCATTGTAAT': 1}

def test_frequentkmer():
    text_test = """aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactga
    aactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaa
    ttacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaa
    acaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggttt
    ctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattca
    agattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtat
    ccaagccgatttcagagaaacctaccacttacctaccacttacctaccacccgggtggta
    agttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaa
    cctaccacctgcgtcccctattatttactactactaataatagcagtataattgatctga"""
   
    k = 9
    assert len(frequentkmer(text_test, k, threshold=3)) == 4
    assert frequentkmer(text_test, k, threshold=3) == ['TGGTAGGTT', 'GGTAGGTTT', 'ACCTACCAC', 'CCTACCACC']



def test_findclumps():
    text = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    k = 5
    L = 50
    t = 4
    assert findclumps(text, k,L,t) == ['GAAGA', 'CGACA']

    