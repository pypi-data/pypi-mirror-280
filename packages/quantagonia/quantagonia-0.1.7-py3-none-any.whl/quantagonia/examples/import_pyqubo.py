import os

import pyqubo as pq

from quantagonia import HybridSolver, HybridSolverParameters
from quantagonia.qubo import QuboModel

API_KEY = os.environ["QUANTAGONIA_API_KEY"]

x0, x1, x2, x3, x4 = pq.Binary("x0"), pq.Binary("x1"), pq.Binary("x2"), pq.Binary("x3"), pq.Binary("x4")
pyqubo_qubo = (2 * x0 + 2 * x2 + 2 * x4 - x0 * x2 - x2 * x0 - x0 * x4 - x4 * x0 - x2 * x4 - x4 * x2 + 3).compile()

# setup model
qubo = QuboModel.from_pyqubo(pyqubo_qubo)

# solve with Quantagonia
params = HybridSolverParameters()
params.set_time_limit(10)
hybrid_solver = HybridSolver(API_KEY)
qubo.solve(hybrid_solver, params)

# to be used in tests
if qubo.eval() != 3.0:
    raise Exception("Objective value is not correct")
