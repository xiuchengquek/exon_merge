#!/usr/bin/env python 


import sys
import re






gene_re = re.compile('gene_name \"([^"]+)\"')
gene_id_re = re.compile( 'gene_id \"([^.]+)\.')


gene_dict = {}


with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        gene_name = gene_re.search(line).group(1)
        gene_id = gene_id_re.search(line).group(1)
        gene_dict[gene_id] = gene_name

with open(sys.argv[2],'w') as f:
    f.write('ensg\thgnc\n') 
    for key, value in gene_dict.items():
        f.write("%s\t%s\n" % (key, value ))



