"""
ecoinvent v3 and Ember Climate

All emissions to air for the cycle.
"""
from functools import reduce
from typing import Tuple

from hestia_earth.utils.tools import list_sum, flatten
from hestia_earth.schema import EmissionMethodTier

from hestia_earth.models.log import logShouldRun, logRequirements, log_blank_nodes_id
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.blank_node import group_by_keys
from hestia_earth.models.utils.completeness import _is_term_type_complete
from hestia_earth.models.utils.term import get_electricity_grid_mix_terms
from .utils import get_emission, get_all_emission_terms

REQUIREMENTS = {
    "Cycle": {
        "site": {
            "@type": "Site",
            "country": {"@type": "Term", "termType": "region"}
        },
        "inputs": [{
            "@type": "Input",
            "term.@id": ["electricityGridMarketMix", "electricityGridRenewableMix"],
            "value": ""
        }],
        "completeness.electricityFuel": "True"
    }
}
RETURNS = {
    "Emission": [{
        "value": "",
        "methodTier": "background",
        "@type": "Emission",
        "inputs": ""
    }]
}
LOOKUPS = {
    "region-ember-energySources": "using `country`",
    "ember-ecoinvent-mapping": ["ember", "ecoinventId", "ecoinventName"]
}

MODEL = 'ecoinventV3AndEmberClimate'
MODEL_KEY = 'impactAssessment'  # keep to generate entry in "model-links.json"
TIER = EmissionMethodTier.BACKGROUND.value


def _emission(value: float, term_id: str, inputs: list, operation: dict) -> dict:
    emission = _new_emission(term_id, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = TIER
    emission["inputs"] = list(inputs)
    if operation:
        emission["operation"] = operation
    return emission


def _grid_inputs(inputs: list, electricity_grid_terms: list):
    electricity_grid_term_ids = [v.get('@id') for v in electricity_grid_terms]
    return [
        i for i in inputs if i.get("term", {}).get("@id") in electricity_grid_term_ids
    ]


def _run_input(cycle: dict, inputs: list, emission_term_id: str, input_term: dict):
    inputs = _grid_inputs(inputs, [input_term])
    return [
        _emission(
            value=get_emission(
                term_id=emission_term_id,
                country=cycle.get("site", {}).get("country", {}).get("@id", ""),
                energy=list_sum(flatten([i.get("value", []) for i in op_inputs])),
                year=cycle.get("endDate", ""),
                model=MODEL
            ),
            term_id=emission_term_id,
            inputs=[input_term],
            operation=op_inputs[0].get("operation")
        )
        for op_inputs in _group_by_operation(inputs).values()
    ] if inputs else []


def _group_by_operation(inputs: list) -> dict:
    return reduce(group_by_keys(['operation']), inputs, {})


def _run_emission(cycle: dict, electricity_grid_terms: list, inputs: list, emission_term_id: str) -> list:
    return flatten([
        _run_input(
            cycle=cycle,
            inputs=inputs,
            emission_term_id=emission_term_id,
            input_term=input_term
        ) for input_term in electricity_grid_terms
    ])


def _should_run_emission(cycle: dict, electricity_grid_terms: list, term_id: str) -> Tuple[bool, list]:
    term_type_complete = _is_term_type_complete(cycle, 'electricityFuel')
    inputs = _grid_inputs(cycle.get('inputs', []), electricity_grid_terms)
    has_relevant_inputs = bool(inputs)
    has_country = bool(cycle.get("site", {}).get("country", {}))

    logRequirements(cycle, model=MODEL, term=term_id,
                    input_ids=log_blank_nodes_id(inputs))

    should_run = all([term_type_complete, has_relevant_inputs, has_country])
    logShouldRun(cycle, MODEL, term_id, should_run, methodTier=TIER)
    return should_run, inputs


def _run_emissions(cycle: dict, electricity_grid_terms: list):
    def run_emissions_for_term(term_id: str) -> list:
        should_run, inputs = _should_run_emission(cycle, electricity_grid_terms, term_id)
        return _run_emission(cycle, electricity_grid_terms, inputs, term_id) if should_run else []
    return run_emissions_for_term


def run(cycle: dict):
    electricity_grid_terms = get_electricity_grid_mix_terms()
    return flatten(list(map(_run_emissions(cycle, electricity_grid_terms), get_all_emission_terms())))
