#!/usr/bin/env python
"""Modified from pygame.examples.chimp"""


# Import Modules
import os
import pygame as pg

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")


# functions to create our resources
def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)
    image = image.convert()

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    sound = pg.mixer.Sound(fullname)

    return sound


# classes for our game objects
class HeMan(pg.sprite.Sprite):
    """Moves a He-Man on the screen, following the mouse"""

    def __init__(self):
        #pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        super().__init__()
        self._no_punch_image, self._rect = load_image("no-punch.png", -1)
        self._punch_image, _ = load_image("punch.png", -1)
        self.image = self._no_punch_image
        self.rect = self._rect
        self.offset = (-122, -170)
        self.punching = False
        # self.debug_rect = None

    def update(self):
        """Move He-Man based on the mouse position"""
        pos = pg.mouse.get_pos()
        # if self.punching:
        #    self.rect.move_ip(15, 25)
        self.rect.topleft = pos
        self.rect.move_ip(self.offset)

    def punch(self, target):
        """Returns True if He-Man punches the target"""
        if not self.punching:
            self.punching = True
            self.image = self._punch_image
            # hitbox = self.rect.inflate(-5, -5)
            hitbox = self.rect.move((100,-61)).inflate(-122, -122)
            # self.debug_rect = hitbox
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        """Called to unpunch pose He-Man"""
        self.punching = False
        self.image = self._no_punch_image


class Skeletor(pg.sprite.Sprite):
    """Moves Skeletor across the screen. Skeletor spins when punched."""

    def __init__(self):
        super().__init__()
        self.image, self.rect = load_image("skeletor-he-man-armor.png", -1)
        screen = pg.display.get_surface()
        self.screen = screen
        self.area = screen.get_rect()
        self.rect.topleft = 10, 90
        self.move = 10
        self.dizzy = False
        # self.debug_rect = None

    def update(self):
        """Walk or spin, depending on Skeletor's state"""
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        """move Skeletor across the screen, and turn at the ends"""
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pg.transform.flip(self.image, True, False)
        self.rect = newpos

    def _spin(self):
        """Spin the Skeletor image"""
        center = self.rect.center
        self.dizzy = self.dizzy - 12
        # if self.dizzy >= 45 and self.dizzy < 57:
        #    self.debug_rect = self.image.get_rect(center=center)
        if self.dizzy <= -360:
            self.dizzy = False
            self.image = self.original
        else:
            rotate = pg.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        """This will cause Skeletor to start spinning"""
        if not self.dizzy:
            self.dizzy = True
            self.original = self.image


def main():
    """this function is called when the program starts.
    it initializes everything it needs, then runs in
    a loop until the function returns."""
    # Initialize Everything
    pg.init()
    screen = pg.display.set_mode(size=(1280, 480), flags=pg.SCALED, vsync=1)
    pg.display.set_caption("Skeletor steals He-Man's armor!")
    pg.mouse.set_visible(False)

    # Create The Background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    # Put Text On The Background, Centered
    if pg.font:
        font = pg.font.Font(None, 64)
        text = font.render("Skeletor steals He-Man's armor?!?", True, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        background.blit(text, textpos)

    # Display The Background
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Prepare Game Objects
    whiff_sound = load_sound("whiff.wav")
    punch_sound = load_sound("punch.wav")
    skeletor = Skeletor()
    heman = HeMan()
    allsprites = pg.sprite.RenderPlain((skeletor, heman))
    clock = pg.time.Clock()

    # Main Loop
    going = True
    while going:
        clock.tick(30)

        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if heman.punch(skeletor):
                    punch_sound.play()  # punch
                    skeletor.punched()
                else:
                    whiff_sound.play()  # miss
            elif event.type == pg.MOUSEBUTTONUP:
                heman.unpunch()

        allsprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        #if heman.debug_rect:
        #    pg.draw.rect(screen, 100, heman.debug_rect)
        allsprites.draw(screen)
        pg.display.flip()

    pg.quit()


# Game Over


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
