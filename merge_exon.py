
#!/usr/bin/env python

__author__ = 'xiuchengquek'


import sys
import re
import subprocess
import locale

from progressbar import ProgressBar , Percentage, Bar, RotatingMarker, ETA

from tempfile import NamedTemporaryFile

from collections import defaultdict
import os


gene_name_re = re.compile('gene_name \"([^\"]+)\"')
gene_annotation = defaultdict(list)

fh_out = open(sys.argv[2], 'w+')


encoding = locale.getdefaultlocale()[1]

with open(sys.argv[1]) as f:
    for line in f:
        matched = gene_name_re.search(line)
        gene_name = matched.group(1)
        gene_annotation[gene_name].append(line)






pbar = ProgressBar(widgets=[Percentage(), Bar(marker=RotatingMarker()), ETA()], maxval= len(gene_annotation.keys())).start()

i = 0


for gene, lines in gene_annotation.items():
    temp_file = NamedTemporaryFile(mode='w', delete=False)
    temp_file.write("".join(lines))
    temp_file.close()
    proc = subprocess.Popen(['bedtools','merge', '-s' ,'-i',temp_file.name],stdout=subprocess.PIPE, stderr= subprocess.PIPE)
    std_out , std_err =  proc.communicate()




    if std_err:
        raise ValueError('error in bed line')


    lines = std_out.decode(encoding).split('\n')

    for l in lines:
        if len(l) != 0:
            fields = l.split('\t')
            fields.insert(-1, gene)
            fields.insert(-1, '0')
            l = "\t".join(fields)
            fh_out.write( "%s\n" % l )
    i = i + 1
    pbar.update(i)




fh_out.close()
pbar.finish()














