from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3,venn2

def _2sets(operation):
    operation=operation.split(' ')

    sets={}
    sets['A']={'100','110'}
    sets['B']={'110','010'}

    set1=list(sets.get(str(operation[0])))
    set2=list(sets.get(str(operation[2])))

    if operation[1]=='-':
        result=set(set1)-set(set2)
    elif operation[1]=='u':
        result=set(set1)|set(set2)
    elif operation[1]=='n':
        result=set(set1).intersection(set2)

    diagrama=venn2(subsets=(1, 1, 1),set_labels=('A','B'),alpha=1)
    for i in ('100','110','010'):
        if i in result:
            diagrama.get_patch_by_id(i).set_color('#252440')
        else:
            diagrama.get_patch_by_id(i).set_color('white')        
    
    
    for i in ('10','11','01'):
        diagrama.get_patch_by_id(i).set_edgecolor("black")
    
    plt.show()
    return result

def _3sets(operation):
    operation=operation.split(' ')

    set3=['111','011','001','101']

    _1op=str(operation[0]+' '+operation[1]+' '+operation[2])

    res_1op=_2sets(_1op)
    print(res_1op)

    if operation[3]=='-':
        result=set(res_1op)-set(set3)
    elif operation[3]=='u':
        result=set(res_1op)|set(set3)
    elif operation[3]=='n':
        result=set(res_1op).intersection(set3)

    diagrama=venn3(subsets=(1, 1, 1,1,1,1,1),set_labels=('A','B','C'),alpha=1)
    for i in ('100','110','010','001','101','111','011'):
        if i in result:
            diagrama.get_patch_by_id(i).set_color('#252440')
        else:
            diagrama.get_patch_by_id(i).set_color('white')        
    
    
    for i in ('100','110','010','001','101','111','011'):
        diagrama.get_patch_by_id(i).set_edgecolor("black")
    

    plt.show()


_3sets(input('operation: '))
