import os

from quantagonia import HybridSolver, HybridSolverParameters

mip_path0 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "example.mps")
mip_path1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "garbage.mps")
qubo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "example.qubo")
api_key = os.environ["QUANTAGONIA_API_KEY"]

hybrid_solver = HybridSolver(api_key)

params1 = HybridSolverParameters()
params1.set_time_limit(10)
params2 = HybridSolverParameters()
params2.set_time_limit(10)
params3 = HybridSolverParameters()
params3.set_time_limit(10)

problems = [mip_path0, mip_path1, qubo_path]
params = [params1, params2, params3]
results, _ = hybrid_solver.solve(problems, params, suppress_output=True)  # blocks until all problems are solved

for ix, res in enumerate(results):
    print(f"=== PROBLEM {ix}: status {res['status']} ===")
    print(res["solver_log"])
