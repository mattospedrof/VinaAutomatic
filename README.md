# Automatic-Vina
Linux script to run autodock and separate your generated data.

# Português
- Este script, escrito com o auxílio do ChatGPT, tem como objetivo facilitar a execução do Autodock Vina e a filtragem dos resultados de afinidade.
- Ele foi feito para ser executado no terminal do ubuntu, mas também funciona no WSL2 do windows. Lembre-se de estar em modo root
- Recomenda-se que os arquivos do receptor e do ligante estejam na mesma pasta/diretório. Além disso, não se esqueça de substituir as variáveis com seus respectivos caminhos. Caso esteja no WSL2, o caminho precisa ser correspondente ao que mostra no terminal.
- Está ajustado para 23 rodadas, o que gera 207 valores de afinidade, mas, caso queira mudar isso, basta apenas mudar
a variável NUM_ROUNDS com o número de rodadas que deseja e na porção "for i in range(1, 24)" troque o 24 pelo Nº +1. Por exemplo, se for 50, troque para 51.
- Lembre-se de verificar as permissões do diretório, através do comando 'ls -ld'.
- Caso não tenha permissôes de leitura e escrita, execute dentro do diretório o comando 'chmod +x stfull.py' ou 'chmod 777 stfull.py'.
- Após todas essas etapas, execute 'python3 stfull.py' e ele começará a rodar Vina. No final, todos os arquivos estarão na pasta/diretório informado.
- Qualquer sugestão, envie um email para francobiomed@gmail.com 

# English
- This script, written with the help of ChatGPT, aims to facilitate the execution of Autodock Vina and the filtering of affinity results.
- It was made to be run in ubuntu's terminal, but it also works under WSL2 on windows. Remember to be in root mode
- It is recommended that the receptor and ligand files are in the same folder/directory. Also, don't forget to replace the variables with their respective paths. If you are in WSL2, the path needs to match the one shown in the terminal.
- It is set to 23 rounds, which generates 207 affinity values, but if you want to change this, just change
the NUM_ROUNDS variable with the number of rounds you want and in the portion "for i in range(1, 24)" change the 24 to the Nr. +1. For example, if it is 50, change it to 51.
- Remember to check the permissions of the directory, using the command 'ls -ld'.
- If you do not have read and write permissions, run 'chmod +x stfull.py' or 'chmod 777 stfull.py'.
- After all these steps, run 'python3 stfull.py' and it will start running Vina. At the end, all the files will be in the folder/directory you entered.
- Any suggestions, send an email to francobiomed@gmail.com 
- 
