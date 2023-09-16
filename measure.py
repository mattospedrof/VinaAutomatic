import os
import math
from tqdm import tqdm
from Bio.PDB import PDBParser

def get_superscript(number):
    superscript_digits = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    return str(number).translate(superscript_digits)

def format_atom_id(atom, reverse_order=False):
    res_id = atom.get_parent().get_id()[1]
    res_name = atom.get_parent().get_resname()
    atom_name = atom.get_name()
    chain_id = atom.get_parent().get_parent().id
    
    formatted_res_id = get_superscript(res_id)
    
    if reverse_order:
        return f"- {atom_name} {res_name}{formatted_res_id}"
    else:
        return f"{chain_id} \t {res_name}{formatted_res_id} - {atom_name}"

def valid_pdbqt(description):
    while True:
        path_file = input(f"Enter the file name of the {description} with the '.pdbqt': ")
        if os.path.exists(path_file):
            return path_file
        print("File pdbqt not found. Please enter a valid name.")

receptor_file = valid_pdbqt("receptor")
ligand_file = valid_pdbqt("ligand")

parser = PDBParser(QUIET=True)

receptor_structure = parser.get_structure("receptor", receptor_file)
ligand_structure = parser.get_structure("ligand", ligand_file)

receptor_chain = input("Enter the chain of the receptor you want to analyze: ")
ligand_chain = input("Enter the chain of the ligand you want to analyze: ")
output_name = input(
                    "\nEnter the name of the output file you want without\n"
                    "the extension '.txt'. For example, 'distance_chain_A'"
                    ": "
                )

receptor_atoms = []
ligand_atoms = []
distances = []

for model in receptor_structure:
    for chain in model:
        if chain.id == receptor_chain:
            receptor_atoms.extend(chain.get_atoms())

for model in ligand_structure:
    for chain in model:
        if chain.id == ligand_chain:
            ligand_atoms.extend(chain.get_atoms())

def calculate_distance(atom1, atom2):
    x1, y1, z1 = atom1.get_coord()
    x2, y2, z2 = atom2.get_coord()
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

with open(f'{output_name}.txt', 'w') as f:
    f.write("Atoms at a distance of up to 3.6 Å between receptor and ligand:\n")
    f.write("\n")
    f.write("Chain \t Receptor \t Ligand \t Distance \n")

    with tqdm(total=(len(receptor_atoms) * len(ligand_atoms) / len(receptor_atoms) + len(ligand_atoms)), ncols=100, leave = False, dynamic_ncols= True) as pbar:
        for receptor_atom in receptor_atoms:
            for ligand_atom in ligand_atoms:
                distance = calculate_distance(receptor_atom, ligand_atom)
                if distance <= 3.6:
                    formatted_ligand_atom = format_atom_id(ligand_atom, reverse_order=True)
                    f.write(f"{format_atom_id(receptor_atom)} \t {formatted_ligand_atom} \t {distance:.1f} Å\n")
                    distances.append(distance)
            pbar.update(1)
    
    if distances:
        med_distance = sum(distances) / len(distances)
        f.write("\n")
        f.write(f"The average distance is {med_distance:.1f} Å\n")
    else:
        f.write("No distance less than or equal to 3,6 Å.")

print(
    "\nYour distance data has been successfully exported.\n"
    f"Check the output file {output_name}.txt.\n"
    "For any question, visit the github:\n"
    "https://github.com/mattospedrof/Automatic-Autodock-Vina"
)