import os
import send2trash

# Limpar a pasta %temp%
temp_folder = os.path.join(os.environ.get('TEMP'))
for file_name in os.listdir(temp_folder):
    file_path = os.path.join(temp_folder, file_name)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            send2trash.send2trash(file_path)
    except Exception as e:
        print(f'Falha ao deletar o arquivo {file_path}. Erro: {e}')

# Esvaziar a lixeira do computador
send2trash.send2trash(os.path.expanduser('~/.local/share/Trash/files'))
