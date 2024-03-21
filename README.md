# Autovina
<p style="text-align: justify;">
This python-designed module aims to automate docking simulations using Autodock-Vina in order to minimize the time it takes to carry out extensive simulations.
</p>

Requirements of run:
- Vina version 1.1.2 or later.
- Python version 3.8 or later for Windows system and Python3 version 3.7 for Linux system.
- Replace in the config file the parameters and file names according to your docking system.
- In the variable 'vina_path', you must put the path to vina, for example:
```
vina_path = /usr/bin/vina
```

Running
- For Windows, run at the prompt command:
``` python
python autovina.py
```
- For linux or wsl2, run at the prompt command:
``` python
python3 autovina.py
```
The results will be exported to the directory where the script is run.

# Div_output
<p style="text-align: justify;">
This module aims to obtain specific models of a docking result. So far, only one model can be obtained at a time. Note that the output file will contain the round number and the model number. For example, if a simulation had 30 rounds, and you want model 7 from round 20, the output file for this module will be 'output_docking_20_7.pdbqt'.
</p>

Running
- For Windows and Linux, run at the prompt command:
``` python
python div_output.py
```
The results will be exported to the directory where the script is run.

# Measure
<p style="text-align: justify;">
This module performs the Euclidean calculation of atomic distances between receptor and ligand. To visualize them, use the Pymol software, for example (https://pymol.org/). So far, the script supports choosing one receptor chain at a time.
</p>

Running
- For Windows and Linux, run at the prompt command:
``` python
python measure.py
```
The results will be exported to the directory where the script is run.

# Analysis
This module has two functions:
- Transform the results of the measure module into an Excel spreadsheet.
- Create a boxplot graph of the distance measurements using python's matplotlib library. In the future, the code will analyze several plots at the same time.

Running
- For Windows and Linux, run at the prompt command:
``` python
python analysis.py
```
The results will be exported to the directory where the script is run.

###
For any problems or suggestions, send an email to (francobiomed@gmail.com).
###

# Citation
<p style="text-align: justify;">
Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function, efficient optimization, and multithreading. J Comput Chem. 30 de janeiro de 2010;31(2):455–61.
</p>