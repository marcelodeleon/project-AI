import random

w = 0.729844  # Factor de Inercia
c1 = 1.496180  # Constante de aceleración
c2 = 1.496180  # Constante de aceleración
swarmSize = 30  # Tamaño de la población
iteraciones = 3000
dimension = 20  # Tamaño del problema
xmin = 0  # posición mínima
xmax = 0  # posición maxima


class Particle:
    """
    TODO: Write docstring
    """

    def __init__(self, problem):
        self.position = None     # Posición de la partícula
        self.fitness = None
        self.velocity = None     # Velocidad de la partícula
        self.pos_best = None    # mejor posición individual
        self.pos_best_fitness = None

        # Inicio Velocidades y Posiciones
        self.velocity.append(random.uniform(-1, 1))
        self.position.append(problem.randomElement())
        self.pos_best.append(self.position)

    def update_position(self):
        self.position = tuple(map(lambda x: x + self.velocity), self.position)

    def update_velocity(self, gBest):
        # for i in range(dimension):
        r1 = random.random()
        r2 = random.random()
        # social = c1 * r1 * (gBest[i] - self.position_i[i])
        social = tuple(map(lambda x, y: c1 * r1 * (x - y)), zip(gBest, self.position)))
        # cognitivo = c2 * r2 * (self.pos_best_i[i] - self.position_i[i])
        cognitivo = tuple(map(lambda x, y: c2 * r2 * (x - y)), zip(self.pos_best, self.position)))
        self.velocity = (w * self.velocity_i[i]) + social + cognitivo

    def satisfy_constraints(self):
        # This is where constraints are satisfied
        return


class PSO:
    solucion = []
    swarm = []

    def __init__(self, problem, steps):
        for h in range(swarmSize):
            particle = Particle(problem)
            self.swarm.append(particle)
            return

    def optimize(self):
        for i in range(iteraciones):
            print "iteracion ", i
            # Obtiene el mejor global
            globalBest = self.swarm[0]
            for j in range(swarmSize):
                posBest = self.swarm[j].posBest
                if self.f(posBest) > self.f(globalBest):
                    globalBest = posBest
                    solution = globalBest
                    # Acutalizo la posición de la particula
                    for k in range(swarmSize):
                        self.swarm[k].ActualizaVel(globalBest)
                        self.swarm[k].ActualizaPos()
                        self.swarm[k].satisfyConstraints()
                        # Actualiza el personal best
                        for l in range(swarmSize):
                            posBest = self.swarm[l].posBest
                            if self.f(self.swarm[l]) > self.f(posBest):
                                self.swarm[l].posBest = self.swarm[l].position_i
                                return solution

    def f(self, solution):
        return random.random()

def sum_squares():
    from .test_problems import SUM_SQUARES
    problem = SUM_SQUARES
    finalStep = list(particle_swarm(problem, steps=10000))[-1]
    print(finalStep)

def eggholder():
    from .test_problems import EGGHOLDER
    problem = EGGHOLDER
    finalStep = list(particle_swarm(problem, steps=10000))[-1]
    print(finalStep)

def graphcolor():
    from .test_problems import GRAPHCOLOR
    problem = GRAPHCOLOR
    finalStep = list(particle_swarm(problem, steps=10000))[-1]
    print(finalStep)
