import pygame

class Player:
    """Clase que representa la nave espacial del jugador."""
    
    def __init__(self, x, y, velocidad):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.velocidad = velocidad

    def mover(self, keys):
        """Mueve la nave con las teclas de dirección."""
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.velocidad
        if keys[pygame.K_d] and self.rect.x < 800 - self.rect.width:
            self.rect.x += self.velocidad
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.velocidad
        if keys[pygame.K_s] and self.rect.y < 600 - self.rect.height:
            self.rect.y += self.velocidad

    def dibujar(self, pantalla):
        """Dibuja la nave en la pantalla."""
        pygame.draw.rect(pantalla, (0, 255, 0), self.rect)