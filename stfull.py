import subprocess
import re
import os

# Script 1: Executar o docking

# Caminho para o executável do Vina
VINAPATH = "/usr/bin/vina"

# Caminho para o arquivo do ligante
LIGAND_FILE = "/caminho/para/o/ligante/nome_do_ligante.pdbqt"

# Caminho para o arquivo do receptor
RECEPTOR_FILE = "/caminho/para/o/ligante/nome_do_receptor.pdbqt"

# Prefixo para os arquivos de saída gerados pelo Vina
OUTPUT_PREFIX = "output_docking"

# Número de rodadas a serem executadas
NUM_ROUNDS = 23

# Parâmetros de configuração para o docking
CENTER_X = 66.814
CENTER_Y = 77.135
CENTER_Z = 41.613
SIZE_X = 75.0
SIZE_Y = 75.0
SIZE_Z = 75.0
ENERGY_RANGE = 3
EXHAUSTIVENESS = 8

# Executar as rodadas de acoplamento
for i in range(1, NUM_ROUNDS + 1):
    print("Rodada", i)
    subprocess.run(
        [
            VINAPATH,
            "--receptor",
            RECEPTOR_FILE,
            "--ligand",
            LIGAND_FILE,
            "--out",
            f"{OUTPUT_PREFIX}_{i}.pdbqt",
            "--log",
            f"{OUTPUT_PREFIX}_{i}.log",
            "--center_x",
            str(CENTER_X),
            "--center_y",
            str(CENTER_Y),
            "--center_z",
            str(CENTER_Z),
            "--size_x",
            str(SIZE_X),
            "--size_y",
            str(SIZE_Y),
            "--size_z",
            str(SIZE_Z),
            "--energy_range",
            str(ENERGY_RANGE),
            "--exhaustiveness",
            str(EXHAUSTIVENESS),
        ]
    )

# Script 2: Processar resultados do docking

# Nome do arquivo de saída para os dados processados
output_file = "output_results.txt"

# Diretório de entrada contendo os arquivos de log do Vina
input_directory = "/caminho/para/o/diretório"

# Lista para armazenar os dados de afinidade
data = []

# Expressão regular para encontrar os dados de afinidade nos arquivos de log
pattern = r"\s+(\d+)\s+([-+]?\d*\.\d+|\d+)"

# Percorrer os arquivos de log na pasta de entrada
for i in range(1, 24):
    filename = f"output_docking_{i}.log"
    file_path = os.path.join(input_directory, filename)

    if os.path.isfile(file_path):
        round_num = str(i)
        first_round_occurrence = True  # Restaurar o valor para a próxima rodada

        with open(file_path, "r") as file:
            content = file.read()

            # Encontrar os dados de afinidade usando expressões regulares
            matches = re.findall(pattern, content)

            affinity_data = []
            for match in matches:
                mode = int(match[0])
                affinity = float(match[1])

                if first_round_occurrence:
                    affinity_data.append([round_num, mode, affinity])
                    first_round_occurrence = False
                else:
                    affinity_data.append(["", mode, affinity])

        data.extend(affinity_data)
        data.append([])  # Adicionar linha em branco para separar os conjuntos de dados

# Exportar os dados processados para o arquivo de saída
with open(output_file, "w") as file:
    file.write("Round\tMode\tAffinity\n")
    for row in data:
        if row:
            file.write("\t".join(str(item) for item in row) + "\n")
        else:
            file.write("\n")

print("Seus dados foram exportados com sucesso!!")
print("Verifique o arquivo output_table.txt")