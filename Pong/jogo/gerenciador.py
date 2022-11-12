"""Realiza a orquestração do jogo e invoca os objetos."""
import time

import pygame

from .objetos.bola import Bola
from .objetos.tela import Tela
from .objetos.placar import Placar
from .objetos.paleta import Paleta

class Gerenciador:
    def __init__(self) -> None:
        self.tela = Tela()     # tela voltou para o construtor
        self.placar = Placar() # inicializa o placar zerado
        self.inicia_partida()

    def inicia_partida(self):
        self.paletas = [
            Paleta([20, 125], pygame.K_w, pygame.K_s),
            Paleta([570, 125], pygame.K_UP, pygame.K_DOWN)
        ]
        self.bola = Bola()

    def roda_loop(self):
        while True:
            cliques = self.monitora_cliques()
            if pygame.QUIT in cliques:
                break

            self.trata_teclas_pressionadas()
            self.bola.movimenta()

            # se o método atualiza() retorna True, é porque houve uma
            # pontuação, e o jogo precisa ser reposicionado
            if self.placar.atualiza(self.paletas, self.bola):
                time.sleep(0.5)         # aguarda 0.5 segundos
                self.inicia_partida()   # reposiciona paletas e bola

            self.aumenta_vel()
            if self.placar.p1 >= 5:
                self.tela.renderiza(self.paletas, self.bola, self.placar)
                time.sleep(1)
                break
            if self.placar.p2 >= 5:
                self.tela.renderiza(self.paletas, self.bola, self.placar)
                time.sleep(1)
                break

            # atualizada a chamada do método para incluir o placar
            self.tela.renderiza(self.paletas, self.bola, self.placar)

            pygame.time.Clock().tick(60)


    def trata_teclas_pressionadas(self):
        teclas = pygame.key.get_pressed()
        for paleta in self.paletas:
            paleta.movimenta(teclas)

    def aumenta_vel(self):
        if self.bola.posicao[0] == 35 or self.bola.posicao[0] == 565:
            self.bola.velocidade += 1
            for paleta in self.paletas:
                paleta.altura -= 10

    @staticmethod
    def monitora_cliques():
        cliques = []
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cliques.append(pygame.QUIT)

        return cliques