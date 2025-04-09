import os
import configparser


def read_pdbqt(name_archive_pdbqt, output_prefix):
    with open(name_archive_pdbqt, 'r') as origin_pdbqt:
        content_in_origin = origin_pdbqt.read()

    model_number = 1
    while True:
        init_model = content_in_origin.find(f"MODEL {model_number}")
        if init_model == -1:
            break
        
        next_model = content_in_origin.find("MODEL ", init_model + 1)
        end_model = next_model if next_model != -1 else len(content_in_origin)
        excerpt_model = content_in_origin[init_model:end_model].strip()

        name_desired_file = f"{output_prefix}_{model_number}.pdbqt"
        with open(name_desired_file, 'w') as desired_file:
            desired_file.write(excerpt_model)
        
        print(f"The model excerpt {model_number} was written in the file {name_desired_file}.")
        model_number += 1


config = configparser.ConfigParser()
config.read("config.txt")
number_rounds = config.getint('Docking', 'num_rounds') + 1

for n in range(1, number_rounds):
    origin_pdbqt = f"output_docking_{n}.pdbqt"
    if os.path.exists(origin_pdbqt):
        output_prefix = f"output_docking_{n}"
        read_pdbqt(origin_pdbqt, output_prefix)
    else:
        print(f"The file '{origin_pdbqt}' does not exist.")

print("Files successfully divided by models.")
