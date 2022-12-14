from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3,venn2

def _2sets():
    diagrama=venn2(subsets=(1, 1, 1),set_labels=('A','B'),alpha=1)
    diagrama.get_patch_by_id('10').set_color('white')
    diagrama.get_patch_by_id('11').set_color('#252440')
    diagrama.get_patch_by_id('01').set_color('white')
    for i in ('10','11','01'):
        diagrama.get_patch_by_id(i).set_edgecolor("black")
    plt.show()

def _3sets():
    pass

_2sets()
'''plt.figure(figsize=(4,4))
v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels = ('A', 'B', 'C'))
plt.show()'''