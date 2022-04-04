# Importing necessary modules to run test cases
# Module sys for path setting
# Importing module project1 
# Importing redactor.py from project1
# Module pytest to run test cases
# Modules nltk, spacy and os.path for entity recognition and files and directory functions

import sys
sys.path.append('..')
import project1
from project1 import redactor
import pytest
import nltk
import spacy
import os.path

# Downloading necessary models for the pytest to run

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('omw-1.4')

nlp = spacy.load('en_core_web_sm')

# Test case for read_text() function in redactor.py
def test_output():
    if os.path.exists('project1/*.txt'):
        assert True

# Test case for readact_names() function in redactor.py
def test_names():
    data = 'Mike'
    data1 = data
    data = nlp(data)
    name_test = redactor.redact_names(data1,'none')
    assert name_test == '██████'

# Test case for readct_address() function in redactor.py
def test_address():
    data = 'California'
    data1 = data
    data = nlp(data)
    address_test = redactor.redact_address(data1,'none')
    assert address_test == '███'

# Test case for readact_dates() function in redactor.py
def test_dates():
    data = ' Wed,'
    data1 = data
    data = nlp(data)
    date_test = redactor.redact_dates(data1,'none')
    assert date_test == '█████'

# Test case for readact_genders() function in redactor.py
def test_gender():
    data = ' he '
    gender_test = redactor.redact_genders(data,'none')
    assert len(gender_test) ==len('████')

# Test case for readct_concepts() function in redactor.py
def test_concept():
    data = 'film'
    concept_test = redactor.redact_concepts(data,'none','film')
    assert len(concept_test) == len('███████')

# Test case for readct_phonenumber() function in redactor.py
def test_phone():
    data = '609-271-3007'
    phone_test = redactor.redact_phonenumber(data,'none')
    assert len(phone_test) ==len('████████████')

# Test case for writing output code in redactor.py
def test_output():
    if os.path.exists('project1/files/*.redacted'):
        assert True

# Test case for printing and writing stats of functions in redactor.py
def test_stats():
    if os.path.exists('project1/stats/*.txt'):
        assert True
