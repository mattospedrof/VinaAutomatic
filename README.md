![Badge em Desenvolvimento](https://img.shields.io/badge/Status-In_Development-darkblue)

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
This module extracts all the models from an output_docking, regardless of how many there are.
</p>

Running
- For Windows and Linux, run at the prompt command:
``` python
python div_output.py
```
The results will be exported to the directory.

# Div_files
<p style="text-align: justify;">
This module divides all output_docking files into folders for easy organization.
</p>

Running
- For Windows and Linux, run at the prompt command:
``` python
python div_files.py
```
The results are view in real time.

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

# Measure_membrane
<p style="text-align: justify;">
This module calculates distances specifically for cell membranes using all files, generating distance data for all models in output_docking format. Ions and other elements are not included for the time being. Due to the limitations of the conversion to PDBQT, phospholipids will only be described as DPP.
</p>

Running
- For Windows and Linux, run at the prompt command:
``` python
python measure_membrane.py
```
The results will be exported in each output_docking folder under legend_distance.

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
Don't forget to mention this repository in your methodology.
###

# Citation
<p style="text-align: justify;">
Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function, efficient optimization, and multithreading. J Comput Chem. 30 de janeiro de 2010;31(2):455–61.

Cock, P.J.A. et al. Biopython: freely available Python tools for computational molecular biology and bioinformatics. Bioinformatics 2009 Jun 1; 25(11) 1422-3 https://doi.org/10.1093/bioinformatics/btp163 pmid:19304878
</p>