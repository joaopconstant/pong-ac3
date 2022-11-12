"""
Organiza as cores do projeto.
"""
from dataclasses import dataclass

@dataclass
class CORES:
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    vermelho = (255, 0, 0)

if __name__ == "__main__":
    print(CORES.branco)
