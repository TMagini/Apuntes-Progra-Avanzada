from collections import deque


class Repositorio:

    def __init__(self, archivos=[]):
        self.archivos_remotos = []
        self.archivos_locales = archivos
        self.cola = deque()

    def git_add(self, archivos):
        if type(archivos) == list:
            for c in archivos:
                if c in self.archivos_locales:
                    print(f'El archivo {c} se encuentra repetido en tu repositorio\nSe eliminará')
                    archivos.remove(c)
                else:
                    self.archivos_locales.append(c)

            print('Ya puede hace commit, no se encuentra ningún archivo repetido')

        else:
            if archivos in self.archivos_locales:
                print(f'El archivo {archivos} se encuentra repetido en tu repositorio\n \
                    Se eliminará')
            else:
                self.archivos_locales.append(archivos)

    def git_commit(self, comentario):
        print(comentario)
        for c in self.archivos_locales:
            if c not in self.archivos_remotos:
                self.cola.append(c)

    def git_push(self):
        while len(self.cola) > 0:
            self.archivos_remotos.append(self.cola.popleft())


if __name__ == "__main__":
    mi_repo = Repositorio(["main.py", "windows.py", "user.txt"])
    mi_repo.git_add('README.md')
    mi_repo.git_commit('Agregado el README :D')
    mi_repo.git_push()
    print(mi_repo.archivos_remotos)
    mi_repo.git_add(["data.json", "client.py", "user.txt"])
    mi_repo.git_commit("subiendo datos")
    mi_repo.git_push()
    print(mi_repo.archivos_remotos)
