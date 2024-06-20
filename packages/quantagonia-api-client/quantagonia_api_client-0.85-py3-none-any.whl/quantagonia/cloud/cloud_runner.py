import sys
import asyncio
from time import sleep
from yaspin import yaspin
import uuid
import pathlib
from quantagonia.cloud.solver_log import SolverLog
from quantagonia.cloud.specs_https_client import SpecsHTTPSClient, JobStatus
from quantagonia.cloud.specs_enums import *
from quantagonia.runner import Runner
from quantagonia.parameters import HybridSolverParameters
from quantagonia.enums import HybridSolverServers, HybridSolverProblemType
from quantagonia.parser.log_parser import SolverLogParser
from quantagonia.parser.solution_parser import SolutionParser


class CloudRunner(Runner):
    """
    Runner subclass that provides functionality for submitting and solving QUBO and MIP instances to the cloud.

    Args:
        api_key (str): The API key string used to authenticate with the cloud.
        server (HybridSolverServers): (optional) The 'HybridSolverServers' to use for the hybrid solver service, defaults to the
            production server. Defaults to 'HybridSolverServers.PROD'.
        suppress_output (bool): (optional) Boolean indicating whether to suppress logging output from the runner, defaults to False.

    Attributes:
        https_client: The 'SpecsHTTPSClient' used for making requests to the hybrid solver service.
    """
    def __init__(self, api_key: str, server: HybridSolverServers = HybridSolverServers.PROD, suppress_output : bool = False):
        self.https_client = SpecsHTTPSClient(api_key=api_key, target_server=server)
        self.suppress_output = suppress_output
        self._error_symbol = "❌"

    def httpsClient(self):
        return self.https_client

    def _parseKwargs(self, **kwargs):

        poll_frequency = kwargs.get("poll_frequency", 1)
        timeout = kwargs.get("timeout", 14400)
        new_incumbent_callback = kwargs.get("new_incumbent_callback", None)
        submit_callback = kwargs.get("submit_callback", None)
        job_options = kwargs.get("job_options", {})

        return poll_frequency, timeout, new_incumbent_callback, submit_callback, job_options

    def waitForJob(self, jobid: uuid, poll_frequency: float, timeout: float, solver_logs: list, batch_size : int, new_incumbent_callback = None) -> JobStatus:
        """
        Polls the status of a job identified by `jobid` until it reaches a final status or until the timeout is exceeded. The function updates the solver logs and calls the new incumbent callback function if a new incumbent is found in the batch item.

        Args:
            jobid: A UUID object that identifies the job to poll the status for.
            poll_frequency: The frequency (as float, in seconds) at which the function should poll for job status.
            timeout: The maximum amount of time (as float, in seconds) to wait for the job to finish before timing out.
            solver_logs: A list of `SolverLog` objects to update with the current log of the job.
            batch_size: The size of the batch for the job as an integer.
            new_incumbent_callback: (optional) A callback function to call if a new incumbent is found in the batch item. Defaults to None.

        Returns:
            JobStatus: A `JobStatus` enum value indicating whether the job has finished, terminated, or timed out.
        """
        printed_created = False
        printed_running = False
        spinner = yaspin()

        batch_num_incumbents = [0] * batch_size

        for t in range(0,int(timeout/poll_frequency)):

            sleep(poll_frequency)

            try:
                status = self.https_client.checkJob(jobid=jobid)
            except RuntimeError as runtime_e:
                sys.exit(f"{self._error_symbol} Unable to check job:\n\n{runtime_e}")

            if printed_running and not self.suppress_output:
                try:
                    logs = self.https_client.getCurrentLog(jobid=jobid)
                except RuntimeError as runtime_e:
                    sys.exit(f"{self._error_symbol} Unable to get log:\n\n{runtime_e}")

                for ix in range(0, batch_size):
                    solver_logs[ix].updateLog(logs[ix])

            # stop spinner if necessary: for small problems polling interval might be too long to ever reach JobStatus.running
            if (status == JobStatus.running or status == JobStatus.finished) and not printed_running and not self.suppress_output:
                spinner.text = f"Job {jobid} unqueued, processing..."
                spinner.ok("✔")
                spinner.stop()
                solver_logs[0].nextTimeAddNewLine()
                printed_running = True

            # note: we do not give an error status to the job, but rather do
            # this on the batch item level (as part of getResults)
            if status == JobStatus.finished:
                return JobStatus.finished
            elif status == JobStatus.terminated:
                return JobStatus.terminated
            elif status == JobStatus.error:
                return JobStatus.error
            elif status == JobStatus.created:
                if not self.suppress_output:
                    if not printed_created:
                        printed_created = True
                        spinner.text = "Waiting for a free slot in the queue..."
                        spinner.start()
                        solver_logs[0].nextTimeAddNewLine()
            elif status == JobStatus.running:
                # check whether we got a new solution in any of the batch items
                if new_incumbent_callback is not None:
                    try:
                        batch_solutions = self.https_client.getCurrentSolution(jobid=jobid)
                    except RuntimeError as runtime_e:
                        sys.exit(f"{self._error_symbol}: " + str(runtime_e))

                    for ix in range(0, batch_size):
                        if int(batch_solutions[ix]["incumbents"]) > batch_num_incumbents[ix]:
                            new_incumbent_callback(ix, batch_solutions[ix]["objective"], batch_solutions[ix]["solution"])
                            batch_num_incumbents[ix] = int(batch_solutions[ix]["incumbents"])

        return JobStatus.timeout

    async def waitForJobAsync(self, jobid: uuid, poll_frequency: float, timeout: float, solver_logs: list, batch_size : int, new_incumbent_callback = None) -> JobStatus:
        """
        Asynchronously polls the status of a job identified by `jobid` until it reaches a final status or until the timeout is exceeded. The function updates the solver logs and calls the new incumbent callback function if a new incumbent is found in the batch item.

        Args:
            jobid: A UUID that identifies the job to poll the status for.
            poll_frequency: The frequency (as float, in seconds) at which the function should poll for job status.
            timeout: The maximum amount of time (as float, in seconds) to wait for the job to finish before timing out.
            solver_logs: A list of `SolverLog` objects to update with the current log of the job.
            batch_size: The size of the batch for the job as integer.
            new_incumbent_callback: (optional) A callback function to call if a new incumbent is found in the batch item. Defaults to None.

        Returns:
            JobStatus: A `JobStatus` enum value indicating whether the job has finished, terminated, or timed out.
        """

        printed_created = False
        printed_running = False
        spinner = yaspin()

        batch_num_incumbents = [0] * batch_size

        for t in range(0,int(timeout/poll_frequency)):

            await asyncio.sleep(poll_frequency)

            try:
                status = await self.https_client.checkJobAsync(jobid=jobid)
            except RuntimeError as runtime_e:
                sys.exit(f"{self._error_symbol} Unable to check job:\n\n{runtime_e}")

            if printed_running and not self.suppress_output:
                try:
                    logs = await self.https_client.getCurrentLogAsync(jobid=jobid)
                except RuntimeError as runtime_e:
                    sys.exit(f"{self._error_symbol}: " + str(runtime_e))
                for ix in range(0, batch_size):
                    solver_logs[ix].updateLog(logs[ix])

            # stop spinner if necessary: for small problems polling interval might be too long to ever reach JobStatus.running
            if (status == JobStatus.running or status == JobStatus.finished) and not printed_running and not self.suppress_output:
                spinner.text = f"Job {jobid} unqueued, processing..."
                spinner.ok("✔")
                spinner.stop()
                solver_logs[0].nextTimeAddNewLine()
                printed_running = True

            if status == JobStatus.finished:
                return JobStatus.finished
            elif status == JobStatus.terminated:
                return JobStatus.terminated
            elif status == JobStatus.error:
                return JobStatus.error
            elif status == JobStatus.created:
                if not self.suppress_output:
                    if not printed_created:
                        printed_created = True
                        spinner.text = "Waiting for a free slot in the queue..."
                        spinner.start()
                        solver_logs[0].nextTimeAddNewLine()

            elif status == JobStatus.running:
                # check whether we got a new solution in any of the batch items
                if new_incumbent_callback is not None:
                    try:
                        batch_solutions = await self.https_client.getCurrentSolutionAsync(jobid=jobid)
                    except RuntimeError as runtime_e:
                        sys.exit(f"{self._error_symbol}: " + str(runtime_e))

                    for ix in range(0, batch_size):
                        if int(batch_solutions[ix]["incumbents"]) > batch_num_incumbents[ix]:
                            new_incumbent_callback(ix, batch_solutions[ix]["objective"], batch_solutions[ix]["solution"])
                            batch_num_incumbents[ix] = int(batch_solutions[ix]["incumbents"])

        return JobStatus.timeout

    def solve(self, problem_file: str, params: HybridSolverParameters = None, tag : str = "", **kwargs):
        """
        Submits a QUBO or MIP instance to the solver.

        Args:
            problem_file (str): Path to problem file as string.
            params (HybridSolverParameters): HybridSolverParameter object.

        Keyword arguments:
            submit_callback: (optional) Custom callback function that is called when a job is submitted. Defaults to None.
            poll_frequency (float): (optional) The frequency (as float, in seconds) at which the function should poll for job status. Defaults to 1.
            new_incumbent_callback: (optional) A callback function to call if a new incumbent is found in the batch item. Defaults to None.
            timeout (float): (optional) The maximum amount of time (as float, in seconds) to wait for the job to finish before timing out. Defaults to 14400.

        Returns:
            dict: Solver results as dictionary containing the keys 'status', 'solver_log', 'sol_status', 'timing', 'objective', 'bound', 'absolute_gap', 'relative_gap', 'iterations', 'nodes', 'nodes_per_sec', 'best_node', 'best_time', 'num_quantum_solutions', 'solver_mix', and 'solution'.
        """
        if params is None:
            params = HybridSolverParameters()

        res, time_billed = self.solveBatched([problem_file], [params], tag, **kwargs)
        return res[0], time_billed


    ###
    # kwargs:
    # - submit_callback(jobid): called when job is submitted, receives jobid as parameter
    ###
    def solveBatched(self, problem_files: list, params: list = [], tag : str = "", **kwargs):
        """
        Submits a set of QUBO or MIP instances to the cloud for solving.

        Args:
            problem_files (List[str]): List of paths to problem files as string.
            params (List[HybridSolverParameters]): List of HybridSolverParameter objects.

        Keyword arguments:
            submit_callback: (optional) Custom callback function that is called when a job is submitted. Defaults to None.
            poll_frequency (float): (optional) The frequency (as float, in seconds) at which the function should poll for job status. Defaults to 1.
            new_incumbent_callback: (optional) A callback function to call if a new incumbent is found in the batch item. Defaults to None.
            timeout  (float): (optional) The maximum amount of time (as float, in seconds) to wait for the job to finish before timing out. Defaults to 14400.

        Returns:
            List[Dict[str, Any]]: List of solver results. For each submitted instance it contains a dictionary with the keys 'status', 'solver_log', 'sol_status', 'timing', 'objective', 'bound', 'absolute_gap', 'relative_gap', 'iterations', 'nodes', 'nodes_per_sec', 'best_node', 'best_time', 'num_quantum_solutions', 'solver_mix', and 'solution'.
        """

        # parse keyword args
        poll_frequency, timeout, new_incumbent_callback, submit_callback, job_options = self._parseKwargs(**kwargs)
        # get batch size
        batch_size = len(problem_files)
        # prepare solver logs
        solver_logs = [SolverLog() for ix in range(0, batch_size)]

        # initialize params list if it is not passed
        if params == []:
            params = [HybridSolverParameters() for _ in problem_files]
        specs = build_specs_list(params, problem_files, job_options)


        if not self.suppress_output:
            spinner = yaspin()
            spinner.start()
            spinner.text = "Submitting job to the Quantagonia cloud..."
            spinner.start()
        try:
            context = kwargs["context"] if 'context' in kwargs.keys() else ""
            jobid = self.https_client.submitJob(
                problem_files=problem_files, specs=specs, tag=tag, context=context)
            if("submit_callback" in kwargs):
                kwargs["submit_callback"](jobid)
        except RuntimeError as runtime_e:
            if not self.suppress_output:
                spinner.text = "Cannot submit job"
                spinner.ok(self._error_symbol)
                spinner.stop()
            sys.exit(str(runtime_e))
        except FileNotFoundError as fnf_e:
            if not self.suppress_output:
                spinner.text = "File not found"
                spinner.ok(self._error_symbol)
                spinner.stop()
            sys.exit(str(fnf_e))

        if not self.suppress_output:
            spinner.text = f"Queued job with jobid: {jobid} for execution in the Quantagonia cloud..."
            spinner.ok("✔")
            spinner.stop()

        status: JobStatus = self.waitForJob(jobid=jobid, poll_frequency=poll_frequency, timeout=timeout,
            solver_logs=solver_logs, batch_size=batch_size, new_incumbent_callback=new_incumbent_callback)

        if status is not JobStatus.finished:
            raise Exception(f"Job with jobid {jobid} error. Status of the job: {status}")
        else:
            if not self.suppress_output:
                print(f"Finished processing job {jobid}...")

        try:
            res, time_billed = self.https_client.getResults(jobid=jobid)
        except RuntimeError as runtime_e:
            sys.exit(f"{self._error_symbol}: " + str(runtime_e))

        if not self.suppress_output:
            for ix in range(0, batch_size):
                solver_logs[ix].updateLog(res[ix]['solver_log'])

        # parse solver logs and add solution
        for ix in range(0, batch_size):
            # parse and add solve stats
            logparser = SolverLogParser(res[ix]["solver_log"])
            res[ix].update(logparser.get_solver_summary())
            # add solution
            res[ix]["solution"] = SolutionParser.parse(res[ix]["solution_file"])
            # no need to keep the solution file
            res[ix].pop("solution_file")

        return res, time_billed

    async def solveAsync(self, problem_file: str, params: HybridSolverParameters = None, tag : str = "", **kwargs):
        """
        Asynchonously submits a QUBO or MIP instance to the cloud for solving.

        Args:
            problem_file (str): Path to problem file as string.
            spec (dict): A dictionary of solver options and parameters.

        Keyword arguments:
            submit_callback: (optional) Custom callback function that is called when a job is submitted. Defaults to None.
            poll_frequency (float): (optional) The frequency (as float, in seconds) at which the function should poll for job status. Defaults to 1.
            new_incumbent_callback: (optional) A callback function to call if a new incumbent is found in the batch item. Defaults to None.
            timeout (float): (optional) The maximum amount of time (as float, in seconds) to wait for the job to finish before timing out. Defaults to 14400.

        Returns:
            dict: Solver results as dictionary containing the keys 'status', 'solver_log', 'sol_status', 'timing', 'objective', 'bound', 'absolute_gap', 'relative_gap', 'iterations', 'nodes', 'nodes_per_sec', 'best_node', 'best_time', 'num_quantum_solutions', 'solver_mix', and 'solution'.
        """
        if not params:
            params = HybridSolverParameters()

        res, time_billed = await self.solveBatchedAsync([problem_file], [params], tag, **kwargs)
        return res[0], time_billed

    async def solveBatchedAsync(self, problem_files: list, params: list = [], tag : str = "", **kwargs):
        """
        Asynchronously submits a set of QUBO or MIP instances to the cloud for solving.

        Args:
            problem_files (List[str]): List of paths to problem files as string.
            specs (List[HybridSolverParameters]): List of HybridSolverParameters

        Keyword arguments:
            submit_callback: (optional) Custom callback function that is called when a job is submitted. Defaults to None.
            poll_frequency (float): (optional) The frequency (as float, in seconds) at which the function should poll for job status. Defaults to 1.
            new_incumbent_callback: (optional) A callback function to call if a new incumbent is found in the batch item. Defaults to None.
            timeout (float): (optional) The maximum amount of time (as float, in seconds) to wait for the job to finish before timing out. Defaults to 14400.

        Returns:
            List[Dict[str, Any]]: List of solver results. For each submitted instance it contains a dictionary containing the keys 'status', 'solver_log', 'sol_status', 'timing', 'objective', 'bound', 'absolute_gap', 'relative_gap', 'iterations', 'nodes', 'nodes_per_sec', 'best_node', 'best_time', 'num_quantum_solutions', 'solver_mix', and 'solution'.
        """

        # parse keyword args
        poll_frequency, timeout, new_incumbent_callback, submit_callback, job_options = self._parseKwargs(**kwargs)
        # get batch size
        batch_size = len(problem_files)
        # prepare solver logs
        solver_logs = [SolverLog() for ix in range(0, batch_size)]

        # initialize params list if it is not passed
        if params == []:
            params = [HybridSolverParameters() for _ in problem_files]
        specs = build_specs_list(params, problem_files, job_options)


        if not self.suppress_output:
            spinner = yaspin()
            spinner.start()
            spinner.text = "Submitting job to the Quantagonia cloud..."
            spinner.start()
        try:
            context = kwargs["context"] if 'context' in kwargs.keys() else ""
            jobid = await self.https_client.submitJobAsync(
                problem_files=problem_files, specs=specs, tag=tag, context=context)
        except RuntimeError as runtime_e:
            if not self.suppress_output:
                spinner.text = "Cannot submit job"
                spinner.ok(self._error_symbol)
                spinner.stop()
            sys.exit(str(runtime_e))
        except FileNotFoundError as fnf_e:
            if not self.suppress_output:
                spinner.text = "File not found"
                spinner.ok(self._error_symbol)
                spinner.stop()
            sys.exit(str(fnf_e))

        if not self.suppress_output:
            spinner.text = f"Queued job with jobid: {jobid} for execution in the Quantagonia cloud..."
            spinner.ok("✔")
            spinner.stop()

        status: JobStatus = await self.waitForJobAsync(jobid=jobid, poll_frequency=poll_frequency, timeout=timeout,
            solver_logs=solver_logs, batch_size=batch_size, new_incumbent_callback=new_incumbent_callback)

        if status is not JobStatus.finished:
            raise Exception(f"Job with jobid {jobid} error. Status of the job: {status}")
        else:
            if not self.suppress_output:
                print(f"Finished processing job {jobid}...")

        try:
            res, time_billed = self.https_client.getResults(jobid=jobid)
        except RuntimeError as runtime_e:
            sys.exit(f"{self._error_symbol}: " + str(runtime_e))
        if not self.suppress_output:
            for ix in range(0, batch_size):
                solver_logs[ix].updateLog(res[ix]['solver_log'])

        for ix in range(0, batch_size):
            # parse and add solve stats
            logparser = SolverLogParser(res[ix]["solver_log"])
            res[ix].update(logparser.get_solver_summary())
            # add solution
            res[ix]["solution"] = SolutionParser.parse(res[ix]["solution_file"])
            # no need to keep the solution file
            res[ix].pop("solution_file")

        return res, time_billed


    def interrupt_job(self, jobid: uuid):
        """
        Sends an interrupt signal to stop the execution of the specified job.

        Args:
            jobid (uuid): The UUID of the job to be interrupted.

        Returns:
            dict: A dictionary containing the response from the server.
        """
        resp = self.https_client.interrupt_job(jobid)
        return resp

    async def interrupt_job_async(self, jobid:uuid):
        """
        Asynchronously sends an interrupt signal to stop the execution of a submitted job.

        Args:
            jobid (uuid): The UUID of the job to be interrupted.

        Returns:
            dict: A dictionary containing the response from the server.
        """
        resp = await self.https_client.interruptJobAsync(jobid)
        return resp



#################################
# helper functions
#################################

def build_specs_list(params: list, problem_files: list, job_options: dict):
    """
    Build a list of spec dictionaries consisting of solver parameters and the problem type.
    Here we use the file suffix to determine the problem type.
    A proper problem type detection is done serverside.
    """

    specs = []
    for idx, param in enumerate(params):
        spec = {
            "solver_config": param.getd(),
            "problem_type": get_problem_type_from_filename(problem_files[idx]).value,
            "processing": job_options
        }
        specs.append(spec)

    return specs

def get_problem_type_from_filename(problem_file_name):
    # remove suffixes
    problem_file_name = pathlib.Path(problem_file_name)
    suffixes = problem_file_name.suffixes
    suffixes.reverse()  # reverse list to check last suffix first
    for suffix in suffixes:
        if suffix in [".qubo"]:
            return HybridSolverProblemType.QUBO
        elif suffix in [".lp", ".mps"]:
            return HybridSolverProblemType.MIP

    raise RuntimeError("Could not detect problem type.")
