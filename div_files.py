import os
import shutil
import configparser

config = configparser.ConfigParser()
config.read("config.txt")
number_rounds = config.getint('Docking', 'num_rounds') + 1
number_models = config.getint('Docking', 'exhaustiveness') + 2

for i in range(1, number_rounds):
    folder_name = f"output_docking_{i}"
    os.makedirs(folder_name, exist_ok=True)
    
    pdbtq_one_file = f"output_docking_{i}.pdbqt"
    pdbqt_log_file = f"output_docking_{i}.log"
    
    if os.path.exists(pdbtq_one_file):
        shutil.move(pdbtq_one_file, os.path.join(folder_name, pdbtq_one_file))
    if os.path.exists(pdbqt_log_file):
        shutil.move(pdbqt_log_file, os.path.join(folder_name, pdbqt_log_file))

    for j in range(1, number_models):
        pdbqt_file = f"output_docking_{i}_{j}.pdbqt"
        if os.path.exists(pdbqt_file):
            shutil.move(pdbqt_file, os.path.join(folder_name, pdbqt_file))

print("Files grouped and moved successfully!")
