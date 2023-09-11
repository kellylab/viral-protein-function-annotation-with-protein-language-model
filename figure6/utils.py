from typing import List
from collections import defaultdict
import pandas as pd


def get_faa(path: str, max_length: int = 0) -> List[str]:
    idents = []
    seqs = []
    seq = []

    with(open(path)) as file:
        for line in file:
            line = line.rstrip()
            if line.startswith('>'):
                idents.append(line)
                if len(seq) > 0:
                    seqs.append(''.join(seq).replace('-', ''))
                    seq = []
            else:
                seq.append(line)
    seqs.append(''.join(seq).replace('-', ''))

    # protbert_bfd can only handle sequences < 5096aa
    if max_length > 0:
        seqs = [x[0:max_length] for x in seqs]

    return idents, seqs

def collect_family_pairs(contig_df: pd.DataFrame, neighborhood: int) -> pd.DataFrame:
    contig_df = contig_df.sort_values('protein_id', ascending=True)
    
    family_pairs = []
    for p in contig_df['protein_id']:
        df = contig_df[contig_df['protein_id'].between(p-neighborhood, p+neighborhood)]
        if len(df) > 1:
            query_f = df[df['protein_id'] == p]['query_id'].item()
            target_f = list(df['query_id'])
            target_f.remove(query_f)
            family_pairs.append([(query_f, t) for t in target_f])
    pairs = [p for pp in family_pairs for p in pp]
    return pd.DataFrame(pairs, columns=['p1', 'p2'])

