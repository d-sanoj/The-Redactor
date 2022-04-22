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
import en_core_web_md


# Downloading and loading necessary models for nltk and spacy running the program

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('omw-1.4')

nlp = en_core_web_md.load()
#nlp = spacy.load('en_core_web_sm')

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
    countname1 = 0
    for ent in reversed(doc.ents):
            if ent.label_ == 'PERSON':
                clean_text1 = clean_text1[:ent.start_char] + u"\u2588"*len(ent.label_) + clean_text1[ent.end_char:]
                countname1 = countname1+1
    return clean_text1, countname1

# Redacting addresses using spacy entity recognition
def redact_address(txt, inputfiles):
    clean_text2 = txt
    doc = nlp(txt)
    countaddress1 = 0
    for ent in reversed(doc.ents):
            if ent.label_ == 'GPE':
                clean_text2 = clean_text2[:ent.start_char] + u"\u2588"*len(ent.label_) + clean_text2[ent.end_char:]
                countaddress1 = countaddress1+1
            if ent.label_ == 'LOC':
                clean_text2 = clean_text2[:ent.start_char] + u"\u2588"*len(ent.label_) + clean_text2[ent.end_char:]
                countaddress1 = countaddress1+1
            if ent.label_ == 'FAC':
                clean_text2 = clean_text2[:ent.start_char] + u"\u2588"*len(ent.label_) + clean_text2[ent.end_char:]
                countaddress1 = countaddress1+1
    str=re.findall(r"^\s*\S+(?:\s+\S+){2}\s[a-zA-Z',.\s-]{1,25}\s\d{5}(?:[-\s]\d{4})?$",txt)
    for digit in str:
        countaddress1 = countaddress1 + 1
        clean_text2=re.sub('\\b{}\\b'.format(digit),'\u2588'*len(digit), clean_text2)
    return clean_text2, countaddress1

# Redacting dates using spacy entity recognition and regex
def redact_dates(txt, inputfiles):
    clean_text3 = txt
    doc = nlp(txt)
    countdate1 = 0
    for ent in reversed(doc.ents):
            if ent.label_ == 'DATE':
                countdate1 = countdate1+1
                clean_text3 = clean_text3[:ent.start_char] + u"\u2588"*len(ent.label_) + clean_text3[ent.end_char:]
    str=re.findall(r'\d{4} | [\d]{1,2}/[\d]{1,2}/[\d]{2,4} | Sun,| Mon,| Tue,| Wed,| Thu,| Fri,| Sat,| Jan | Feb | Mar | Apr| May | Jun | Jul | Aug | Sep | Oct | Nov | Dec ',txt)
    for digit in str:
        countdate1 = countdate1+1
        clean_text3=clean_text3.replace(digit,u"\u2588"*len(digit))
    return clean_text3, countdate1

# Redacting genders using regex
def redact_genders(txt, inputfiles):
    clean_text4 = txt
    countgender1 = 0
    str=re.findall(r'(\b[Hh]usband\b|\b[Ww]ife\b|\b[Mm]other\b|\b[Ff]ather\b|\b[Mm]om\b|\b[Dd]ad\b|\b[Ss]on\b|\b[Dd]aughter|\b[Hh]imself\b|\b[Hh]erself\b|\b[Gg]irl\b|\b[Bb]oy\b|\b[Ff]emale\b|\b[Mm]ale\b|\b[Hh]e\b|\b[Ss]he\b|\b[Hh]er\b|\b[Hh]im|\b[Hh]is\b|\b[Mm]en\b|\b[Ww]omen\b|\b[Ww]oman\b|\b[Mm]an\b)',txt)
    for digit in str:
        countgender1 = countgender1 + 1
        clean_text4=re.sub('\\b{}\\b'.format(digit),'\u2588'*len(digit), clean_text4)
    return clean_text4, countgender1

# Redacting phonenumbers using regex
def redact_phonenumber(txt, inputfiles):
    clean_text5 = txt
    countphone1 = 0
    str=re.findall(r' \d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4} ',txt)
    for digit in str:
        countphone1 = countphone1+1
        clean_text5=clean_text5.replace(digit,u"\u2588"*len(digit))
    return clean_text5, countphone1

# redacting synonyms using nltk wordnet and lemma
def redact_concepts(txt, inputfiles, concept):
    clean_text6 = txt
    countconcept1 = 0
    for syn in wordnet.synsets(concept):
        for l in syn.lemmas():
            sentence = clean_text6.splitlines()
            for line in sentence:
                if concept in line:
                    countconcept1 = countconcept1 + 1
                    clean_text6=clean_text6.replace(line,u"\u2588"*len(line))
    return clean_text6, countconcept1


# Main function to run above functions
arg_ls = sys.argv
allfiles=[]
totalcount = 0
countname = 0
countaddress = 0
countdate = 0
countgender = 0
countphone = 0
countconcept = 0
for i in range(len(arg_ls)):
    if arg_ls[i] == '--input':
        # Using glob to read input files
        allfiles.extend(glob.glob(arg_ls[i+1]))

for i in allfiles:
    data = read_text(i)
    for j in range(len(arg_ls)):
            if arg_ls[j] == '--names':
                data, countname = redact_names(data, i)

            if arg_ls[j] == '--address':
                data, countaddress = redact_address(data, i)

            if arg_ls[j] == '--dates':
                data, countdate = redact_dates(data, i)

            if arg_ls[j] == '--phones':
                data, countphone = redact_phonenumber(data, i)

            if arg_ls[j] == '--concept':
                data, countconcept = redact_concepts(data, i, arg_ls[j+1])
                concept = arg_ls[j+1]

            if arg_ls[j] == '--genders':
                data, countgender = redact_genders(data, i)

            # Writing output to a file in files director
            if arg_ls[j] == '--output':
                if not os.path.exists(arg_ls[j+1]):
                    os.mkdir(arg_ls[j+1])
                z = i.split('/')[-1]
                #with open(arg_ls[j+1]+z+'.redacted', 'w') as statsfile:
                    #sys.stdout = statsfile
                file = open(arg_ls[j+1]+z+'.redacted','w')
                #sys.stdout = file
                for x in data.splitlines():
                    x = data
                file.write(data)
                file.close()

            if arg_ls[j] == '--stats':  
                # Source for file functions - https://realpython.com/working-with-files-in-python/
                # Writing stats to user dedlared file in stats folder when stderr is provided
                if arg_ls[j+1] == 'stderr':
                    print("\nRedacted Stats for input file:", i.format())
                    print("Names redacted:",countname)
                    print("Address redacted:",countaddress)
                    print("Dates redacted",countdate)
                    print("Genders redacted:",countgender)
                    print("Phonenumber redacted",countphone)
                    print("Concept Redacted",countconcept)
                
                # Printing the output of stats to console when stdout is provided
                elif arg_ls[j+1] == 'stdout':
                    print("\nRedacted Stats for input file:", i.format())
                    print("Names redacted:",countname)
                    print("Address redacted:",countaddress)
                    print("Dates redacted",countdate)
                    print("Genders redacted:",countgender)
                    print("Phonenumber redacted",countphone)
                    print("Concept Redacted",countconcept)

                else:
                    path = os.path.join('stats', arg_ls[j+1])
                    with open(arg_ls[j+1],'a') as statsfile:
                        sys.stdout = statsfile
                        print("\nRedacted Stats for input file:", i.format())
                        print("Names redacted:",countname)
                        print("Address redacted:",countaddress)
                        print("Dates redacted",countdate)
                        print("Genders redacted:",countgender)
                        print("Phonenumber redacted",countphone)
                        print("Concept Redacted",countconcept)
                    statsfile.close()
