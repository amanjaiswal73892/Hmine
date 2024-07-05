# Hmine

This is a port of the Hmine algorithm in Python.

## Requirements: 
Some sample datasets are given:
  1. Market_Basket_Optimisation.txt
  2. Random_Test.txt
  3. Chess_data.txt

> Any `.txt` dataset with items separated by delimiter (space) `" "` can be used.
          
 The Project_Main.py runs both the H_mine and Apriori algorithms for all three datasets and
  outputs the result into files.
 
## To Run the program :
 
 1. Open Terminal(Mac) or Cmd(Windows).

 2. Change your directory to the same directory where the program is stored.

      Command: cd /path/to/program

 3.  Enter The Command:
    
    python Project_Main.py  
     
 4. After Running, the Program will read all the 3 datasets one by one and run H-mine and 
    Apriori with arbitrary value of minimum_support given in the file. 

 5. The output file is generated indicating the name of the dataset and the algorithm
    used. Confirmation of storage is given in the terminal with a prompt.

 NOTE: Only 5 files are generated since the Apriori algorithm is not triggered for chess.txt.



Instruction: To Run algorithm H_Mine_Algo.py or Apriori_Algo.py Invidually.

>NOTE: Python interactive shell is used to run the runHmine() or runApriori().

## To Run the module :
 
 1. Open Terminal(Mac) or Cmd(Windows).

 2. Change your directory to the same directory where the program is stored.

      Command: cd /path/to/program
      Command: "python" (to enter python interactive shell)
      NOTE: use "pyhton3" for Bluenose

 3.  Enter The following Command in python interactive shell:

     `import Apriori_Algo`
     
     `import H_Mine_Algo`
  
     Apriori_Algo() and H_Mine_Algo() takes 3 parameters:
  
     1) Input_file_name.txt
     2) Output_file_name.txt
     3) Relative support (Valid range 0<x<1)
  
     For example,
  
     `Apriori_Algo.runApriori("Random_Test.txt","Random_Test_Out.txt",0.1)`
  
     `H_Mine_Algo.runHmine("Random_Test.txt","Random_Test_Out.txt",0.1)`
       
     
 5. After Running, the program will read the input file and run the corresponding
    algorithm with the given minimum_support. 

 6. The output file is generated with the given name. If completed successfully, the Program 
    will print a completion message.




# CONTACT INFO                          
Email: aman.jaiswal.dal.ca

