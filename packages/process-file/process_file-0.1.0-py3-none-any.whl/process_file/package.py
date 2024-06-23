import sys
import os
import psutil


class ProcessInfo:
    def __init__(self):
        self.pid = os.getpid()
        self.nome_app = os.path.basename(sys.executable)  # Obtém o nome do executável .exe
        self.diretorio_app = sys.executable  # Obtém o diretório do executável
        self.public_ip = self.get_public_ip()

    def pid_exists(self, pid: str):
        """Verifica se um PID existe na lista de processos."""
        for proc in psutil.process_iter(['pid']):
            if proc.pid == pid:
                return True
        return False

    def get_pid(self):
        return self.pid

    def get_diretorio_app(self):
        return self.diretorio_app

    def get_nome_app(self):
        return self.nome_app

    def get_public_ip(self):
        try:
            # Implementação para obter o IP público
            return "IP Público Aqui"
        except Exception:
            return None

    def encerrar_processo_atual(self):
        try:
            os.kill(os.getpid(), 9)
        except Exception as e:
            print(f"Falha ao encerrar o processo: {e}")

    def is_process_on(self, nome_app: str, caminho_absoluto: str) -> bool:
        cont = 0
        for proc in psutil.process_iter(attrs=['pid', 'name', 'exe']):
            try:
                if proc.name() == nome_app and os.path.abspath(proc.exe()) == caminho_absoluto:
                    cont += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                pass

        if cont > 2:
            return True

        return False
