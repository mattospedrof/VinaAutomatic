import subprocess
import re
import os
import configparser
import sys
import time


def run_docking(vina_path, ligand_file, receptor_file, output_prefix, center_x, center_y, center_z, size_x, size_y, size_z, energy_range, exhaustiveness, num_rounds):
    for i in range(1, num_rounds + 1):
        print(f"\nRodada: {i}\n")
        subprocess.run(
            [
                vina_path,
                "--receptor", receptor_file,
                "--ligand", ligand_file,
                "--out", f"{output_prefix}_{i}.pdbqt",
                "--log", f"{output_prefix}_{i}.log",
                "--center_x", str(center_x),
                "--center_y", str(center_y),
                "--center_z", str(center_z),
                "--size_x", str(size_x),
                "--size_y", str(size_y),
                "--size_z", str(size_z),
                "--energy_range", str(energy_range),
                "--exhaustiveness", str(exhaustiveness),
            ]
        )


def process_results(input_directory, num_rounds):
    # Diretório de entrada contendo os arquivos de log do Vina
    receptor_file = os.path.join(input_directory, "receptor.pdbqt")

    # Lista para armazenar os dados de afinidade
    data = []
    pattern = r"\s+(\d+)\s+([-+]?\d*\.\d+|\d+)"

    # Percorrer os arquivos de log na pasta de entrada
    for i in range(1, num_rounds + 1):
        filename = f"output_docking_{i}.log"
        file_path = os.path.join(input_directory, filename)

        if os.path.isfile(file_path):
            round_num = str(i)
            first_round_occurrence = True

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

    return data


def export_results(data, output_file):
    with open(output_file, "w") as file:
        file.write("Round\tMode\tAffinity\n")
        for row in data:
            if row:
                file.write("\t".join(str(item) for item in row) + "\n")
            else:
                file.write("\n")


def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return f"{days:02.0f}d {hours:02.0f}h {minutes:02.0f}min {seconds:02.0f}s"


def main():
    print('\nO seu docking já vai começar, aguarde!!')
    print('Obrigado pelo apoio!!')

    config_file = 'config.txt'

    if not os.path.isfile(config_file):
        print(f"Arquivo de configuração '{config_file}' não encontrado!")
        return

    config = configparser.ConfigParser()
    config.read(config_file)

    vina_path = config.get('Docking', 'vina_path')
    ligand_file = config.get('Docking', 'ligand')
    receptor_file = config.get('Docking', 'receptor')
    output_prefix = config.get('Docking', 'output_prefix')
    center_x = config.getfloat('Docking', 'center_x')
    center_y = config.getfloat('Docking', 'center_y')
    center_z = config.getfloat('Docking', 'center_z')
    size_x = config.getfloat('Docking', 'size_x')
    size_y = config.getfloat('Docking', 'size_y')
    size_z = config.getfloat('Docking', 'size_z')
    energy_range = config.getint('Docking', 'energy_range')
    exhaustiveness = config.getint('Docking', 'exhaustiveness')
    num_rounds = config.getint('Docking', 'num_rounds')

    total_time = 0
    start_time = time.time()

    for i in range(1, num_rounds + 1):
        print(f"\nRodada: {i}\n")
        round_start_time = time.time()

        subprocess.run(
            [
                vina_path,
                "--receptor", receptor_file,
                "--ligand", ligand_file,
                "--out", f"{output_prefix}_{i}.pdbqt",
                "--log", f"{output_prefix}_{i}.log",
                "--center_x", str(center_x),
                "--center_y", str(center_y),
                "--center_z", str(center_z),
                "--size_x", str(size_x),
                "--size_y", str(size_y),
                "--size_z", str(size_z),
                "--energy_range", str(energy_range),
                "--exhaustiveness", str(exhaustiveness),
            ]
        )

        round_end_time = time.time()
        round_time = round_end_time - round_start_time
        total_time += round_time

        estimated_time_remaining = (total_time / i) * (num_rounds - i)

        sys.stdout.write(f"\nÚltima Simulação: {round_time:.2f}s | Tempo Estimado Restante: {format_time(estimated_time_remaining)}\n")
        sys.stdout.flush()

    input_directory = os.path.dirname(receptor_file)
    data = process_results(input_directory, num_rounds)
    output_file = "output_results.txt"
    export_results(data, output_file)

    print("\nDocking 100% concluído")
    print("Dados exportados com sucesso!!")
    print("Verifique o arquivo output_results.txt")


if __name__ == "__main__":
    main()