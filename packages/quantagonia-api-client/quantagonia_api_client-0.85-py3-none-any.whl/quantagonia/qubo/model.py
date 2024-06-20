import os
from operator import itemgetter

from typing import List, Dict
import tempfile
import gzip

# import necessary parts for conversion methods
from pyqubo import Model as pqModel
from dimod import BinaryQuadraticModel
from qiskit_optimization.problems.quadratic_program import QuadraticProgram as QiskitQP
from qiskit_optimization.problems.quadratic_objective import ObjSense

try:
    from functools import singledispatchmethod
except:
    from singledispatchmethod import singledispatchmethod

from quantagonia.enums import HybridSolverOptSenses
from quantagonia.parser.log_parser import SolverLogParser
from quantagonia.runner import Runner
from quantagonia.parameters import HybridSolverParameters
from quantagonia.qubo.variable import *
from quantagonia.qubo.term import *
from quantagonia.qubo.expression import *

class QuboModel(object):
    """
    A class representing a Quadratic Unconstrained Binary Optimization (QUBO) problem instance.
    """

    def __init__(self, sense : HybridSolverOptSenses = HybridSolverOptSenses.MAXIMIZE):
        """
        Initializes a new instance of the :class:`QuboModel` class.

        Args:
            sense (HybridSolverOptSenses): An enum representing the optimization sense of the QUBO. Defaults to `HybridSolverOptSenses.MAXIMIZE`.
        """
        self.vars = {}
        self.objective = QuboExpression()
        self.sense = sense

        # for future use
        self.sos1 = []
        self.sos2 = []

        self._pos_ctr = 0

        self._eps = 1e-12

    @property
    def sense(self):
        """
        The optimization sense of the QUBO.

        The function :code:`sense()` returns the current QUBO's optimization sense if there is no argument. When passed a `HybridSolverOptSenses` member it sets the optimization sense to the specified value.

        Args:
            sense (HybridSolverOptSenses): (optional) An enum representing the optimization sense of the QUBO. Can be either `HybridSolverOptSenses.MINIMIZE` or `HybridSolverOptSenses.MAXIMIZE`.

        Raises:
            RuntimeError: If the `sense` argument is not a valid optimization sense value.
        """
        return self.__sense

    @sense.setter
    def sense(self, sense: HybridSolverOptSenses):
        """
        Sets the optimization sense of the QUBO.

        The function :code:`sense()` returns the current QUBO's optimization sense if there is no argument. When passed a `HybridSolverOptSenses` member it sets the optimization sense to the specified value.

        Args:
            sense (HybridSolverOptSenses): (optional) An enum representing the optimization sense of the QUBO. Can be either `HybridSolverOptSenses.MINIMIZE` or `HybridSolverOptSenses.MAXIMIZE`.

        Raises:
            RuntimeError: If the `sense` argument is not a valid optimization sense value.
        """
        if isinstance(sense, HybridSolverOptSenses):
            self.__sense = sense
        else:
            raise RuntimeError(f"Try to set invalid optimization sense: {sense}")

    def addSOS1(self, vars : list):
        warnings.warn("SOS1 constraints are currently not supported in QUBOs")
        self.sos1.append(vars)

    def addSOS2(self, vars : list):
        warnings.warn("SOS2 constraints are currently not supported in QUBOs")
        self.sos2.append(vars)

    def addVariable(self, name : str, initial=None, fixing=None, disable_warnings=False):
        """
        Adds a new variable to the QUBO.

        Note:
            QUBO Variables are binary and can take a value in {0, 1, None}.

        Args:
            name (str): The name of the variable.
            initial (Any): The initial value of the variable. Defaults to `None`.
            fixing (Any): The value to which the variable should be fixed. Defaults to `None`.
            disable_warnings (bool): If `True`, disables the warning message that is displayed when a variable with the same name is already in the QUBO. Defaults to `False`.

        Returns:
            QuboVariable: The :class:`QuboVariable` that was added to the QUBO.

        Raises:
            Warning: If initial not in {0, 1, None}.
        """
        # make sure to have variable names as strings
        # this crashes, if variable name cannot be casted as a string, which is the desired behavior
        name = str(name)

        if(name in self.vars):
            if(not disable_warnings):
                warnings.warn("Variable " + name + " already in QUBO...")

            return self.vars[name]

        self.vars[name] = QuboVariable(name, self._pos_ctr, initial, fixing)
        self._pos_ctr += 1

        return self.vars[name]

    def variable(self, name : str):
        """
        Returns the :class:`QuboVariable` with the specified name.

        Args:
            name (str): A string of the name of the :class:`QuboVariable` to retrieve.

        Returns:
            QuboVariable: The :class:`QuboVariable` with the specified name.

        Raises:
            KeyError: If no :class:`QuboVariable` with the specified name exists in the QUBO.
        """
        return self.vars[name]

    def eval(self):
        """
        Returns the objective function value for the current variable assignment. After solving, it provides the optimal value.

        Returns:
            float: The value of the QUBO's objective function.
        """
        return self.objective.eval()

    def isValid(self):
        """
        Checks that all terms are in the upper triangle and that they have been reduced in the right way.

        Returns:
            bool: Indicating whether conditions are all true.
        """
        return self.objective.isValid()

    def writeQUBO(self, path : str):
        """
        Writes QUBO to file in the Quantagonia QUBO format.

        Args:
            path (str): Path as string to the destined file.

        Raises:
            Exception: If the QUBO is not valid.
            FileNotFoundError: If the path or file cannot be found.
            PermissionError: If program does not have sufficient permissions to access the file.
            TypeError: If path is not a string.
        """
        shift = 0.0
        num_shift = 0
        if "" in self.objective.terms:
            num_shift = 1
            shift = self.objective.terms[""].coefficient

        # check that all terms are in the upper triangular part
        if not self.isValid():
            raise Exception("QUBO invalid - check that all terms are in the upper triangular part of Q.")

        # prepare sorted (by row) COO triplets
        triplets = []
        for key in self.objective.terms:
            if key == "":
                continue

            term = self.objective.terms[key]

            # remove terms with coefficient == 0.0
            if abs(term.coefficient) < self._eps:
                continue

            if(term.order() == 1):
                triplets.append((term.vars[0].id(), term.vars[0].id(), term.coefficient))

            # By convention, we only store the upper triangular part of the matrix, but it
            # is mirrored into the lower triangular part inside the QUBO solver - hence in
            # order to maintain the optimum, we have to divide the coefficients of
            # off-diagonal entries by 2
            if(term.order() == 2):
                triplets.append((term.vars[0].id(), term.vars[1].id(), 0.5 * term.coefficient))

        triplets.sort(key=itemgetter(0,1))

        with open(path, 'w') as f:

            sense_str = self.__sense.value
            f.write(sense_str + "\n")
            f.write("1\n")
            f.write("1.0\n")

            f.write(f"{shift}\n")

            # create sparse matrix from terms in objective
            f.write(f"{len(self.vars)} {len(triplets)}\n")
            for t in triplets:
                f.write(f"{t[0]} {t[1]} {t[2]}\n")

            # add fixings
            for var in self.vars.values():
                if var.fixing is not None:
                    f.write(f"f {var.id()} {var.fixing}\n")

    def getNnzUpperTriangle(self):
        """
        Get the number of nonzero entries for the upper triangle matrix. This corresponds to the number of terms in the objective function, excluding the shift.

        Returns:
            int: Integer representing the number of nonzero entries for the upper triangle matrix.
        """

        # do we have a shift?
        if "" in self.objective.terms:
            return len(self.objective.terms) - 1
        else:
            return len(self.objective.terms)

    def getNnzFullMatrix(self):
        """
        Compute number of nonzero entries of the full matrix on demand.

        Returns:
            int: Integer representing the number of nonzero entries of the full matrix.
        """
        # first, get nnz of the upper triangle matrix, this is only the number of terms in the objective
        upper_triangle_nnz = self.getNnzUpperTriangle()
        # count linear terms to compute nnz of full matrix
        linear_terms = 0
        for term in self.objective.terms.values():
            if term.order() == 1:
                linear_terms += 1
        full_matrix_nnz = 2*upper_triangle_nnz - linear_terms

        return full_matrix_nnz

    @classmethod
    def readQUBO(cls, path : str):
        """
        Reads a QUBO from file.

        Args:
             path (str): String containing the path to the QUBO file.

        Returns:
            QuboModel: The QUBO.
        """
        if path.endswith(".gz"):
            with gzip.open(path, 'rt') as f:
                qubo = cls._readQuboFile(f)
        else:
            with open(path, 'r') as f:
                qubo = cls._readQuboFile(f)

        return qubo


    @classmethod
    def _readQuboFile(cls, f):
        """
        Reads a QUBO from a file object and returns it as a :class:`QuboModel`.

        Args:
            f (TextIO): A file object containing the QUBO in the .qubo format.

        Returns:
            A :class:`QuboModel` instance representing the QUBO problem read from the file.

        Raises:
            Exception: If the QUBO file contains aggregated or weighted QUBOs, or if the file is not
            formatted correctly.
        """


        # check if sense is specified in first line
        first_line = f.readline().strip()
        if first_line in [sense.value for sense in HybridSolverOptSenses]:
            sense = HybridSolverOptSenses(first_line)
            num_terms = int(f.readline().strip())
        else:
            sense = HybridSolverOptSenses.MAXIMIZE # default
            num_terms = int(first_line)
        if num_terms != 1:
            raise Exception("Aggregated QUBOs are not supported...")
        weight = float(f.readline().strip())
        if weight != 1.0:
            raise Exception("Weighted QUBOs are not supported...")
        shift = float(f.readline().strip())

        nnz_string = f.readline().strip().split(" ")
        num_vars = int(nnz_string[0])
        num_nnz = int(nnz_string[1])

        # create variables
        qubo = QuboModel(sense)

        if shift != 0:
            qubo.objective += shift

        vars = []
        for ix in range(0, num_vars):
            vars.append(qubo.addVariable(f"x_{ix}"))

        # create terms
        term_ctr = 0
        check_symmetry = False
        lower_terms = []
        for line in f:
            split = line.split(" ")
            ix_i = int(split[0])
            ix_j = int(split[1])
            entry = float(split[2])

            if ix_i == ix_j:
                qubo.objective += entry * vars[ix_i]
            elif ix_i > ix_j:
                raise Exception("Invalid .qubo file, only upper triangular matrix can be stored")
            else:
                # since we only store the upper triangular matrix, we need to
                # make the entries in the lower triangular matrix explicit
                # through doubling the coefficient
                qubo.objective += 2.0 * entry * vars[ix_i] * vars[ix_j]

            term_ctr += 1


        if term_ctr != num_nnz:
            raise Exception("Invalid .qubo files, float of NNZ specified does not match NZ entries!")

        return qubo

    @classmethod
    def fromQiskitQubo(cls, qp : QiskitQP):
        """
        Converts a QUBO in Qiskits QuadraticProgram format to a :class:`QuboModel`.

        Args:
            qp (:class: `qiskit_optimization.problems.quadratic_program.QuadraticProgram`) : The :class: `qiskit_optimization.problems.quadratic_program.QuadraticProgram` to be converted.

        Returns:
            QuboModel: The resulting :class:`QuboModel`.
        """

        # make sure we have a QUBO: all variables need to be binary, no constraints allowed
        if not qp.get_num_vars() == qp.get_num_binary_vars():
            raise Exception("Model contains non-binary variables.")

        if qp.get_num_linear_constraints() != 0 or qp.get_num_quadratic_constraints() != 0:
            raise Exception("Model contains constraints.")

        # init qubo with correct sense
        sense = HybridSolverOptSenses.MINIMIZE if qp.objective.sense == ObjSense.MINIMIZE else HybridSolverOptSenses.MAXIMIZE
        qubo = QuboModel(sense)

        # add variables
        for var in qp.variables:
            qubo.addVariable(var.name)

        # linear terms
        for var_name, var_coeff in qp.objective.linear.to_dict(use_name=True).items():
            qubo.objective += var_coeff * qubo.vars[var_name]

        # quadratic terms
        for var_tpl, var_coeff in qp.objective.quadratic.to_dict(use_name=True).items():
            qubo.objective += var_coeff * qubo.vars[var_tpl[0]] * qubo.vars[var_tpl[1]]

        return qubo


    @classmethod
    def fromDwaveBQM(cls, bqm : BinaryQuadraticModel):
        """
        Converts a D-Wave BQM to a :class:`QuboModel`.

         Args:
            bqm (:class:`dimod.BinaryQuadraticModel`) : The :class:`dimod.BinaryQuadraticModel` to be converted.

         Returns:
            QuboModel: The resulting :class:`QuboModel`.
        """

        # D-Wave only allows minimization, so we also set the sense to minimization
        qubo = QuboModel(HybridSolverOptSenses.MINIMIZE)

        # add variables
        for var_name in bqm.variables:
            qubo.addVariable(var_name)

        # add shift
        qubo.objective += bqm.offset

        # create linear terms
        for var, coeff in bqm.linear.items():
            qubo.objective += coeff * qubo.vars[var]

        # create quadratic terms
        for var_tpl, coeff in bqm.quadratic.items():
            qubo.objective += coeff * qubo.vars[var_tpl[0]] * qubo.vars[var_tpl[1]]

        return qubo


    @classmethod
    def fromPyqubo(cls, pqm : pqModel, constants = {}):
        """
        Reads a PyQUBO quadratic model into a :class:`QuboModel` that can be solved by Quantagonia solvers.

        Args:
          pqm (:class:`pyqubo.Model`) : A :class:`pyqubo.Model` to be converted.
          constants (dict) : A dictionary of constant values that can be used in the conversion.

        Returns:
          QuboModel: The resulting :class:`QuboModel`.
        """

        # PyQUBO always assumes minimization
        qubo = QuboModel(HybridSolverOptSenses.MINIMIZE)

        # guarantees that we only have terms of oders {1, 2}
        qmodel, shift = pqm.to_qubo(feed_dict=constants)

        # build objective
        for term in qmodel:
            if (term[0] == term[1]):
                # unary term
                v = qubo.addVariable(term[0], disable_warnings=True)
                qubo.objective += QuboTerm(qmodel[term], [v])
            else:
                # pairwise term
                v0 = qubo.addVariable(term[0], disable_warnings=True)
                v1 = qubo.addVariable(term[1], disable_warnings=True)
                qubo.objective += QuboTerm(qmodel[term], [v0, v1])

        if shift != 0:
            qubo.objective += shift

        return qubo

    def _solvePrep(self):

        # temporary folder for the QUBO problem
        tmp_path = tempfile.mkdtemp()
        tmp_problem = os.path.join(tmp_path, "pyclient.qubo")

        # convert problem into QUBO format (i.e. a matrix)
        self.writeQUBO(tmp_problem)

        return tmp_problem

    def _assignSolution(self, solution):
        """Assign solution to variables."""

        var_names = list(self.vars)
        for var_idx, (sol_var_name, val) in enumerate(solution.items()):
            # Dicts are ordered and the QUBO solver preserves the original
            # variable ordering. Thus, we can reassign index to name.
            # NOTE: The variable names get lost when writing the QUBO file.
            #       As a result, the QUBO solver does not see the original variable names, but
            #       only knows indices. The solution file uses indices as variable names.
            # We double check, if the variable names from the solution file match the
            # variable index:
            if int(sol_var_name) != var_idx:
                warnings.warn("Possible mismatch in assigning solution value to variable.")
            self.vars[var_names[var_idx]].assignment = int(val)

    async def solveAsync(self, runner : Runner, params : HybridSolverParameters = HybridSolverParameters()):
        """
        Solves the QUBO asynchronously using the specified Runner.

        Args:
            runner (CloudRunner): Runner instance used to solve the QUBO.
            params (HybridSolverParameters): Solver parameters.

        Returns:
            Dict[str, Any]: List of solver results. It contains a dictionary containing the keys 'status', 'solver_log', 'sol_status', 'timing', 'objective', 'bound', 'absolute_gap', 'relative_gap', 'iterations', 'nodes', 'nodes_per_sec', 'best_node', 'best_time', 'num_quantum_solutions', 'solver_mix', and 'solution'.
        """
        tmp_problem = self._solvePrep()
        res, _ = await runner.solveAsync(tmp_problem, params)

        logparser = SolverLogParser(res["solver_log"])
        res.update(logparser.get_solver_summary())

        self._assignSolution(res['solution'])

        return res

    def solve(self, runner : Runner, params : HybridSolverParameters = HybridSolverParameters()):
        """
        Solves the QUBO using the specified Runner.

        Args:
            runner (CloudRunner): Runner instance used to solve the QUBO.
            params (HybridSolverParameters): Solver parameters.

        Returns:
            Dict[str, Any]: List of solver results. It contains a dictionary containing the keys 'status', 'solver_log', 'sol_status', 'timing', 'objective', 'bound', 'absolute_gap', 'relative_gap', 'iterations', 'nodes', 'nodes_per_sec', 'best_node', 'best_time', 'num_quantum_solutions', 'solver_mix', and 'solution'.
        """
        tmp_problem = self._solvePrep()
        res, _ = runner.solve(tmp_problem, params)

        logparser = SolverLogParser(res["solver_log"])
        res.update(logparser.get_solver_summary())

        self._assignSolution(res['solution'])

        return res

    def __str__(self):
        return str(self.objective)
