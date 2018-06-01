#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__='dh'
'''
write for using DAVID api
URL has a charactor size limitation (<= 2048 characters in total), i.e., the very large gene list may not be able to completely passed by URL.
No more than 200 hits in a day from one computer.
10 seconds interval between hits.
'''
import webbrowser,sys
tool=['gene2gene','term2term','summary','chartReport','annotationReport','list','geneReport','geneReportFull']
type=['AFFYMETRIX_3PRIME_IVT_ID','AFFYMETRIX_EXON_GENE_ID','AFFYMETRIX_SNP_ID','AGILENT_CHIP_ID','AGILENT_ID','AGILENT_OLIGO_ID','ENSEMBL_GENE_ID','ENSEMBL_TRANSCRIPT_ID','ENTREZ_GENE_ID','FLYBASE_GENE_ID','FLYBASE_TRANSCRIPT_ID','GENBANK_ACCESSION','GENPEPT_ACCESSION','GENOMIC_GI_ACCESSION','PROTEIN_GI_ACCESSION','ILLUMINA_ID','IPI_ID','MGI_ID','GENE_SYMBOL','PFAM_ID','PIR_ACCESSION','PIR_ID','PIR_NREF_ID','REFSEQ_GENOMIC','REFSEQ_MRNA','REFSEQ_PROTEIN','REFSEQ_RNA','RGD_ID','SGD_ID','TAIR_ID','UCSC_GENE_ID','UNIGENE','UNIPROT_ACCESSION','UNIPROT_ID','UNIREF100_ID','WORMBASE_GENE_ID','WORMPEP_ID','ZFIN_ID']
annot={'Gene_Ontology':['GOTERM_BP_1','GOTERM_BP_2','GOTERM_BP_3','GOTERM_BP_4','GOTERM_BP_5','GOTERM_BP_ALL','GOTERM_BP_FAT','GOTERM_CC_1','GOTERM_CC_2','GOTERM_CC_3','GOTERM_CC_4','GOTERM_CC_5','GOTERM_CC_ALL','GOTERM_CC_FAT','GOTERM_MF_1','GOTERM_MF_2','GOTERM_MF_3','GOTERM_MF_4','GOTERM_MF_5','GOTERM_MF_ALL','GOTERM_MF_FAT'],
       'Protein_Domains':['BLOCKS_ID','COG','INTERPRO','PDB_ID','PFAM','PIR_ALN','PIR_HOMOLOGY_DOMAIN','PIR_SUPERFAMILY','PRINTS','PRODOM','PROSITE','SCOP_ID','SMART','TIGRFAMS'],
       'Pathways':['BBID','BIOCARTA','EC_NUMBER','KEGG_COMPOUND','KEGG_PATHWAY','KEGG_REACTION'],
       'General Annotations':['ALIAS_GENE_SYMBOL','CHROMOSOME','CYTOBAND','GENE','GENE_SYMBOL','HOMOLOGOUS_GENE','LL_SUMMARY','OMIM_ID','PIR_SUMMARY','PROTEIN_MW','REFSEQ_PRODUCT','SEQUENCE_LENGTH','SP_COMMENT'],
       'Functional Categories':['CGAP_EST_QUARTILE','CGAP_EST_RANK','COG_ONTOLOGY','PIR_SEQ_FEATURE','SP_COMMENT_TYPE','SP_PIR_KEYWORDS','UP_SEQ_FEATURE'],
       'Protein-Protein Interaction':['BIND','DIP','HIV_INTERACTION_CATEGORY','HIV_INTERACTION','MINT','NCICB_CAPATHWAY','TRANSFAC_ID'],
       'Literature':['GENERIF_SUMMARY','HIV_INTERACTION_PUBMED_ID','PUBMED_ID'],
       'Disease':['GENETIC_ASSOCIATION_DB_DISEASE','OMIM_DISEASE']}

def api(type,annot,ids,tool):
    api_url = 'http://david.abcc.ncifcrf.gov/api.jsp?type=%s&ids=%s&tool=%s&annot=%s'%(type,ids,tool,annot)
    print('number of char:%s'%len(ids))
    if len(ids)<=2048:
        webbrowser.open_new(api_url)
if __name__=='__main__':
    fl=sys.argv[1]
    type=sys.argv[2]
    tool=sys.argv[3]
    annot=sys.argv[4]
    with open(fl,'r')as f:
        ids=f.readlines()
    ids=[id.strip('\n')for id in ids]
    ids=','.join(ids)
    api(type,annot,ids,tool)
