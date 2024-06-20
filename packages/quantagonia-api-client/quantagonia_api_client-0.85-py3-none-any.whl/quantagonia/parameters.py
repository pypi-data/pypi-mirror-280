import json
from typing import Dict
import warnings

# set up warnings
def plain_warning(message, category, filename, lineno, line=None):
    return '%s: %s\n' % (category.__name__, message)
warnings.formatwarning = plain_warning


class HybridSolverParameters:
    """
    Class with setter options that allows to pass parameters to the solver.
    """

    def __init__(self):

        self._parameters = {}


    def gets(self) -> str:
        """
        Returns solver options as string.

        Returns:
            str: Json string containing solver parameters.
        """
        return json.dumps(self._parameters)


    def getd(self) -> Dict:
        """
        Returns solver options as dictionary.

        Returns:
            dict: Dictionary containing solver parameters.
        """
        return self._parameters


    def set_relative_gap(self, rel_gap: float):
        """
        Set the relative gap.

        The relative gap is defined as :math:`|f^\ast - \bar{f}|\, /\,  |f^\ast|`,
        i.e., it is the improvement potential relative to the best-known objective value.
        The solver terminates once the relative gap falls below the specified value for rel_gap.
        The default value is set to 1e-4 (0.01%).

        Args:
            rel_gap (float): A float representing the relative gap for termination.

        Returns:
            None.

        Raises:
            ValueError: If :code:`rel_gap` is not a float or integer.

        Example::

            rel_gap = 1e-2
            spec.set_relative_gap(rel_gap)
        """
        param_name = "relative_gap"
        check_type(param_name, rel_gap, (float, int), type_name="numeric")
        self._parameters[param_name] = rel_gap


    def set_absolute_gap(self, abs_gap: float):
        """
        Set the absolute gap.

        The absolute gap is the difference between the objective value :math:`f∗` of the best solution found
        and the best bound :math:`fˉ​` on the objective value.
        Hence, the absolute gap tells by how much the objective value could potentially still be improved.
        The solver terminates if the absolute gap falls below the specified value for abs_gap.
        The default value is set to 1e-9.

        Args:
            abs_gap (float): A float representing the absolute gap for termination.

        Returns:
            None.

        Raises:
            ValueError: If :code:`abs_gap` is not a float or integer.

        Example::

            abs_gap = 1e-6
            spec.set_absolute_gap(abs_gap)
        """
        param_name = "absolute_gap"
        check_type(param_name, abs_gap, (float, int), type_name="numeric")
        self._parameters[param_name] = abs_gap


    def set_time_limit(self, time_limit: float):
        """
        Sets time limit.

        The solver runs at most for 'time_limit' seconds and returns the best found solution along with the optimality gap.
        The optimality gap tells you by how much the solution could possibly be improved, if the solver continues to run.

        Returns:
            None

        Example::

            time_limit = 10 # seconds
            spec.set_time_limit(time_limit)
        """
        param_name = "time_limit"
        check_type(param_name, time_limit, (float, int), type_name="numeric")
        check_numeric_value(param_name, time_limit, lb=0)
        self._parameters[param_name] = time_limit


    def set_as_qubo(self, as_qubo: bool):
        """
        Set the as_qubo option (MIP only)

        If true, the (M)IP is not only solved with MIP techniques but also
        solved as QUBO in parallel.

        Args:
            as_qubo (bool): A bool that enables or disables the as_qubo option.

        Returns:
            None.

        Raises:
            ValueError: If :code:`as_qubo` is not a bool.
        """
        param_name = "as_qubo"
        check_type(param_name, as_qubo, bool)
        self._parameters[param_name] = as_qubo


    def set_as_qubo_only(self, as_qubo_only: bool):
        """
        Set the as_qubo_only option (MIP only)

        If true, the (M)IP is not solved with MIP techniques but instead is transformed
        to a QUBO and solved as such.

        Args:
            as_qubo_only (bool): A bool that enables or disables the as_qubo_only option.

        Returns:
            None.

        Raises:
            ValueError: If :code:`as_qubo_only` is not a bool.
        """
        param_name = "as_qubo_only"
        check_type(param_name, as_qubo_only, bool)
        self._parameters[param_name] = as_qubo_only


    def set_presolve(self, presolve: bool):
        """
        Enable or disable presolve.

        Args:
            presolve (bool): A boolean indicating whether to enable or disable presolve.

        Returns:
            None.

        Raises:
            ValueError: If :code:`presolve` is not a boolean.

        Example::

            spec.set_presolve(False)
        """
        param_name = "presolve"
        check_type(param_name, presolve, bool)
        self._parameters[param_name] = presolve


    def set_seed(self, seed: float):
        """
        Set the random number seed

        This acts as a small perturbation to some subroutines of the solver and may lead to different solution paths.

        Args:
            seed (float): The random number seed.

        Returns:
            None.
        """
        param_name = "seed"
        check_type(param_name, seed, (float, int), type_name="numeric")
        self._parameters[param_name] = seed


    def set_heuristics_only(self, heuristics_only: bool):
        """
        Only apply the root node primal heuristics and then terminate (QUBO only)

        This waits until *all* primal heuristics are finished and displays a table with
        objective value and runtime per heuristic.

        Args:
            heuristics_only (bool): Flag to enable or disable heuristics_only mode.
        Returns:
            None
        """
        param_name = "heuristics_only"
        check_type(param_name, heuristics_only, bool)
        self._parameters[param_name] = heuristics_only


    def set_objective_limit(self, objective_value: float):
        """
        Sets a limit on the objective value to terminate optimization.

        The solver terminates as soon as it finds a feasible solution with an objective value at least as
        good as the specified :code:`objective_value`.

        Args:
            objective_value (float): A float representing the termination value for the objective.

        Returns:
            None.

        Raises:
            ValueError: If :code:`objective_value` is not a float or integer.
        """
        param_name =  "objective_limit"
        check_type(param_name, objective_value, (float, int), type_name="numeric")
        self._parameters[param_name] = objective_value


    def set_quantum_heuristics(self, heuristics: list):
        """
        Set quantum heuristics (QUBO only).

        Args:
            heuristics (list): A list of quantum heuristics that are applied in the solution process.

        Returns:
            None.
        """
        param_name = "root_node_quantum_heuristics"
        check_type(param_name, heuristics, list)
        self._parameters[param_name] = heuristics


def check_type(option_name, option_value, type, type_name=None):

    if not isinstance(option_value, type):
        if type_name is None:
            type_name = type.__name__
        raise ValueError(f"Value for {option_name} is set to {option_value} but must be a {type_name}.")


def check_numeric_value(option_name, option_value, lb=None, ub=None):
    if lb is not None and option_value < lb:
        raise ValueError(f"Value for {option_name} must be >= {lb}")
    if ub is not None and option_value > ub:
        raise ValueError(f"Value for {option_name} must be <= {ub}")
