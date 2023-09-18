from  nucleotide import *
import re


def test_reverse():
    assert reverse_complement("data.txt") == "AGTCCGAAT"

def test_nucleotide_loci(): 
    pattern = "ATAT"
    file_path = "genome.txt"
   
    assert nucleotide_loci(pattern, file_path) == [1,3,9]


    
