import logging
import re

import logging

def reverse_complement(file_path):
    """
    Generate the reverse complement of a DNA sequence read from a file.

    Args:
        file_path (str): The path to the file containing the DNA sequence.

    Returns:
        str: The reverse complement of the DNA sequence.
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

    try:
        with open(file_path, "r") as f:
            # Read the DNA sequence from the file.
            nucleotide = f.readline().strip()

            # Check if the DNA sequence is empty.
            if not nucleotide:
                raise ValueError("The DNA sequence is empty in the file.")

            # Iterate through each nucleotide in the input sequence.
            for i in nucleotide:
                # Look up the complement in the dictionary and append it to the list.
                nuc = nuc_dict.get(i, i)  # Use get to handle unknown nucleotides
                nuc_list.append(nuc)

            # Reverse the list to get the reverse complement.
            nuc_list.reverse()

            # Join the reversed complement list into a single string.
            update_nuc_list = "".join(nuc_list)

            # Return the reverse complement as a string.
            return update_nuc_list

    except FileNotFoundError as e:
        raise FileNotFoundError(f'File not found: {file_path}') from e
    except IOError as e:
        raise IOError(f'An error occurred while reading the file: {e}') from e
    except ValueError as e:
        raise ValueError(f'Error in DNA sequence: {e}') from e

def nucleotide_loci(pattern, file_path):

    try:
        with open(file_path, "r") as f:
            genome = f.readline().strip()
        
        # check the file is not empty
        if not genome:
            raise ValueError("The genome file is empty")
        
        matches = re.finditer(fr'(?=({pattern}))', genome)
        list_start = [match.start() for match in matches]
        return list_start
    except FileNotFoundError as e:
        raise FileNotFoundError(f'File not found : {file_path}') from e
    except IOError as e:
        raise IOError(f' An error occured while reading the file: {e}') from e
    except ValueError as e:
        raise ValueError(f' Error in the dna_sequences: {e}') from e



# Configure logging
logging.basicConfig(filename='reverse_complement.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    file_path = 'dna_sequence.txt'  # Replace with the path to your DNA sequence file
    try:
        reverse_comp = reverse_complement(file_path)
        print(f'Reverse Complement: {reverse_comp}')
        logger.info('Reverse complement generated successfully.')
    except Exception as e:
        print(f'Error: {e}')
        logger.error(f'Error: {e}')








