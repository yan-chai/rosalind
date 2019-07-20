import re
strand1 = 'GUGCGCAAGGUCCUGGAGUAUCCGCUCUCGCAC'
strand2 = 'GUGCGUCUCAUCUGGAGGCUGCACCUGUCCGACCACUACGGCAUCUGGCAGGAAUUCGGCCAGAAGUUCCUCGUCGACCCCGACAUCAUCAAG'
def find_end(rna):
    index1 = -1
    index1_list=[]
    coden1 = re.findall(r'.{3}',rna)
    for i in coden1:
        index1+=1
        if i == "UGA" or i == "UAG" or i == "UAA":
            index1_list.append(index1)
    coden = []
    for i in index1_list:
        coden.append(coden1[:i+1:])
    return(coden)

end1 = find_end(strand1)
end2 = find_end(strand2)
print(end1,end2)
