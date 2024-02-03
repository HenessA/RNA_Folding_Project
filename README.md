# Objective function for the RNA folding problem 
by *Ouhab ELKOUADI* and *Henes AMROUCHE*

The goal, using the following worflow, is to estimate the **Gibbs free energy**. Indeed it's on this measure that the **native folding** of a **RNA** chain is hold. We know that the native folding is associate with the lowest Gibbs free energy. 

The workflow is containing the following scripts, we advice to use python 3. Make sure to have all the packages from `requirements.txt` to use it.  

- `distances_calculator.py`:
    **Reading and calculating interatomic distances** 
    The first code extracts data from PDB files and calculates interatomic distances between C3' atoms of different base pairs.
    It also provides a function to merge these distances from multiple files.
- `frequency_calculator.py`: **Computing observed and reference frequencies**
The second code defines functions to compute observed frequencies of interatomic distances within specific intervals and reference frequencies based on given distance lists.
- `scoring_values.py`: **Calculating and writing score values**
The third code implements functions to compute score values based on observed and reference frequencies, then writes them to CSV and TXT files.
- `ìnter_atomic_distances.py`: **Reading and computing score values for filtered distances**
The fourth code reads score values from files and calculates scores for filtered interatomic distances using these score values.
- `gibbs_free_energy.py`: **Estimating Gibbs free energy**
The final code coodinates the entire process by computing interatomic distances, filtering distances, calculating scores for filtered distances, and ultimately estimating Gibbs free energy based on the calculated scores.

## Installation
To get all the repository files : 
```
git clone https://github.com/HenessA/RNA_Folding_Project/tree/main
```
Then go to the directory that contain and check : 
```
cd RNA_Folding_Project
ls
```
Follow the next step, in guideline...
## Guideline
Follow the command line in the following order :
```
python3 inter_atomic_distances.py
```
```
python3 gibbs_free_energy.py
```
## Visualization 
Import the `plotting.Rmd` script and set the working directory that contain the .csv files (*_scoring_values.csv) in RStudio, then run the script to get the plot such as following (for each considered pair, here 10 plots) : 

![image](https://github.com/HenessA/RNA_Folding_Project/assets/94346915/6871bd4f-ee26-49b5-a6c1-44556e1ef64f)
![image](https://github.com/HenessA/RNA_Folding_Project/assets/94346915/8abc0ecf-5caa-4faf-9811-980e04a4a41c)
![image](https://github.com/HenessA/RNA_Folding_Project/assets/94346915/1c0b2727-d61b-436f-9dd9-bf439e43d469)



