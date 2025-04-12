import pygame
from src.core.game import Game

def mostrar_pantalla_carga(pantalla):
    """Muestra una pantalla de carga antes de iniciar el juego."""
    pantalla.fill((0, 0, 0))
    fuente = pygame.font.Font(None, 60)
    texto = fuente.render("Cargando...", True, (255, 255, 255))
    pantalla.blit(texto, (300, 250))
    pygame.display.flip()
    pygame.time.delay(2000)  # Simula el tiempo de carga

def configurar_juego():
    """Configura las opciones del juego antes de iniciarlo."""
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    mostrar_pantalla_carga(pantalla)  # Muestra pantalla de carga
    return pantalla

if __name__ == "__main__":
    pantalla = configurar_juego()  # Inicializa la pantalla con carga previa
    juego = Game()
    juego.bucle_principal()
