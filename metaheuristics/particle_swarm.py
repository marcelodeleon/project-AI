import random

# Particle Swarm coefficients.
W = 0.729844  # Inertia.
C1 = 1.496180  # Cognitive acceleration.
C2 = 1.496180  # Social acceleration.

# Population size
SWARM_SIZE = 30


class Particle:
    """
    TODO: Write docstring
    """

    def __init__(self, problem, initial=None):
        """
        Particle constructor.

        Parameters
        ----------
        problem: Object
            Representation of the problem to be optimized.
        """

        # Particle's memory, indicates the best position (with it's associated
        # fitness) found so far.
        self.best = {
            'fitness': None,
            'position': None
        }

        # Initialize position.
        self.position = initial if initial else problem.randomElement()

        # Initialize velocity vector.
        self.velocity = (random.uniform(-1, 1) for _ in
                         range(0, len(self.position)))

        # Evaluate initial position's fitness.
        self.fitness = problem.objective(self.position)

        # Initialize best.
        self.best['fitness'] = self.fitness
        self.best['position'] = self.position

    def _get_social_term(self, gBest):
        """
        Get the social term group from the particle velocity equation.

        Parameters
        ----------
        gBest: tuple
            Best position from the swarm so far.
        """

        R2 = random.random()

        return tuple(map(
            lambda x, y: C2 * R2 * (x - y),
            zip(gBest, self.position)
        ))

    def _get_cognitive_term(self):
        """
        Get the cognitive term group from the particle velocity equation.
        """

        R1 = random.random()

        return tuple(map(
            lambda x, y: C1 * R1 * (x - y),
            zip(self.pos_best, self.position)
        ))

    def update_position(self):
        """
        Calculate the new position using the latest velocity.
        """

        self.position = tuple(map(lambda x: x + self.velocity), self.position)

    def update_velocity(self, gBest):
        """
        Calculate the new velocity of the particle.

        Parameters
        ----------
        gBest: tuple
            Best position from the swarm so far.
        """

        social_term = self._get_social_term(gBest)
        cognitive_term = self._get_cognitive_term()

        self.velocity = tuple(map(
            lambda x, y, z: W * x + y + z,
            zip(self.velocity, social_term, cognitive_term)
        ))

    def __repr__(self):
        return 'Position: {}\nFitness: {}'.format(self.position, self.fitness)

    def satisfy_constraints(self):
        # This is where constraints are satisfied
        return


class PSO:
    solucion = []

    def __init__(self, problem, steps):
        self.swarm = []

        # Definition of the optimization problem.
        self.problem = problem

        # Number of steps for the algorithm.
        self.steps = steps

        for _ in range(SWARM_SIZE):
            particle = Particle(problem)
            self.swarm.append(particle)

        for p in self.swarm:
            print(p)

    # def optimize(self):
    #     for i in range(iteraciones):
    #         print "iteracion ", i
    #         # Obtiene el mejor global
    #         globalBest = self.swarm[0]
    #         for j in range(swarmSize):
    #             posBest = self.swarm[j].posBest
    #             if self.f(posBest) > self.f(globalBest):
    #                 globalBest = posBest
    #                 solution = globalBest
    #                 # Acutalizo la posición de la particula
    #                 for k in range(swarmSize):
    #                     self.swarm[k].ActualizaVel(globalBest)
    #                     self.swarm[k].ActualizaPos()
    #                     self.swarm[k].satisfyConstraints()
    #                     # Actualiza el personal best
    #                     for l in range(swarmSize):
    #                         posBest = self.swarm[l].posBest
    #                         if self.f(self.swarm[l]) > self.f(posBest):
    #                             self.swarm[l].posBest = self.swarm[l].position_i
    #                             return solution

    # def f(self, solution):
    #     return random.random()


def sum_squares():
    from .test_problems import SUM_SQUARES
    problem = SUM_SQUARES
    PSO(problem, steps=10000)

sum_squares()
# def eggholder():
#     from .test_problems import EGGHOLDER
#     problem = EGGHOLDER
#     finalStep = list(particle_swarm(problem, steps=10000))[-1]
#     print(finalStep)

# def graphcolor():
#     from .test_problems import GRAPHCOLOR
#     problem = GRAPHCOLOR
#     finalStep = list(particle_swarm(problem, steps=10000))[-1]
#     print(finalStep)
