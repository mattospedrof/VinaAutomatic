import os
import math
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
        return f"{atom_name}\t{res_name}{formatted_res_id}\t{chain_id}"
    else:
        return f"{chain_id}\t{res_name}{formatted_res_id}\t{atom_name}"


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


with open(f'{output_name}.txt', 'w', encoding='utf-8') as f:
    f.write("Atoms at a distance of up to 3.6 Å between receptor and ligand:\n")
    f.write("\n")
    f.write("Chain_r\tAA_r\tAtom_r\tAtom_l\tAA_l\tChain_l\tDistance\n")

    for receptor_atom in receptor_atoms:
        for ligand_atom in ligand_atoms:
            distance = calculate_distance(receptor_atom, ligand_atom)
            if distance <= 3.6:
                formatted_ligand_atom = format_atom_id(ligand_atom, reverse_order=True)
                f.write(f"{format_atom_id(receptor_atom)}\t{formatted_ligand_atom}\t{distance:.2f}Å\n")
                distances.append(distance)

    if distances:
        med_distance = sum(distances) / len(distances)
        f.write("\n")
        f.write(f"The average distance is {med_distance:.1f}Å\n")
    else:
        f.write("No distance less than or equal to 3,6 Å.")

with open(f'legend_{output_name}.txt', 'w') as t:
    t.write("Chain_r = Chain_receptor\n")
    t.write("AA_r = Aminoacid_receptor\n")
    t.write("Atom_r = Atom_receptor\n")
    t.write("Atom_l = Atom_ligand\n")
    t.write("AA_l = Aminoacid_ligand\n")
    t.write("Chain_l = Chain_ligand\n\n")
    t.write("If you want, use '⁰¹²³⁴⁵⁶⁷⁸⁹' ")

if os.path.exists(output_name):
    print(
        "\nYour distance data has been successfully generated!\n"
        f"Check the output file {output_name}.txt\n"
        "Check the output of legend for more info."
        " "
        "For any question, visit the github:\n"
        "https://github.com/mattospedrof/Automatic-Autodock-Vina"
        " "
        "Mattos Tech ~ 2024."
    )
else:
    print(
        "Oops, something happened, go to the repository so I can help you.\n"
        "https://github.com/mattospedrof/Automatic-Autodock-Vina"
    )
