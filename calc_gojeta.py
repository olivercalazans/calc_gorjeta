import sys
from tkinter     import filedialog, Tk
from dataclasses import dataclass, field


@dataclass(slots=True)
class Funcionario:
    funcao:     str       = None
    faltas:     list[int] = field(default_factory=list)
    descontos:  float     = 0
    adicionais: float     = 0
    total:      float     = 0



class CalculoGorjeta:

    def __init__(self):
        self._funcionarios: dict[str, Funcionario] = {}

    

    @staticmethod
    def _abortar(msg: str):
        print(f"[ ERRO ] {msg}")
        sys.exit(1)



    def execute(self):
        try:
            ...
        except Exception as e:
            self._abortar(e)



    @staticmethod
    def _pegue_caminho_arquivo() -> str:
        root = Tk()
        root.withdraw()
        
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione um arquivo",
            filetypes=(("Arquivos de texto", "*.xlsx"), ("Todos os arquivos", "*.*"))
        )
        
        return caminho_arquivo



    def _calcule_gorjeta_atendente(self):
        # Gorjeta do atendente 40% do valor feito
        ...




if __name__ == "__main__":
    cg = CalculoGorjeta()
    cg.execute()
