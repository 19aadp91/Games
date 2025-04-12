import pygame
import random

class Enemy:
    """Clase que representa a un enemigo en el juego."""

    def __init__(self, x, y, velocidad):
        self.rect = pygame.Rect(x, y, 40, 40)  # Tamaño del enemigo
        self.velocidad = velocidad

    def mover(self):
        """Mueve el enemigo verticalmente."""
        self.rect.y += self.velocidad

        # Reiniciar la posición si sale de la pantalla
        if self.rect.y > 600:
            self.rect.y = 0
            self.rect.x = random.randint(0, 760)  # Posición aleatoria al reiniciar

    def dibujar(self, pantalla):
        """Dibuja el enemigo en la pantalla."""
        pygame.draw.rect(pantalla, (255, 0, 0), self.rect)  # Color rojo