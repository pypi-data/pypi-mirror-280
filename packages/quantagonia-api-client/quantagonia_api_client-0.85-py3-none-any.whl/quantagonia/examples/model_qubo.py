import os

from quantagonia.qubo import *
from quantagonia.cloud.cloud_runner import CloudRunner
from quantagonia.parameters import HybridSolverParameters
from quantagonia.enums import HybridSolverOptSenses

API_KEY = os.environ["QUANTAGONIA_API_KEY"]

def test_model_qubo_native():

  # setup model
  model = QuboModel()

  # setup variables
  x0 = model.addVariable("x_0", initial=1)
  x1 = model.addVariable("x_1", initial=1)
  x2 = model.addVariable("x_2", initial=1)
  x3 = model.addVariable("x_3", initial=1)
  x4 = model.addVariable("x_4", initial=1)

  # build objective
  model.objective += 2 * x0
  model.objective += 2 * x2
  model.objective += 2 * x4
  model.objective -= x0 * x2
  model.objective -= x2 * x0
  model.objective -= x0 * x4
  model.objective -= x4 * x0
  model.objective -= x2 * x4
  model.objective -= x4 * x2
  model.objective += 3

  # set the sense
  model.sense = HybridSolverOptSenses.MINIMIZE

  print("Problem: ", model)
  print("Initial: ", model.eval())

  runner = CloudRunner(API_KEY)

  params = HybridSolverParameters()
  params.set_time_limit(10)
  res = model.solve(runner, params)

  print("Runtime:", res["timing"])
  print("Status:", res["sol_status"])
  print("Objective:", model.eval())
  return model.eval()

if __name__ == '__main__':
  if test_model_qubo_native() != 3.0:
    raise Exception("Objective value is not correct")
