import pandas as pd
import numpy as np

def hamming(s1,s2):
    '''compute hamming distance as a fraction of the target sequence (s1) length'''
    h = 0
    n = 0
    for a,b in zip(s1,s2):
        if a!=b:
            h += 1
            n += 1
        elif a!='-':
            n += 1
    return h/n


def hamming_allvall(seqs_df):
    '''from a table of aligned sequences, compute hamming distance matrix'''
    N = len(seqs_df)
    X = np.zeros((N,N))
    X[:,:] = np.nan
    
    x = np.array(seqs_df.aln)
    for i in range(N):
        for j in range(i,N):
            h = hamming(x[i], x[j])
            X[i,j] = h
            X[j,i] = h
        if i%200 == 0:
            print(f'completed: {i} out of {N} sequences')
    return X

def read_fa(fa_file):
    '''reads fasta file into header/sequence pairs'''
    header = ''
    seq = ''
    seqs = []
    with open(fa_file, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == 0 or line[0] == '#':
                continue
            if line[0] == '>':
                seqs.append((header, seq))
                header = line[1:]
                seq = ''
            else:
                seq += line

    seqs.append((header, seq))
    seqs = pd.DataFrame(seqs[1:], columns=['header', 'seq'])
    return seqs
 

def write_fa(fa_table, outfile):
    '''write seq table to fasta'''
    with open(outfile, 'w') as f:
        for i, row in fa_table.iterrows():
            f.write('>' + row['header'] + '\n')
            f.write(row['seq'] + '\n')

             