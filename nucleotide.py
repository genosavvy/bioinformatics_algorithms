import logging
import re

# Configure the logger
logging.basicConfig(filename='nucleotide.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def reverse_complement(file_path):
    """
    Compute the reverse complement of a nucleotide sequence.

    Args:
        nucleotide (str): A string representing a DNA sequence consisting of 'A', 'T', 'G', and 'C'.

    Returns:
        str: The reverse complement of the input nucleotide sequence.
    """

    
    # Define a dictionary to map each nucleotide to its complement.
    nuc_dict = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    
    # Initialize an empty list to store the complement of each nucleotide.
    nuc_list = [] 

    # Read file 

    try:

        with open(file_path, "r") as f:
            logger.error('File can not be opened')
            file = f.readlines()
    

        nucleotide = file[0] 
        # logger.debug(f'Generating the reverse complement of {nucleotide}')  

        # Iterate through each nucleotide in the input sequence.
        for i in nucleotide:
            # Look up the complement in the dictionary and append it to the list.
            logger.debug(f'computing the complements for {i}')
            nuc = nuc_dict[i]
            nuc_list.append(nuc)

        # Reverse the list to get the reverse complement.
        nuc_list.reverse()

        # Join the reversed complement list into a single string.
        update_nuc_list = "".join(nuc_list)

        # Return the reverse complement as a string.
        return update_nuc_list
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except IOError as e:
        print(f'An error called while reading the file: {e}')


def nucleotide_loci(pattern, genome):
    matches = re.finditer(fr'(?=({pattern}))', genome)
    list_start = [match.start() for match in matches]
    return list_start
    



