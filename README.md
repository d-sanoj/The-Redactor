# SANOJ DODDAPANENI
### Project 1 - The Redactor
**Introduction** - In this project, we need to collect all the text files in a specified folder and then redact all the names, addresses, dates, genders, phone numbers. Aditionally we need to redact the synonyms for a word using concepts function. For example, we need to redact the string movies in the file when string film is mentioned while execution. This project is developed using python and command line tools in Ubuntu.  
#### Sources -   
**_For entity redaction functions -_** _https://predictivehacks.com/redact-name-entities-with-spacy/_  
**_Regex founctions and sources:_**  
_Examples -_ _https://stackoverflow.com/questions/16699007/regular-expression-to-match-standard-10-digit-phone-number_  
_Tester_ - _https://www.regextester.com_  
**_File functions -_** _https://realpython.com/working-with-files-in-python/_  

**Installation directions -** In this project, we use the packages spacy, collections, re, nltk, glob, sys, os and nltk. These packages can be installed using the command below replacing [package_name] with the package that is to be installed. These packages will be imported according to requirement.  
**pipenv install [package_name]**  

#### Project Description -
**redactor.py file -** This file is provided in the project1 directory which constains the functions and execution code for the program for desired output. Each function is further explained below.

**read_text() function -** This function will read the textfile that is spcified in a folder and convert it into the desired format for further redaction process.

**redact_names() function -** This function takes the input from read_text() function and then using spacy package, name entities are recognized for the input and is marked with █ character.

**redact_address() function -** This function takes the input from the previous function and then using spacy module, GPE, LOC and FAC entities in the data are redacted with the █ character.

**redact_dates() function -** This function takes the input from the previous function and then using spacy, DATE entities are redated with █ character. Aditionally, regex expression for date formats -  
    ``` r'\d{4} | [\d]{1,2}/[\d]{1,2}/[\d]{2,4} | Sun,| Mon,| Tue,| Wed,| Thu,| Fri,| Sat,| Jan | Feb | Mar | Apr| May | Jun | Jul | Aug | Sep | Oct | Nov | Dec ' ```  
is used and the input file matching to the above expression is also masked with █.

**redact_genders() function -**  This function takes input from the previous called function and replaces the string with █ when matched with the format of regex expression -  ``` r'\A He | he |[Ss]he | [Hh]im| [Hh]is | [Hh]er | [Mm]en| [Ww]omen'. ```

**redact_phonenumber() function -** This function will take the input from the previous called function and then replaces the string when matched with the regex format below -  ``` r' \d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4} ' ```

**redact_concepts() function -** This function will take the input from the last called function and then using nltk package and lemmas, the synonym of the word mentioned during the execution of the program in command line and mask the synonyms with the character █.

Aditionally, code for to write complete masked data is written in main function. This data will take the masked data of each text file in a project1 folder, run the functions and then writes the redacted data into the [name].redacted file in files folder of project1 directory.

Further, code for stats is also written in main function, this will count the each occurance of the masked data in the input data according to each requirement names, dates, address, phone number, genders and concepts. During the execution, if we provide **stdout** for --stats, it will print the count of the masked data according to each file and their attributes as the terminal output. Alternatively, if we provide **stderr** for --stats, the count of maksed data of each file according to the file and attributes will be appended into the stats.txt file in folder stats in the directory project1.

To run the function, we need to run the command below in project1 directory -  
```    pipenv run python redactor.py --input '*.txt'      --input 'project1/.txt'                               --names                                                                                                                     --address                                                                                                                   --dates                                                                                                                     --genders                                                                                                                   --phones                                                                                                                   --concept 'film'                                                                                                           --output 'files/'                                                                                                           --stats stdout```  
In the command above, the word **film** can be replaced to find and mask synonym of any other word. and the word **stdout** which prints the data in console can be replaced with the word **stderr** to append the output to stats.txt file.

#### Test Cases - 
Here, we have created a new directory called **tests** and then created a file called **test_code.py** which contains different functions of test cases for each function in redactor.py. Each test case in the file is explained below accordingly.

Firstly, we import the packages sys to execute test file for all the directories of the project and provide the path accordingly and then import project1 folder and redactor.py within the folder and then finally we should import package pytest to run testcases accordingly. Pyest modules works on pytest framework and can be installed using the command below -  
```pipenv install pytest command.```

**test_readinput() function -** In this function, we test if there are existing files in project1 folder to be read as input. the test case will be passed if there are existing files for processing.

**test_names() function -** In this function, we declare a string and then call the function redact_names() from redactor.py and assert if the string is masked correctly. If the string declared in masked correctly, test case will be passed.

**test_address() function -** In this function, we declare a string of address and then call the function redact_address() from redactor.py and assert if the string is masked correctly. If the string declared in masked correctly, test case will be passed.

**test_dates() function -** In this function, we declare a string of address and then call the function redact_address() from redactor.py and assert if the string is masked correctly. If the string declared in masked correctly, test case will be passed.

**test_gender() function -** In this function, we declare a string from the regex expression of genders function and then call the function redact_genders() from redactor.py and assert if the string is masked correctly. If the string declared in masked correctly, test case will be passed.

**test_concept() function -** In this function, we declare a string of synonym for the word declared in variable data and then call the function redact_concepts() from redactor.py and assert if the string is masked correctly. If the string declared in masked correctly, test case will be passed.

**test_phone() function -** In this function, we declare a string of phone number and then call the function redact_phonenumber() from redactor.py and assert if the string is masked correctly. If the string declared in masked correctly, test case will be passed.

Here, Test cases can be executed using below command -  
``` pipenv run python -m pytest```

Once the command is passed, it will show the execution of test cases.

#### Possible Bugs -  
In the redactor.py program, we have used spacy module, this spacy module might not always be accurate to recognize the entities specified which could cause some data not being masked. Further, the count of concepts in the stats output might give return same values for all the text files being redacted. This bug only persists with count of stats starting from second text file.

At the end, these files are added, committed and pushed into git hub using git commands accordingly for each file.
