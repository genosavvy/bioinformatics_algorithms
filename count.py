import re
import logging


logging.basicConfig(
    filename= "count.log",
    level= logging.DEBUG,
    format= '%(asctime)s:%(levelname)s:%(message)s' 
)
logger = logging.getLogger(__name__)

def patterncount(dna_sequence, pattern):
    match = re.finditer(fr'(?=({pattern}))', dna_sequence)    
    return len(list(match))


def frequencytable(dna_sequence, k):
    freqMap = {}
    for i in range(len(dna_sequence)-k + 1):
        kmer = dna_sequence[i:i + k]
        freqMap[kmer] = freqMap.get(kmer, 0) + 1
    return freqMap

def frequentkmer(dna_sequence, k, threshold=None):
    """
    Find frequently occurring k-mers (subsequences) in a given DNA sequence.

    Args:
        dna_sequence (str): The DNA sequence in which to search for frequent k-mers.
        k (int): The length of k-mers to consider.
        threshold (int, optional): An optional threshold value to filter k-mers based on frequency.
            If not provided (default is None), the function returns the most frequent k-mer(s) of
            length k. If provided, the function returns k-mers of length k that occur equal to or
            more times than the specified threshold.

    Returns:
        list: A list of frequently occurring k-mers of length k, based on the specified criteria.
              If threshold is None, the list contains the most frequent k-mer(s) of length k.
              If threshold is provided, the list contains k-mers of length k that occur at least
              as many times as the threshold.

    Example:
        >>> dna_sequence = "AGCTAGCTAGCTAGCTAGCT"
        >>> k = 4
        >>> frequentkmer(dna_sequence, k)
        ['AGCT']
        >>> frequentkmer(dna_sequence, k, threshold=3)
        ['AGCT']
    """
    # Implementation of the function...

    dna_sequence = dna_sequence.upper().strip()
    freq_map = frequencytable(dna_sequence, k)
    if threshold is None:
        max_freq = max(freq_map.values())
        return [key for key, value in freq_map.items() if value == max_freq]
    else:
        return [key for key, value in freq_map.items() if value >= threshold]


def findclumps(dna_sequence,k,L,t):
    kmers= []
    for i in range(len(dna_sequence)-L + 1):
        window= dna_sequence[i:i+L]
        freqmap = frequencytable(window, k)
        [kmers.append(key) for key, value in freqmap.items() if value >= t]

    pattern = list(set(kmers))    

    return pattern





if __name__ == '__main__':
    try:
        with open('text.txt', 'r') as f:
            text = f.readline().strip()
        k = 9
        L = 500
        t = 3
        kmer_list = findclumps(text, k,L,t)
        logger.debug(f'{len(kmer_list)}')
    except FileNotFoundError as e:
        logger.exception('{e}')


