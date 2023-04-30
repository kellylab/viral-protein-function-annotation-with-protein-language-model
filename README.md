# viral-protein-function-annotation-with-protein-language-model
Accompanying jupyter notebooks and data for figure generation for published manuscript

to run notebooks data must be downloaded:  
Final_Super_Condensed_Annotations-updated_efam.tsv (184.8 Mb) from: https://storage.googleapis.com/viral_protein_family_plm_embeddings/efam/Final_Super_Condensed_Annotations-updated_efam.tsv
PHROG_index_downloaded_01232022.csv (4.4 Mb) from: https://storage.googleapis.com/viral_protein_family_plm_embeddings/phrogs/PHROG_index_downloaded_01232022.csv 
PHROG_index_revised_v4_10292022.csv (4.1 Mb) from: https://storage.googleapis.com/viral_protein_family_plm_embeddings/phrogs/PHROG_index_revised_v4_10292022.csv 

(phrog classifier training only) protbert_bfd_embeddings_phrog/ (38,800 pkl objects) from: https://storage.googleapis.com/viral_protein_family_plm_embeddings/phrogs/protbert_bfd_embeddings_phrog/ + 'phrog_#' for all 38,880 PHROG families

(figure3 only) phrog_familiy_centroid/ (38,880 pkl objects, \~4.1Kb/per) from: https://storage.googleapis.com/viral_protein_family_plm_embeddings/phrogs/phrog_family_centroid/ + 'phrog_#' for all 38,880 PHROG families


To download sequence embeddings generated for this project:

1) PHROG families- each directory contains 38,800 pkl objects corresponding to the 38,880 viral protein families in PHROGs. To download the pkl objects, use the base url below + 'phrog_#.pkl' for the phrog of interest.  
For example- for the Transformer_BFD embeddings of PHROG 1- https://storage.googleapis.com/viral_protein_family_plm_embeddings/phrogs/protbert_bfd_embeddings_phrog/phrog_1.pkl. pkl object size varies with number of sequences the family.  
Embedding order in the object corresponds to the order of the sequences in the corresponding phrog faa file, which can be downloaded from https://storage.googleapis.com/viral_protein_family_plm_embeddings/phrogs/faa_downloaded_04052022/ with + 'phrog_#.faa'.  

Transformer_BFD from: https://storage.googleapis.com/viral_protein_family_plm_embeddings/phrogs/protbert_bfd_embeddings_phrog/  
LSTM_Uniref90 from: https://storage.googleapis.com/viral_protein_family_plm_embeddings/phrogs/bepler_dlm_embed_phrog/  
LSTM_Uniref90_MT from: https://storage.googleapis.com/viral_protein_family_plm_embeddings/phrogs/bepler_mt_embed_phrog/  
Transformer_Uniref90_MT from: https://storage.googleapis.com/viral_protein_family_plm_embeddings/phrogs/proteinbert_embeddings_phrog/  

2) EFAM sequences- downloaded as a single pkl dictionary object with sequence:embedding. All embedding done with Transformer_BFD. 

EFAM embeddings (10.2 Gb)- https://storage.googleapis.com/viral_protein_family_plm_embeddings/efam/identifier_to_vector_protbert_bdf_11012022_dict.pkl  
EFAM protein fasta used (767.5 Mb)- https://storage.googleapis.com/viral_protein_family_plm_embeddings/efam/dereplicated_filtered_proteins_efam_downloaded_10162022.faa

3) PHANN sequences- downloaded as a single pkl dictionary object with sequence:embedding. ll embedding done with Transformer_BFD. 

PHANN embeddings (2.1 Gb)- https://storage.googleapis.com/viral_protein_family_plm_embeddings/phanns/all_sequence_ids_to_vectors_dict.pkl
