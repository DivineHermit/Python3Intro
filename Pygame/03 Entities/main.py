"""
    The main game file containing the main game loop.
"""
import sys
import pygame
import settings

class Game:

    def __init__(self) -> None:
        """ Initialize game variables and load settings/data. """
        # Set the game windows size.
        self.window = pygame.display.set_mode(settings.WINDOW_SIZE)
        # Set the title of the game window.
        pygame.display.set_caption(settings.TITLE)
        # isRunning is used to track when the program is running.
        self.isRunning = True
        # Create a sprite group to to hold all the game sprites.
        self.sg_all_sprites = pygame.sprite.LayeredUpdates()

    def events(self):
        """
            Handle events and user input.
            Player input, quitting and game events are handled here.
        """
        for event in pygame.event.get():
            # ##### PYGAME EVENTS ##### #
            if event.type == pygame.QUIT:
                # Check if the game window is closed.
                self.quit()
            # ##### KEY PRESSES ##### #
            if event.type == pygame.KEYDOWN:
                # Check what key is being pressed down.
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    def quit(self):
        """ Quit and close the program. """
        # Fadeout any playing music.
        pygame.mixer.fadeout(1000)
        # stop the game from playing.
        self.isPlaying = False
        # Close the mixer.
        pygame.mixer.quit()
        # Close pygame.
        pygame.quit()
        # Stop the application.
        self.isRunning = False
        # Tell the Python interpreter application is closing.
        sys.exit()

    def draw(self):
        """ Draw the sprites and graphics to the game window. """
        # Change the color of the game window so we know it's working.
        self.window.fill((200, 0, 0))
        # Tell pygame to update what is being displayed.
        for sprite in self.sg_all_sprites:
            self.window.blit(sprite)
        pygame.display.update()

    def run(self):
        """ The main game loop that calls the other methods. """
        # Set the game to playing.
        self.isPlaying = True
        
        while self.isPlaying:
            # Call the other methods to update the game state.
            self.events()
            self.update()
            self.draw()

    def update(self):
        """ Update game data and sprite positions. """
        pass


if __name__ == "__main__":
    game = Game()
    game.run()
