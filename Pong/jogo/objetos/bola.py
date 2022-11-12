import math
import random
import pygame

from jogo.cores import CORES

class Bola:
    velocidade = 5

    def __init__(self):
        self.posicao = [300, 200]
        self.direcao = self.cria_vetor_unitario()

    def cria_vetor_unitario(self):
        while True:
            dir_x = random.uniform(-1, 1)
            if int(self.velocidade * dir_x) and dir_x not in [-1, 1]:
                break

        dir_y = random.choice([-1, 1]) * math.sqrt(1 - dir_x ** 2)
        return [dir_x, dir_y]

    def movimenta(self):
        self.posicao = [
            int(self.posicao[0] + self.velocidade * self.direcao[0]),
            int(self.posicao[1] + self.velocidade * self.direcao[1])
        ]
        self.verifica_colisoes()

    def verifica_colisoes(self):
        if self.posicao[1] > 395:
            self.direcao[1] *= -1
            self.posicao[1] = 395
        if self.posicao[1] < 5:
            self.direcao[1] *= -1
            self.posicao[1] = 5

        if self.posicao[0] < 35:
            self.direcao[0] *= -1
            self.posicao[0] = 35
        if self.posicao[0] > 565:
            self.direcao[0] *= -1
            self.posicao[0] = 565

    def desenha(self, tela):
        pygame.draw.circle(
            tela,
            CORES.branco,
            self.posicao,
            5
        )
