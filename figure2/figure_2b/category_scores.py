import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import textwrap

def parse_scores(hhresult_file):
	
	df = pd.read_csv(hhresult_file, skiprows=5, header=None, delim_whitespace=True)
	score = list(df[7])
	average_score = sum(score[1:]) / (len(score) - 1)

	return average_score

categories = ['DNA', 'connector', 'head', 'integration', 'lysis', 'moron', 'other', 'tail', 'transcription']


df = pd.DataFrame(columns = ['category', 'scores'])
for category in categories:
    scores = os.listdir('{0}/hhsearch_a3m_against_db' ''.format(category))

    category_scores = []
    for s in scores:
        #category_scores.append(hhparse('{0}/hhsearch_a3m_against_db/{1}' ''.format(category,s)))
        category_scores.append(parse_scores('{0}/hhsearch_a3m_against_db/{1}' ''.format(category,s)))

    category_mean = np.mean(category_scores)
    category_sd = np.std(category_scores)
    category_median = np.median(category_scores)

    cats = [category] * len(category_scores)

    df = pd.concat([df, pd.DataFrame({'category': cats, 'scores': category_scores})], ignore_index=True)

    print('{0}- mean: {1}, sd: {2}, median: {3}' ''.format(category, round(category_mean,3), round(category_sd,3), round(category_median,3)))


# plot distributions
phrog_palette = {
    'DNA': 'red',
    'connector': 'blue',
    'head': 'green',
    'integration': 'pink',
    'lysis': 'gray',
    'moron': 'brown',
    'other': 'purple',
    'tail': 'darkorange',
    'transcription': 'cyan',
    'unknown': 'black'
}


max_width=17

my_order = df.groupby(by=['category'])['scores'].median().sort_values(ascending=False).index

df = df.astype({'scores': float})

g = sns.boxplot(
    y='scores',
    x='category',
    palette=phrog_palette,
    data=df,
    order=my_order
)

xs = {'DNA': 'DNA, RNA and nucleotide metabolism', 
'connector': 'connector', 
'head': 'head and packaging',
'integration': 'integration and excision', 
'lysis': 'lysis', 
'moron': 'moron, auxiliary metabolic gene and host takeover', 
'other': 'other', 
'tail': 'tail', 
'transcription': 'transcription regulation'}

g.set_ylabel('Intra-category family-family HMM similarity')
g.set_xlabel('')
g.set_xticklabels('' for x in g.get_xticklabels())

plt.tight_layout()
plt.savefig('category_hhm_similarity.png', dpi=300)