{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c6a1b285-6920-4164-9627-bff75862ba49",
   "metadata": {},
   "source": [
    "Fonction Reverse Complémentaire "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "749d5460-ab65-44d3-b149-ba00b94af96d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/home/shyrin/LU3IN/402/2.1-HashTable\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "print(os.getcwd())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "83656389-63bf-4ee6-bbe8-464fe61fd95d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TGCCACGTT\n"
     ]
    }
   ],
   "source": [
    "def reversecompl(seq:str) :\n",
    "    \"\"\"Renvoie le brin complémentaire d’une séquence.\n",
    "    entrée seq : sequence de nucléotides (brin sens)\n",
    "    sortie     : sequence de nucléotides (brin complementaire)\n",
    "    >>> reversecompl('AACGTGGCA')\n",
    "    'TGCCACGTT'\n",
    "    \"\"\"\n",
    "    compl = {'A': 'T', 'C': 'G', 'G': 'C', 'T':'A'}\n",
    "    rev_seq = []\n",
    "    for n in seq[::-1] : \n",
    "        rev_seq.append(compl[n])\n",
    "    return \"\".join(rev_seq)\n",
    "\n",
    "print (reversecompl('AACGTGGCA'))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
