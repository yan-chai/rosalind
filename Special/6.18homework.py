# -*- coding=utf-8 -*-
# This is the code to deal 19.6.18's homework
# Copyleft: everybody in ECUST grades 3 major in biology could use this code do genetic engineering homework
#           Written by yhy, supported by qjz
import re   #引入正则库

def reverse(dna):
    pairs = {'A':'T','T':'A','C':'G','G':'C'}
    return ''.join([pairs[x] for x in dna])[::-1]

def transcribe(dna):
    pairs = {'A':'U','T':'A','C':'G','G':'C'}
    return ''.join([pairs[x] for x in dna])[::-1]

def find_start(rna):
    index1 = -1
    index1_list=[]
    index2 = -1
    index2_list=[]
    index3 = -1
    index3_list=[]
    coden1 = re.findall(r'.{3}',rna)
    coden2 = re.findall(r'.{3}',rna[1::])
    coden3 = re.findall(r'.{3}',rna[2::])
    for i in coden1:
        index1+=1
        if i == "GUG" or i == "AUG":
            index1_list.append(index1)
    for i in coden2:
        index2+=1
        if i == "GUG" or i == "AUG":
            index2_list.append(index2)
    for i in coden3:
        index3+=1
        if i == "GUG" or i == "AUG":
            index3_list.append(index3)
    coden = []
    for i in index1_list:
        coden.append(coden1[i::])
    for i in index2_list:
        coden.append(coden2[i::])
    for i in index3_list:
        coden.append(coden3[i::])
    return(coden)   
    
def find_end(rna):
    index1 = -1
    index1_list=[]
    index2 = -1
    index2_list=[]
    index3 = -1
    index3_list=[]
    coden1 = re.findall(r'.{3}',rna)
    coden2 = re.findall(r'.{3}',rna[1::])
    coden3 = re.findall(r'.{3}',rna[2::])
    for i in coden1:
        index1+=1
        if i == "UGA" or i == "UAG" or i == "UAA":
            index1_list.append(index1)
    for i in coden2:
        index2+=1
        if i == "UGA" or i == "UAG" or i == "UAA":
            index2_list.append(index2)
    for i in coden3:
        index3+=1
        if i == "UGA" or i == "UAG" or i == "UAA":
            index3_list.append(index3)
    coden = []
    for i in index1_list:
        coden.append(coden1[:i+1:])
    for i in index2_list:
        coden.append(coden2[:i+1:])
    for i in index3_list:
        coden.append(coden3[:i+1:])
    return(coden)

def CG_content(conden_list):
    cg_content = []
    for i in conden_list:
        first =(i[1].count('G')+i[1].count('C'))/3
        second = (i[2].count('G')+i[2].count('C'))/3
        thrid = (i[3].count('G')+i[3].count('C'))/3
        cg_content.append([first*100, second*100, thrid*100])
    return cg_content

def most_likely(codens, var):
    index = 0
    min_var =min(var)
    index_list = []
    likely_coden = []
    for i in var:
        if i == min_var:
            index_list.append(index)
            index+=1
    for i in index_list:
        likely_coden.append(codens[i])
    return likely_coden

def suit(cg):
    variance = []
    for i in cg:
        variance.append(((int(i[0])-66)**2+(int(i[1])-53)**2+(int(i[2])-93)**2)/3)
    return variance

def rare_coden(coden):
    dic = {}
    print(coden)
    for i in coden:
        string = ''
        for j in i:
            string += j
        count_n = int(i.count("UUA"))+int(i.count("CUA"))
        count_r = int(i.count("UUU"))+int(i.count("AUU"))+int(i.count("GUU"))+int(i.count("UCU"))+int(i.count("CCA"))+int(i.count("ACU"))
        dic[string] = str("稀有密码子"+str(count_r)+",禁止密码子"+str(count_n))
    return(dic)

code_s = 'CGCTTGCGTGCGTCTCATCTGGAGGCTGCACCTGTCCGACCACTACGGCATCTGGCAGGAATTCGGCCAGAAGTTCCTCGTCGACCCCGACATCATCAAG'
code_e = 'GGTGCGAGAGCGGATACTCCAGGACCTTGCGCACCTACCTGTCCTACGGCAGCAGCGACAACGCGAACCCAGTCTGCGAGACACGGCTGTGCAGGCCGTC' #输入序列
pair_code_s = reverse(code_e)
pair_code_e = reverse(code_s)
code_s_rna = transcribe(code_e)
code_e_rna = transcribe(code_s)
pair_code_s_rna = transcribe(pair_code_e)
pair_code_e_rna = transcribe(pair_code_s)
start_findall = find_start(code_s_rna)
pair_start_findall = find_start(pair_code_s_rna)
end_findall = find_end(code_e_rna)
pair_end_findall = find_end(pair_code_e_rna)
cg_start = CG_content(start_findall)
pair_cg_start = CG_content(pair_start_findall)
start_suit = suit(cg_start)
pair_start_suit = suit(pair_cg_start)
most_likely_s = most_likely(start_findall, start_suit)
pair_likely_s = most_likely(pair_start_findall, pair_start_suit)
rare = rare_coden(most_likely_s)
pair_rare = rare_coden(pair_likely_s)
print("输入的起始序列：",code_s)
print("输入的结束序列：",code_e)
print("将输入的结束序列逆序互补后作为起始为：",pair_code_s)
print("将输入的起始序列逆序互补后作为结束为：",pair_code_e)
print("给的DNA起始转录后为：", code_s_rna)
print("给的DNA结束转录后为：", code_e_rna)
print("给的DNA互补起始转录后为：",pair_code_s_rna)
print("给的DNA互补结束转录后为：",pair_code_e_rna)
print("给的链找起始子：", start_findall)
print("互补链找起始子：", pair_start_findall)
print("给的链找中止子：", end_findall)
print("互补链找中止子：", pair_end_findall)
print("给的链前三个密码子CG比例：", cg_start)
print("互补链前三个密码子CG比例", pair_cg_start)
print("给的链前三个密码子CG的方差：", start_suit)
print("互补链前三个密码子CG的方差：", pair_start_suit)
print("给的链前三个最可能起始子：", most_likely_s)
print("互补链前三个最可能起始子：", pair_likely_s)
print("给定链密码子偏好分析：", dict(rare, **pair_rare))
input()