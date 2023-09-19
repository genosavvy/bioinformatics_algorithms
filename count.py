import re

def patterncount(text, pattern):
    match = re.finditer(fr'(?=({pattern}))', text) 
   
    return len(list(match))


def frequencytable(text, k):
    freqmap = {}
    for i in range(len(text)-k):
        pattern = text[i:i + k]
        if pattern not in freqmap:
            freqmap[pattern] = 1
        else:
            freqmap[pattern] += 1
    return freqmap

def frequentword(text, k):
    freq_map = frequencytable(text, k)
    max_freq = max(freq_map.values())
    return [key for key, value in freq_map.items() if value == max_freq]




if __name__ == '__main__':
    text = "GCGCG"
    pattern = "GCG"
    print(patterncount(text, pattern))
