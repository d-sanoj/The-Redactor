# Importing necessary libraries to be unsed in this program.
# Module spacy for entity recognition and nlp
# Module clllections being imported
# Module re for regular expressions
# Module nltk for concepts
# Module glob for file reading
# Module sys for main function args
# Module os for file paths, files and directories

import spacy
from spacy import displacy
from collections import Counter
import re
from nltk.corpus import wordnet
import glob
import sys
import os
import nltk

# Downloading and loading necessary models for nltk and spacy running the program

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('omw-1.4')

nlp = spacy.load('en_core_web_sm')

# Code for reading text file that is to be processed
def read_text(inputfiles):
    txt = []
    with open(inputfiles, 'r') as myfile:
        txt = myfile.read()
    return(txt)

# Redacting methods using spacy, re and wordnet
# Source for spacy - https://predictivehacks.com/redact-name-entities-with-spacy/
# Source for regex - https://stackoverflow.com/questions/16699007/regular-expression-to-match-standard-10-digit-phone-number
# Source for regex tester - https://www.regextester.com
# Source for wordnet and lemma - https://www.geeksforgeeks.org/get-synonymsantonyms-nltk-wordnet-python/

# Redacting names using spacy entity recognition
def redact_names(txt, inputfiles):
    clean_text1 = txt
    doc = nlp(txt)
    for ent in reversed(doc.ents):
            if ent.label_ == 'PERSON':
                clean_text1 = clean_text1[:ent.start_char] + u"\u2588"*len(ent.label_) + clean_text1[ent.end_char:]
    return clean_text1

# Redacting addresses using spacy entity recognition
def redact_address(txt, inputfiles):
    clean_text2 = txt
    doc = nlp(txt)
    for ent in reversed(doc.ents):
            if ent.label_ == 'GPE':
                clean_text2 = clean_text2[:ent.start_char] + u"\u2588"*len(ent.label_) + clean_text2[ent.end_char:]
            if ent.label_ == 'LOC':
                clean_text2 = clean_text2[:ent.start_char] + u"\u2588"*len(ent.label_) + clean_text2[ent.end_char:]
            if ent.label_ == 'FAC':
                clean_text2 = clean_text2[:ent.start_char] + u"\u2588"*len(ent.label_) + clean_text2[ent.end_char:]
    return clean_text2

# Redacting dates using spacy entity recognition and regex
def redact_dates(txt, inputfiles):
    clean_text3 = txt
    doc = nlp(txt)
    for ent in reversed(doc.ents):
            if ent.label_ == 'DATE':
                clean_text3 = clean_text3[:ent.start_char] + u"\u2588"*len(ent.label_) + clean_text3[ent.end_char:]

    str=re.findall(r'\d{4} | [\d]{1,2}/[\d]{1,2}/[\d]{2,4} | Sun,| Mon,| Tue,| Wed,| Thu,| Fri,| Sat,| Jan | Feb | Mar | Apr| May | Jun | Jul | Aug | Sep | Oct | Nov | Dec ',txt)
    for digit in str:
        clean_text3=clean_text3.replace(digit,u"\u2588"*len(digit))
    return clean_text3

# Redacting genders using regex
def redact_genders(txt, inputfiles):
    clean_text4 = txt
    r = re.compile(r'\A He | he |[Ss]he | [Hh]im| [Hh]is | [Hh]er | [Mm]en| [Ww]omen')
    str = r.findall(txt)
    for digit in str:
        clean_text4=clean_text4.replace(digit,u"\u2588"*len(digit))
    return clean_text4

# Redacting phonenumbers using regex
def redact_phonenumber(txt, inputfiles):
    clean_text5 = txt
    str=re.findall(r' \d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4} ',txt)
    for digit in str:
        clean_text5=clean_text5.replace(digit,u"\u2588"*len(digit))
    return clean_text5

# redacting synonyms using nltk wordnet and lemma
def redact_concepts(txt, inputfiles, concept):
    clean_text6 = txt
    for syn in wordnet.synsets(concept):
        for l in syn.lemmas():
            sentence = clean_text6.splitlines()
            for line in sentence:
                if concept in line:
                    clean_text6=clean_text6.replace(line,u"\u2588"*len(line))
    return clean_text6


# Main function to run above functions
arg_ls = sys.argv
files=[]

for i in range(len(arg_ls)):
    if arg_ls[i] == '--input':
        # Using glob to read input files
        files.extend(glob.glob(arg_ls[i+1]))

for i in files:
    data = read_text(i)
    datacount = read_text(i)
    for j in range(len(arg_ls)):
            if arg_ls[j] == '--names':
                data = redact_names(data, i)

            if arg_ls[j] == '--address':
                data = redact_address(data, i)

            if arg_ls[j] == '--dates':
                data = redact_dates(data, i)

            if arg_ls[j] == '--phones':
                data = redact_phonenumber(data, i)

            if arg_ls[j] == '--concept':
                data = redact_concepts(data, i, arg_ls[j+1])
                concept = arg_ls[j+1]

            if arg_ls[j] == '--genders':
                data = redact_genders(data, i)

            # Writing output to a file in files director
            if arg_ls[j] == '--output':
                if(arg_ls[j+1]) == 'files/':
                    file = open(arg_ls[j+1]+i.split('.')[0]+'.redacted','w')
                    file.write(data)
                    file.close()
                else:
                    os.mkdir(arg_ls[j+1])
                    file = open(arg_ls[j+1]+i.split('.')[0]+'.redacted','w')
                    file.write(data)
                    file.close()

            if arg_ls[j] == '--stats':
                # Counting stats for each function
                doc = nlp(datacount)
                totalcount = []
                countname = 0
                for ent in reversed(doc.ents):
                    if ent.label_ == 'PERSON':
                        countname = countname+1

                countaddress = 0
                for ent in reversed(doc.ents):
                    if ent.label_ =='GPE':
                        countaddress = countaddress+1
                    if ent.label_ =='LOC':
                        countaddress = countaddress+1
                    if ent.label_ =='FAC':
                        countaddress = countaddress+1
                
                countdate = 0
                for ent in reversed(doc.ents):
                    if ent.label_ == 'DATE':
                        countdate = countdate+1
                str=re.findall(r'\d{4} | [\d]{1,2}/[\d]{1,2}/[\d]{2,4} | Sun,| Mon,| Tue,| Wed,| Thu,| Fri,| Sat,| Jan | Feb | Mar | Apr| May | Jun | Jul | Aug | Sep | Oct | Nov | Dec ',datacount)
                for digit in str:
                    countdate = countdate+1

                countgender = 0
                r = re.compile(r'\A He | he |[Ss]he | [Hh]im| [Hh]is | [Hh]er | [Mm]en| [Ww]omen')
                str = r.findall(datacount)
                for digit in str:
                    countgender = countgender+1

                countphone = 0
                str=re.findall(r' \d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4} ',datacount)
                for digit in str:
                    countphone = countphone+1

                countconcept = 0
                for syn in wordnet.synsets(concept):
                    countconcept = countconcept+1
                

                total = 0
                total = countname + countaddress + countdate + countgender + countphone + countconcept
                
                # Source for file functions - https://realpython.com/working-with-files-in-python/
                # Writing stats to stats.txt in stats folder when stderr is provided
                if arg_ls[j+1] == 'stderr':
                    path = os.path.join('stats', 'stats.txt')
                    if not os.path.exists('stats'):
                        os.mkdir('stats')
                    with open('stats'+'/'+'stats'+'.txt','a') as statsfile:
                        sys.stdout = statsfile
                        print("\nRedacted Stats for input file:", i.format())
                        print("Names redacted:",countname)
                        print("Address redacted:",countaddress)
                        print("Dates redacted",countdate)
                        print("Genders redacted:",countgender)
                        print("Phonenumber redacted",countphone)
                        print("Concept Redacted",countconcept)
                
                # Printing the output of stats to console when stdout is provided
                if arg_ls[j+1] == 'stdout':
                    print("Redacted Stats for input file:", i.format())
                    print("Names redacted:",countname)
                    print("Address redacted:",countaddress)
                    print("Dates redacted",countdate)
                    print("Genders redacted:",countgender)
                    print("Phonenumber redacted",countphone)
                    print("Concept Redacted",countconcept)
