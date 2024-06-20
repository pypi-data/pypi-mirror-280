import os, math

from quantagonia.cloud.cloud_runner import CloudRunner
from quantagonia.parameters import HybridSolverParameters

input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "ip_as_qubo.lp")

api_key = os.environ["QUANTAGONIA_API_KEY"]

# setup the cloud runner
runner = CloudRunner(api_key)

# set solver parameters
params = HybridSolverParameters()
params.set_time_limit(120)
params.set_as_qubo_only(True)  # this parameterizes the solver to solve the IP as QUBO

res_dict, _ = runner.solve(input_file_path, params)

# print some results
print("Runtime:", res_dict["timing"])
print("Objective:", res_dict["objective"])
print("Bound:", res_dict["bound"])
print("Solution:")
for idx, val in res_dict["solution"].items():
    print(f"\t{idx}: {val}")

# in order to use these as test
if math.fabs(res_dict["objective"] - 4.0) > 1e-4:
    raise Exception("Objective value is not correct")
