from  nucleotide import *
import re


def test_reverse():
    assert reverse_complement("data.txt") == "AGTCCGAAT"

def test_nucleotide_loci(): 
    pattern = "ATAT"
    geneome = "GATATATGCATATACTT"
    assert nucleotide_loci(pattern, geneome) == [1,3,9]


    
