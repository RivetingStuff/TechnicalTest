import functools
import logging
from behave.model import ScenarioOutline


def patch_scenario_to_repeat(scenario, repeats=5):
    """credit to: https://github.com/behave/behave/blob/main/behave/contrib/scenario_autoretry.py

    This function repeats a scenario until the max_attempts is reached or one of the attempts fails.
    The resulting report will only include one scenario run, this is useful when looking for a known
    tempramental failure, but does mislead consumers of the report. Use sparingly and ideally for
    debugging.

    :param scenario:        Scenario or ScenarioOutline to patch.
    :param repeats:         How many times the scenario will be run.
    """

    def scenario_run_with_repeat(scenario_run, *args, **kwargs):
        for attempt in range(1, repeats + 1):
            logging.debug(f"Repeating scenario for attempt {attempt}/{repeats}")
            if scenario_run(*args, **kwargs):
                break
        else:
            logging.debug("All attempts successful")
            return False

        message = "REPEAT SCENARIO FAILED (after {0} attempts)"
        logging.debug(message.format(repeats))
        return True

    if isinstance(scenario, ScenarioOutline):
        scenario_outline = scenario
        for scenario in scenario_outline.scenarios:
            scenario_run = scenario.run
            scenario.run = functools.partial(scenario_run_with_repeat, scenario_run)
    else:
        scenario_run = scenario.run
        scenario.run = functools.partial(scenario_run_with_repeat, scenario_run)
