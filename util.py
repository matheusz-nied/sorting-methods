import os


def list_files():
    pasta = './'
    paths = []

    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.lower().endswith(".csv"):
                paths.append(os.path.join(diretorio, arquivo))

    return paths
