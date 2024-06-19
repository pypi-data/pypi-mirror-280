import os
from typing import Any, Dict, List

import click
import jsonpickle
from gable.helpers.repo_interactions import get_git_repo_info
from gable.openapi import ContractInput, ContractSpec, PostContractRequest, Status
from loguru import logger
from pydantic import ValidationError


def load_contract_from_file(file: click.File) -> Dict[str, Any]:
    if file.name.endswith(".yaml") or file.name.endswith(".yml"):
        import yaml

        try:
            return yaml.safe_load(file)  # type: ignore
        except yaml.scanner.ScannerError as exc:  # type: ignore
            # This should be a custom exception for user errors
            raise click.ClickException(f"Error parsing YAML file: {file.name}")
    elif file.name.endswith(".toml"):
        raise click.ClickException(
            "We don't currently support defining contracts with TOML, try YAML instead!"
        )
    elif file.name.endswith(".json"):
        raise click.ClickException(
            "We don't currently support defining contracts with JSON, try YAML instead!"
        )
    else:
        raise click.ClickException("Unknown filetype, try YAML instead!")


def contract_files_to_post_contract_request(
    contract_files: List[click.File],
) -> PostContractRequest:
    contracts = []
    for contract_file in contract_files:
        logger.debug(f"Loading contract from {contract_file.name}")
        with logger.contextualize(context=contract_file.name):
            contract = load_contract_from_file(contract_file)
            if "id" not in contract:
                raise click.ClickException(
                    f"{contract_file}:\n\tContract must have an id."
                )
            git_info = get_git_repo_info(contract_file.name)
            logger.debug(f"Git info: {jsonpickle.dumps(git_info)}")
            relative_path = os.path.relpath(
                contract_file.name, git_info["localRepoRootDir"]
            )
            logger.debug(f"Relative path: {relative_path}")
            if relative_path.startswith(".."):
                raise click.ClickException(
                    f"{contract_file.name}:\n\tContract must be located within the git repo where gable is being executed ({git_info['localRepoRootDir']})."
                )
            try:
                # Ignore the enforcement level if it's specified in the contract file, otherwise it will very likely overwrite changes in the UI every time
                # the contract publishing flow is run. We made contract publishing idempotent, and advise using a glob pattern to publish all contracts when
                # anything is merged to the main branch in the repo where contracts are defined. As a byproduct, even if this particular contract is not
                # being updated, its enforcement level will be overwritten to the value in the contract.
                # However, I'm leaving the enforcementLevel field in the contract spec for now so we get an exact copy of the contract YAML.
                # https://manifest-data.atlassian.net/browse/MFST-1320
                if "enforcementLevel" in contract:
                    logger.warning(
                        f"{contract_file.name}:\n\tIgnoring enforcementLevel in contract file, enforcementLevel is currently managed in the UI."
                    )

                contract_input = ContractInput(
                    id=contract["id"],
                    version="0.0.1",  # This should be server calculated
                    status=Status("ACTIVE"),
                    reviewers=[],  # This should be info accessible from a github PR integration
                    filePath=relative_path,
                    contractSpec=ContractSpec(**contract),
                    gitHash=git_info["gitHash"],
                    gitRepo=git_info["gitRemoteOriginHTTPS"],  # type: ignore
                    gitUser=git_info["gitUser"],
                    mergedAt=git_info["mergedAt"],
                )
                logger.debug(f"Contract Input: {contract_input.json()}")

                contracts.append(contract_input)
            except ValidationError as ve:
                logger.error(f"Error validating contract {contract_file.name}: {ve}")
                raise click.ClickException(
                    f"Error validating contract {contract_file.name}: {ve}"
                )

    return PostContractRequest(
        __root__=contracts,
    )
