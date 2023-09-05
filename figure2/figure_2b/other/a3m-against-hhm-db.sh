#!/bin/bash

# Code name: a3m-against-hhm-db.sh
# Function: Peform hhsearch for a directory of a3m alignments against a hhsuite db.

msa=($(ls A3M_other | sed 's/.a3m//g'))

for ((i=0; i<${#msa[@]}; i++)); do
        echo "${msa[$i]}"
        hhsearch -i A3M_other/${msa[$i]}.a3m -d phrogs_other_hhsuite_db/phrogs_other -o stdout -B 0 -b 0 -Z 40000 -alt 0 -scores hhsearch_a3m_against_db/${msa[$i]}.scores
done 
