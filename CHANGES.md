# Changes
* **Repo not clone-able** --- I changes the repo name to the given name in the project description and the code is now clonable to run in any instance.
* **Code not executable** --- Updated the code to python 3.10.2 and added the Pipfile information with necessary modules and packages to run the code.
* **Output files not stored in respective folder** --- Made changes to the tree structure. Moved the redactor.py file and  the input files such as input.txt and input2.txt to the root directory of the project where the README.md exists for the execution. Now executing the code will redirect the output redacted files to the folder specified in the command while execution.
* **File names not re-assigned correctly** --- Made changes to the output file names from the format of [filename].txt.redacted to [filename].redacted where [filename] will take the complete name of input file including the format such input input.txt or input2.txt and will associate the .redacted format to it such as input.txt.redacted and input2.txt.redacted.
* **Missing Stats** --- Made changes to the stats file and removed the directory stats and saving the file from user input given in the command line except stdout and stderr. For example - If the command line is given as --stats statistics, it will create the statistics file with the redacted statistics written into it. If the command line is specified as --stats files/abc, it will create the abc file with the necessary information in the files directory. If stdout or stderr is given adter --stats, it will print the statistics to console and not write the statistics to any file
* **Missing/No Features Found for Dates, Concepts, Phone Number, Gender and Names** --- In this case, as the code was not executable, the functions were not working. Therefore, the changes made above will execute the code accordingly.

Tested the Test cases running from the main directory to verify the successful passing of test cases.

**The command to run the code is as below** ---  
```pipenv run python redactor.py --input '*.txt' --names --address --dates --genders --phones --concept 'film' --output 'files/' --stats stdout```

In the above command, we can replace 'film' with any other name to find synonyms and redact the sentence accordingly. Further, we can also replace files/ after output tag to any other name as name of directory to store redacted files. At the end, we can replace stdout to any other name which will create file and append the stats accordingly as mentioned in Missing Stats above.

**The command to run the test cases is as below** ---
```pipenv run python -m pytest```

**Successful execution of code** ---  
<img width="1435" alt="image"src="https://user-images.githubusercontent.com/31980486/164136335-4bcd6860-4139-44c5-884f-df035ab67812.png">  

**Successful execution of test cases** ---
<img width="1435" alt="image"src="https://user-images.githubusercontent.com/31980486/164139358-cafd86b8-0718-4e81-a7fb-783ad23f9359.png">  

**Tree Structure of the code** ---  
<img width="1435" alt="image"src="https://user-images.githubusercontent.com/31980486/164140518-ce5d28fb-9d88-479b-8b83-dc0652a877db.png">  

Changes have been made accordingly and the code has been pushed to the github and tag v2.0 is done.
