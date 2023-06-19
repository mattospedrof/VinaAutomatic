# Automatic-Vina
Linux script to run autodock and separate your generated data.

# Português
- Este script, escrito com o auxílio do ChatGPT, tem como objetivo facilitar a execução do Autodock Vina e a filtragem dos resultados de afinidade.
- Ele foi feito para ser executado no terminal do ubuntu, mas também funciona no WSL2 do windows.
- Os arquivos do receptor e ligante devem estar no diretório e seus nomes no arquivo de config.
- Está ajustado para 23 rodadas, o que gera 207 modelos de encaixe, mas, caso queira mudar isso, apenas altere o número da variável "NUM_ROUNDS"
- Lembre-se de verificar as permissões do diretório, através do comando 'ls -ld'.
- Caso não tenha permissôes de leitura e escrita, execute dentro do diretório o comando 'chmod +x stfull_v2.py'.
- Após todas essas etapas, execute 'python3 stfull_v2.py' e ele começará a rodar Vina. No final, todos os arquivos estarão na pasta/diretório informado
- Verifique os arquivos de saída e o arquivo com os valores de afinidade. 
 
Exemplo de como deve ser o arquivo config do vina:

[Docking]
receptor = receptor.pdbqt
ligand = ligante.pdbqt
output_prefix = output_docking
center_x = 0.000
center_y = 0.000
center_z = 0.000
size_x = 60
size_y = 60
size_z = 60
energy_range = 3
exhaustiveness = 8
num_rounds = 23
vina_path = /usr/bin/vina

Lembre-se de substituir a variável vina_path pelo caminho do Vina, conforme especificado em seu sistema operacional.
