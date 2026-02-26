def readFasta(fastaFileName):
    """
    Lit un fichier fasta
    entrée fastaFileName: nom du fichier fasta
    sortie séquences: liste contenant toutes les séquences du fichier
    """
    
    sequence = ""
    sequences_list = []
    prev_header = ""
    header = ""
        
    for line in open(fastaFileName):
        string = line.strip()
        if string[0] != ">":
            if prev_header != header:
                prev_header = header
            sequence = sequence + string
        else:
            header = string
            if sequence != "":
                sequences_list.append(sequence)
                sequence = ""

    sequences_list.append(sequence)
    return sequences_list

def reversecompl(seq:str) :
    """Renvoie le brin complémentaire d’une séquence.
    entrée seq : sequence de nucléotides (brin sens)
    sortie     : sequence de nucléotides (brin complementaire)
    >>> reversecompl('AACGTGGCA')
    'TGCCACGTT'
    """
    compl = {'A': 'T', 'C': 'G', 'G': 'C', 'T':'A'}
    rev_seq = []
    for n in seq[::-1] : 
        rev_seq.append(compl[n])
    return "".join(rev_seq)
