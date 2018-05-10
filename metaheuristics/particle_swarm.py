import random

# Particle swarm coefficients.
W = 0.729844  # Inertia.
C1 = 1.496180  # Cognitive acceleration.
C2 = 1.496180  # Social acceleration.

# Configuration constants.
STEPS = 1000
SWARM_SIZE = 40


class Particle:
    """
    Representation of a Particle.

    Parameters
    ----------

    problem: Object
        Representation of the optimizatin problem.
    initial: tuple
        Initial particle position for the swarm.

    Note: Initiating all particles in the same position did not return good
    results.
    """

    def __init__(self, problem, initial=None):
        """
        Particle constructor.

        Parameters
        ----------
        problem: Object
            Representation of the problem to be optimized.
        """

        # Particle's memory, indicates the best['position'] (with it's
        # associated fitness) found so far.
        self.best = {
            'fitness': None,
            'position': None
        }

        # Initialize position.
        self.position = initial if initial else problem.randomElement()

        # Initialize velocity vector with lower and upper bounds for each
        # domain.
        self.velocity = (random.uniform(lb, ub) for lb, ub in problem.domains)

        # Evaluate initial position's fitness.
        self.fitness = problem.evaluate(self.position)

        # Initialize best.
        self.best['fitness'] = self.fitness
        self.best['position'] = self.position

    def _get_social_term(self, gBest):
        """
        Get the social term group from the particle velocity equation.

        Parameters
        ----------
        gBest: tuple
            best['position'] from the swarm so far.
        """

        R2 = random.random()

        return tuple(C2 * R2 * (x - y) for x, y in
                     zip(gBest['position'], self.position))

    def _get_cognitive_term(self):
        """
        Get the cognitive term group from the particle velocity equation.
        """

        R1 = random.random()

        return tuple(C1 * R1 * (x - y) for x, y in
                     zip(self.best['position'], self.position))

    def _get_inertia_term(self):
        """
        Get the inertia term from the particle velocity equation.
        """

        return tuple(W * x for x in self.velocity)

    def update_position(self):
        """
        Calculate the new position using the latest velocity vector.
        """

        self.position = tuple(x + y for x, y in
                              zip(self.position, self.velocity))

    def update_velocity(self, gBest):
        """
        Calculate the new velocity of the particle.

        Parameters
        ----------
        gBest: tuple
            Best position from the swarm so far.
        """

        inertia_term = self._get_inertia_term()
        social_term = self._get_social_term(gBest)
        cognitive_term = self._get_cognitive_term()

        self.velocity = tuple(x + y + z for x, y, z in
                              zip(inertia_term, social_term, cognitive_term))

    def __repr__(self):
        return 'Position: {}\nFitness: {}'.format(self.position, self.fitness)

    def satisfy_constraints(self):
        # This is where constraints are satisfied. Using the 'Let it fly'
        # strategy.
        return


class PSO:
    def __init__(self, problem, steps=STEPS, swarm_size=SWARM_SIZE,
                 verbose=False, initial=None):
        self.verbose = verbose
        self.swarm = []

        # Number of particles in the swarm.
        self.swarm_size = swarm_size

        # Definition of the optimization problem.
        self.problem = problem

        # Number of steps for the algorithm.
        self.steps = steps

        # best['position'] for the whole swarm.
        self.gBest = {
            'fitness': -self.problem.target,
            'position': None
        }

        # Initialize list with all particles (Swarm).
        for p in range(self.swarm_size):
            particle = Particle(problem, initial=initial)
            self.swarm.append(particle)

            # Update global best
            if self._current_better_than_global_best(particle):
                self.gBest['position'] = particle.position
                self.gBest['fitness'] = particle.fitness

        if self.verbose:
            for p in self.swarm:
                print(p)

            print('Global Best so far is {}, fitness: {}'.format(
                self.gBest['position'],
                self.gBest['fitness']
            ))

    def _current_better_than_personal_best(self, current_particle):
        """
        Checks if the current particle's position is better than the
        personal best known.
        """

        return self.problem.compareEvaluations(
                   current_particle.best['fitness'],
                   current_particle.fitness
               ) > 0

    def _current_better_than_global_best(self, current_particle):
        """
        Checks if the current particle's position is better than the global
        best known.
        """

        return self.problem.compareEvaluations(
                   self.gBest['fitness'],
                   current_particle.fitness
               ) > 0

    def optimize(self):
        """PSO Main loop."""

        for i in range(self.steps):
            for p in range(self.swarm_size):
                current_particle = self.swarm[p]

                # Update velocity and position for current particle.
                current_particle.update_velocity(self.gBest)
                current_particle.update_position()
                current_particle.satisfy_constraints()

                # Update fitness for new position.
                current_particle.fitnes = self.problem.evaluate(
                    current_particle.position
                )

                # Update best['position'] for current particle.
                if self._current_better_than_personal_best(current_particle):
                    current_particle.best['fitness'] = current_particle.fitness
                    current_particle.best['position'] = \
                        current_particle.position

                    # Update global best.
                    if self._current_better_than_global_best(current_particle):
                        self.gBest['position'] = current_particle.position
                        self.gBest['fitness'] = current_particle.fitness

            if self.verbose:
                print('Global best is {}, fitness is {}'.format(
                    self.gBest['position'],
                    self.gBest['fitness']
                ))

        return self.gBest['position'], self.gBest['fitness'], \
            self.problem.evaluation_count


def sum_squares(initial=None):
    from .test_problems import SUM_SQUARES
    problem = SUM_SQUARES
    pso = PSO(problem, initial=initial)
    return pso.optimize()


def eggholder(initial=None):
    from .test_problems import EGGHOLDER
    problem = EGGHOLDER
    pso = PSO(problem, initial=initial)
    return pso.optimize()


def graph_coloring(initial=None):
    from .test_problems import GRAPHCOLORING
    problem = GRAPHCOLORING
    pso = PSO(problem, initial=initial)
    return pso.optimize()
