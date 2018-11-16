#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:13:25 2018

@author: robin
"""


    
# Distance de Levenstein
def LD(s, t):
    
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([LD(s[:-1], t) + 1,
               LD(s, t[:-1]) + 1,
               LD(s[:-1], t[:-1]) + cost])
    return res

# Nettoyage du texte
def replace(m_string):
    return m_string.replace(":", "").replace(";", "").replace(")", "").replace("(", "").replace("\u200b", "").lower()

# Supprime stopwords
def remove_stopwords(word_list):
    '''''
    I : Liste de mots
    O : Liste de mots filtrée
    '''''
    return [word for word in word_list if word not in stopwords.words('english')]

# regex intermédiaire
def regex_transformation(regex, str):
    
    t = regex.findall(str)
    t = ''.join(t)
    match_number = re.compile('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    t = [float(x) for x in re.findall(match_number, t)]
    return t

# -*- coding: utf-8 -*-
alphabets = "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"


# split texte en listes de phrases
def split_into_sentences(text):
    
    text = " " + text + "  "
    text = text.replace("\n", " ")
    text = re.sub(prefixes, "\\1<prd>", text)
    text = re.sub(websites, "<prd>\\1", text)
    if "Ph.D" in text:
        text = text.replace("Ph.D.", "Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] ", " \\1<prd> ", text)
    text = re.sub(acronyms + " " + starters, "\\1<stop> \\2", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" +
                  alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
    text = re.sub(alphabets + "[.]" + alphabets +
                  "[.]", "\\1<prd>\\2<prd>", text)
    text = re.sub(" " + suffixes + "[.] " + starters, " \\1<stop> \\2", text)
    text = re.sub(" " + suffixes + "[.]", " \\1<prd>", text)
    text = re.sub(" " + alphabets + "[.]", " \\1<prd>", text)
    if "”" in text:
        text = text.replace(".”", "”.")
    if "\"" in text:
        text = text.replace(".\"", "\".")
    if "!" in text:
        text = text.replace("!\"", "\"!")
    if "?" in text:
        text = text.replace("?\"", "\"?")
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

# Bug des listes dans le dataframe
def clean_table(appended_data):
    
    for i, var in enumerate(appended_data):
        appended_data[var] = appended_data[var].str[0]
    return appended_data

# Prend les valeurs dans le texte
def search_direct_values(str):

    str = replace(str)

    regex_glomeruli = re.compile('number of glomeruli -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_glom_scler = re.compile('number globally sclerotic -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_g = re.compile(' g -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_i = re.compile(' i -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_v = re.compile(' v -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_t = re.compile(' t -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_ah = re.compile(' ah -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_cg = re.compile(' cg -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_mm = re.compile(' mm -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_ci = re.compile(' ci -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_ct = re.compile(' ct -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_cv = re.compile(' cv -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_ptc = re.compile(' ptc -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
    regex_ti = re.compile(' ti -?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')


    nb_glomeruli = regex_transformation(regex_glomeruli, str)
    glom_scler = regex_transformation(regex_glom_scler, str)
    g = regex_transformation(regex_g, str)
    i = regex_transformation(regex_i, str)
    v = regex_transformation(regex_v, str)
    t = regex_transformation(regex_t, str)
    ah = regex_transformation(regex_ah, str)
    cg = regex_transformation(regex_cg, str)
    mm = regex_transformation(regex_mm, str)
    ci = regex_transformation(regex_ci, str)
    ct = regex_transformation(regex_ct, str)
    cv = regex_transformation(regex_cv, str)
    ptc = regex_transformation(regex_ptc, str)
    ti = regex_transformation(regex_ti, str)


    df = pd.DataFrame(columns=['glomerulis', 'g', 'i', 't', 'v',
                               'ah', 'cg', 'ci', 'ct', 'ti', 'cv', 
                               'mm', 'ptc', 'glom_scler'])

    y = {'glomerulis': nb_glomeruli, 'g': g, 'i': i, 
         't': t, 'v': v, 'ah': ah, 'cg': cg, 'ci': ci, 
         'ct': ct, 'ti': ti, 'cv': cv, 'mm': mm, 
         'ptc': ptc, 'glom_scler': glom_scler
        }

    df.loc['y'] = y
    df = df.reset_index(drop=True)

    return df

def add_ifta(df):
    if(df.ci.values[0] == 0 and df.ct.values[0] == 1) or (df.ci.values[0] == 1 and df.ct.values[0] == 0) or (df.ci.values[0] == 1 and df.ct.values[0] == 1):
        df['IFTA'] = 1
    elif(df.ci.values[0] == 2 and df.ct.values[0] == 2) or (df.ci.values[0] == 2 or df.ct.values[0] == 2):
         df['IFTA'] = 2
    elif(df.ci.values[0] == 3 and df.ct.values[0] == 3) or (df.ci.values[0] == 3 or df.ct.values[0] == 3):
         df['IFTA'] = 3
    else:
        df['IFTA'] = 0
    return  df

def get_banff_code(dictOfElements, valueToFind):
    for code, name in medical_words.items():
        if valueToFind in name:
            return code