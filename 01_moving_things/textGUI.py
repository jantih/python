import pygame

class TextGUI:
    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.OFFSET = 4
        self.font = pygame.font.SysFont('consolas', 16, False, False)
        self.clock = clock

    def drawText(self, t: str, row: int) -> None:
        tr = t.get_rect()
        tr.move_ip(4, self.OFFSET+row*16)
        self.screen.blit(t, tr)

    def printProjectInfo(self, row: int) -> None:
        text = self.setText("Python PyGame projekti - TBD")
        self.drawText(text, row)

    def updateFPS(self, row: int) -> None:
        text = self.setText("FPS: " + "{:.2f}".format(self.clock.get_fps()))
        self.drawText(text, row)
        
    def updateGUI(self)-> None:
        self.printProjectInfo(0)
        self.updateFPS(1)

    def setText(self, text: str) -> str:
        return self.font.render(text, True, (255,255,255), None)