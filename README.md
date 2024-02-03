# Objective function for the RNA folding problem 
by *Ouhab ELKOUADI* and *Henes AMROUCHE*

The goal, using the following worflow, is to estimate the **Gibbs free energy**. Indeed it's on this measure that the **native folding** of a **RNA** chain is hold. We know that the native folding is associate with the lowest Gibbs free energy. 

The workflow is containing the following scripts, we advice to use python 3. Make sure to have all the packages from `requirements.txt` to use it.  

- `distances_calculator.py`:
    Reading and calculating interatomic distances. 
    The first code extracts data from PDB files and calculates interatomic distances between C3' atoms of different base pairs.
    It also provides a function to merge these distances from multiple files.
- `frequency_calculator.py`: Computing observed and reference frequencies:
The second code defines functions to compute observed frequencies of interatomic distances within specific intervals and reference frequencies based on given distance lists.
- `scoring_values.py`
- `ìnter_atomic_distances.py`
- `gibbs_free_energy.py`

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
