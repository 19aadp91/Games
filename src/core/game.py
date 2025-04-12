import pygame
import random
from src.entities.player import Player
from src.ui.menu import Menu
from src.entities.enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.jugador = Player(375, 500, 5)
        self.en_pausa = False
        self.enemigos = [Enemy(random.randint(0, 760), random.randint(0, 300), 3) for _ in range(5)]
        self.ejecutando = True
        self.en_menu = True  # Comienza en el menú
        self.menu = Menu(self.pantalla)

    def bucle_principal(self):
        while self.ejecutando:
            if self.en_menu:
                accion = self.menu.manejar_eventos()
                if accion == "start_game":
                    self.en_menu = False
                elif accion == "exit":
                    self.ejecutando = False
                self.menu.dibujar()
            else:
                self.manejar_eventos()
                self.actualizar()
                self.dibujar()
            self.clock.tick(60)

    def manejar_menu(self):
        """Muestra el menú y detecta si el usuario quiere jugar o salir."""
        accion = self.menu.manejar_eventos()
        if accion == "start_game":
            self.en_menu = False
        elif accion == "exit":
            self.ejecutando = False
        self.menu.dibujar()

    def manejar_eventos(self):
        """Manejo de eventos durante el juego."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.ejecutando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pausar con la tecla 'P'
                    self.en_pausa = not self.en_pausa  # Alternar pausa

    def actualizar(self):
        if self.en_pausa:
            return
        """Actualiza la posición del jugador y de los enemigos."""
        keys = pygame.key.get_pressed()
        self.jugador.mover(keys)

        for enemigo in self.enemigos:
            enemigo.mover()

            # Detección de colisión entre jugador y enemigo
            if self.jugador.rect.colliderect(enemigo.rect):
                self.fin_juego()  # Si hay colisión, termina el juego

    def dibujar(self):
        """Dibuja todos los elementos del juego en pantalla."""
        self.pantalla.fill((0, 0, 0))
        self.jugador.dibujar(self.pantalla)

        for enemigo in self.enemigos:
            enemigo.dibujar(self.pantalla)

        if self.en_pausa:  # Si está en pausa, muestra un mensaje
            fuente = pygame.font.Font(None, 60)
            texto1 = fuente.render("PAUSA", True, (255, 255, 255))
            texto2 = fuente.render("Presiona P para continuar", True, (255, 255, 255))
            self.pantalla.blit(texto1, (300, 250))
            self.pantalla.blit(texto2, (200, 320))

        pygame.display.flip()
    
    def fin_juego(self):
        """Muestra pantalla de fin de juego con opciones de Reiniciar o Salir."""
        fuente = pygame.font.Font(None, 60)
        opcion_seleccionada = 0
        opciones = ["Reiniciar", "Salir"]

        while True:
            self.pantalla.fill((30, 30, 30))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
                    if event.key == pygame.K_UP:
                        opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
                    if event.key == pygame.K_RETURN:
                        if opcion_seleccionada == 0:  # Reiniciar
                            self.__init__()  # Reinicia la instancia del juego
                            return
                        elif opcion_seleccionada == 1:  # Salir
                            pygame.quit()
                            exit()

            # Mostrar opciones en pantalla
            for i, opcion in enumerate(opciones):
                color = (255, 255, 255) if i != opcion_seleccionada else (255, 0, 0)
                texto = fuente.render(opcion, True, color)
                self.pantalla.blit(texto, (300, 250 + i * 60))

            pygame.display.flip()


if __name__ == "__main__":
    juego = Game()
    juego.bucle_principal()
