import pygame

class Menu:
    """Clase para manejar el menú principal del juego."""

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fuente = pygame.font.Font(None, 50)
        self.opciones = ["Jugar", "Salir"]
        self.opcion_seleccionada = 0

    def manejar_eventos(self):
        """Detecta eventos en tiempo real."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.KEYDOWN:  # Solo detecta cuando una tecla es PRESIONADA
                if event.key == pygame.K_DOWN:
                    self.opcion_seleccionada = (self.opcion_seleccionada + 1) % len(self.opciones)
                if event.key == pygame.K_UP:
                    self.opcion_seleccionada = (self.opcion_seleccionada - 1) % len(self.opciones)
                if event.key == pygame.K_RETURN:
                    if self.opcion_seleccionada == 0:
                        return "start_game"
                    elif self.opcion_seleccionada == 1:
                        return "exit"
        return None

    def dibujar(self):
        """Dibuja las opciones del menú en pantalla."""
        self.pantalla.fill((30, 30, 30))  # Fondo oscuro
        for i, opcion in enumerate(self.opciones):
            color = (255, 255, 255) if i != self.opcion_seleccionada else (255, 0, 0)  # Rojo para la opción seleccionada
            texto = self.fuente.render(opcion, True, color)
            self.pantalla.blit(texto, (350, 250 + i * 60))
        pygame.display.flip()
