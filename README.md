## Introduction

Python wrapper around bedtools to find the coding region from a bedfile by using bedtools merge


bedfile contains exon features only. bed file is generated from gencode gtf file using gtf2bed program 

to run 

```

python exon_merge.py <input> <output>

```


There is a test bed file 


```
python exon_merge.py test/test.bed test/test.out

cat test/test.out
1	50	300	DDX11L1	0	+
```




