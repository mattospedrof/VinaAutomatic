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
    chain_id = atom.get_parent().get_parent().id if atom.get_parent().get_parent().id else "A"

    formatted_res_id = get_superscript(res_id)

    if reverse_order:
        return f"{atom_name}\t{res_name}{formatted_res_id}\t{chain_id}"
    else:
        return f"A\t{res_name}{formatted_res_id}\t{atom_name}"


def calculate_distance(atom1, atom2):
    x1, y1, z1 = atom1.get_coord()
    x2, y2, z2 = atom2.get_coord()
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


receptor_file = input(
    "Enter the file name of the receptor with the '.pdbqt': ")
while not os.path.exists(receptor_file):
    print("File pdbqt not found. Please enter a valid name.")
    receptor_file = input(
        "Enter the file name of the receptor with the '.pdbqt': ")
    
desired_distance = float(input("Enter the desired distance of investigation (Example: 3.6): ")[:5])
parser = PDBParser(QUIET=True)
receptor_structure = parser.get_structure("receptor", receptor_file)

receptor_atoms = []
for model in receptor_structure:
    for chain in model:
        if not hasattr(chain, 'id') or not chain.id:
            chain.id = 'A'
        receptor_atoms.extend(chain.get_atoms())

files_with_distances = []

for i in range(1, 24):
    folder_name = f"output_docking_{i}"
    if os.path.isdir(folder_name):
        os.chdir(folder_name)

        for file in os.listdir():
            if file.startswith(f"output_docking_{i}_") and file.endswith(".pdbqt"):
                parser = PDBParser(QUIET=True)
                ligand_structure = parser.get_structure("ligand", file)
                ligand_atoms = []

                for model in ligand_structure:
                    for chain in model:
                        ligand_atoms.extend(chain.get_atoms())

                distances = []
                file_id = file.replace("output_docking_", "").replace(".pdbqt", "")
                output_name = f"distance_{file_id}.txt"

                with open(output_name, 'w', encoding='utf-8') as o:
                    o.write(f"Atoms at a distance of up to {desired_distance} Å between receptor and ligand:\n\n")
                    o.write("Chain_r\tAA_r\tAtom_r\tAtom_l\tAA_l\tChain_l\tDistance\n")

                    results = []
                    for receptor_atom in receptor_atoms:
                        for ligand_atom in ligand_atoms:
                            distance = calculate_distance(receptor_atom, ligand_atom)
                            if distance <= desired_distance:
                                res_id_lig = ligand_atom.get_parent().get_id()[1]
                                line = f"{format_atom_id(receptor_atom)}\t{format_atom_id(ligand_atom, reverse_order=True)}\t{distance:.2f}Å"
                                results.append((res_id_lig, line))
                                distances.append(distance)

                    results.sort(key=lambda x: x[0])

                    for _, line in results:
                        o.write(f"{line}\n")

                    if distances:
                        med_distance = sum(distances) / len(distances)
                        o.write("\n")
                        o.write(f"The average distance is {med_distance:.1f}Å\n")
                        files_with_distances.append(os.path.join(folder_name, output_name))
                    else:
                        o.write(f"No distance less than or equal to {desired_distance} Å.")

                print(f"Check the output file {output_name}.")

        os.chdir("..")


legend_name = f"legend_general"
with open(legend_name, 'w') as t:
    t.write("Chain_r = Chain_receptor\n")
    t.write("AA_r = Aminoacid_receptor\n")
    t.write("Atom_r = Atom_receptor\n")
    t.write("Atom_l = Atom_ligand\n")
    t.write("AA_l = Aminoacid_ligand\n")
    t.write("Chain_l = Chain_ligand\n\n")

    print(f"\nCheck the output file {legend_name} for increase in your text.\n")
print("\nSummary of files with distance data:")

if files_with_distances:
    with open("summary_files_distances.txt", "w", encoding="UTF-8") as s:
        for file_path in files_with_distances:
            s.write(f"- {file_path}\n")
            print(f"- {file_path}")
else:
    print("No files contained distances within the threshold.")
