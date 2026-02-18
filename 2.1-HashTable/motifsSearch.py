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

print (reversecompl('AACGTGGCA'))
