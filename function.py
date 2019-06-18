import re
def read_txt():
    import glob
    txt = glob.glob('./*txt')
    with open(txt[0], 'r', encoding='UTF-8') as txtData:
        out = txtData.read()
        txtData.close()
    return out

def cut_text(text,lenth): 
    textArr = re.findall('.{'+str(lenth)+'}', text) 
    textArr.append(text[(len(textArr)*lenth):]) 
    return textArr
