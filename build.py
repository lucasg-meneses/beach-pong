import subprocess
import sys
# Substitua as variáveis abaixo pelos seus valores
script_python = 'main.py'
nome_executavel = 'BeachPong'
caminho_icon = 'icon.ico'

# Construa o comando PyInstaller
comando_pyinstaller = [
    'pyinstaller',
    f'--name={nome_executavel}',
    f'--icon={caminho_icon}',
    '--noconsole',
    script_python
]

# Execute o comando usando subprocess
try:
    subprocess.run(comando_pyinstaller, check=True)
except subprocess.CalledProcessError as e:
    print(f"Erro ao executar PyInstaller: {e}")
