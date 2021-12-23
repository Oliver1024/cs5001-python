from laserbeam import LaserBeam
from asteroid import Asteroid
from spaceship import Spaceship


class GameController:
    """
    Maintains the state of the game
    and manages interactions of game elements.
    """

    def __init__(self, SPACE, fadeout):
        """Initialize the game controller"""
        self.SPACE = SPACE
        self.fadeout = fadeout

        self.spaceship_hit = False
        self.asteroid_destroyed = False
        self.asteroids = [Asteroid(self.SPACE)]
        self.laser_beams = []
        self.spaceship = Spaceship(self.SPACE)

    def update(self):
        """Updates game state on every frame"""
        self.do_intersections()

        for asteroid in self.asteroids:
            asteroid.display()

        # ======================================================
        # Problem 3, Part 2: Laser beam handler
        # Your code will replace (or augment) the next several
        # lines. Laser beam objects should remain in the scene
        # as many frames as their lifespan allows.
        # Begin problem 3 code changes
        spent_laserbeams = []

        for line in range(len(self.laser_beams)):
            if self.laser_beams[line].lifespan > 0:
                self.laser_beams[line].display()
            else:
                spent_laserbeams.append(line)
        for spent in spent_laserbeams:
            del self.laser_beams[spent]

        # End problem 3, part 2 code changes
        # =======================================================

        self.spaceship.display()
        SPACE_NUM = 165  # Replace magic number
        ASTEROID_NUM = 250  # Replace magic number

        # Carries out necessary actions if game over
        if self.spaceship_hit:
            if self.fadeout <= 0:
                fill(1)
                textSize(30)
                text("YOU HIT AN ASTEROID",
                     self.SPACE['w']/2 - SPACE_NUM, self.SPACE['h']/2)
            else:
                self.fadeout -= 1

        if self.asteroid_destroyed:
            fill(1)
            textSize(30)
            text("YOU DESTROYED THE ASTEROIDS!!!",
                 self.SPACE['w']/2 - ASTEROID_NUM, self.SPACE['h']/2)

    def fire_laser(self, x, y, rot):
        """Add a laser beam to the game"""
        x_vel = sin(radians(rot))
        y_vel = -cos(radians(rot))
        self.laser_beams.append(
            LaserBeam(self.SPACE, x, y, x_vel, y_vel)
        )

    def handle_keypress(self, key, keycode=None):
        """Handle keypress function"""
        if (key == ' '):
            if self.spaceship.intact:
                self.spaceship.control(' ', self)
        if (keycode):
            if self.spaceship.intact:
                self.spaceship.control(keycode)

    def handle_keyup(self):
        """Handle keyup function"""
        if self.spaceship.intact:
            self.spaceship.control('keyup')

    def do_intersections(self):
        # ======================================================
        # Problem 4, Part 1: Intersections
        # Here's where you'll probably want to check for intersections
        # between asteroids and laser beams. Laser beams should be removed
        # from the scene if they hit an asteroid, and the asteroid should
        # blow up (the blow_up_asteroid method also must be written. It's
        # been started for you below).
        #
        # The intersection logic below between the spaceship
        # and asteroids should give a hint as to how this will work.
        # Begin code changes for Problem 3, Part 1: Intersections
        """Get the position of the laser beam and asteroids whether it hits"""
        asteroid_hit = []
        spent_laser_beam = []

        for i in range(len(self.asteroids)):
            for j in range(len(self.laser_beams)):
                if abs(self.laser_beams[j].x - self.asteroids[i].x) \
                    < self.asteroids[i].radius and \
                    abs(self.laser_beams[j].y - self.asteroids[i].y) \
                        < self.asteroids[i].radius:
                    asteroid_hit.append((i, j))
                    spent_laser_beam.append(j)

        for hit in asteroid_hit:
            # self.blow_up_asteroid(i, j)
            self.blow_up_asteroid(hit[0], hit[1])

        for spent in sorted(spent_laser_beam):
            del self.laser_beams[spent]

        # End of code changes for Problem 4, Part 1: Intersections
        # ======================================================

        # If the space ship still hasn't been blown up
        if self.spaceship.intact:
            # Check each asteroid for intersection
            for i in range(len(self.asteroids)):
                if (
                    abs(self.spaceship.x - self.asteroids[i].x)
                    < max(self.asteroids[i].radius, self.spaceship.radius)
                    and
                    abs(self.spaceship.y - self.asteroids[i].y)
                        < max(self.asteroids[i].radius,
                              self.spaceship.radius)):
                    # We've intersected an asteroid
                    self.spaceship.blow_up(self.fadeout)
                    self.spaceship_hit = True

    def blow_up_asteroid(self, i, j):
        # ======================================================
        # Problem 4, Part 2: Asteroid blow-up

        # Here you'll write the code to blow up an asteroid.
        # The parameters represent the indexes for the list of
        # asteroids and the list of laser beams, indicating
        # which asteroid is hit by which laser beam.

        # You'll need to:
        # A) Remove the hit asteroid from the scene
        # B) Add appropriate smaller asteroids to the scene
        # C) Make sure that the smaller asteroids are positioned
        #    correctly and flying off in the correct directions

        # Specifically. If the large asteroid is hit, it should
        # break into two medium asteroids, which should fly off
        # perpendicularly to the direction of the laser beam.

        # If a medium asteroid is hit, it should break into three
        # small asteroids, two of which should fly off perpendicularly
        # to the direction of the laser beam, and the third
        # should fly off in the same direction that the laser
        # beam had been traveling.

        # If a small asteroid is hit, it disappears.

        # Begin code changes for Problem 4, Part 2: Asteroid blow-up
        """blow up asteroids and set the new asteroids new velocity"""
        VEL_NUM = 5
        HALF_NUM = 2
        PIECE_TWO = 2
        PIECE_THREE = 3

        if self.asteroids[i].asize == "Large":
            new_asteroids_size = "Med"
            piece = PIECE_TWO
        elif self.asteroids[i].asize == "Med":
            new_asteroids_size = 'Small'
            piece = PIECE_THREE
        else:
            piece = 0

        pos_x = self.asteroids[i].x
        pos_y = self.asteroids[i].y
        del self.asteroids[i]

        # Set changed velocity
        vel_chg = [(self.laser_beams[j].y_vel, -self.laser_beams[j].x_vel),
                   (-self.laser_beams[j].y_vel,  self.laser_beams[j].x_vel),
                   (self.laser_beams[j].x_vel, self.laser_beams[j].y_vel)]

        for p in range(piece):
            new_asteroid = Asteroid(self.SPACE, asize=new_asteroids_size,
                                    x=pos_x + vel_chg[p][0]*VEL_NUM,
                                    y=pos_y + vel_chg[p][1]*VEL_NUM,
                                    x_vel=vel_chg[p][0] / HALF_NUM,
                                    y_vel=vel_chg[p][1] / HALF_NUM)
            self.asteroids.append(new_asteroid)

        if len(self.asteroids) == 0:
            self.asteroid_destroyed = True
