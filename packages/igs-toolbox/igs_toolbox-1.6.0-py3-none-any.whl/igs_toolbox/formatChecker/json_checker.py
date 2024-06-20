import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, Optional

import typer

if sys.version_info >= (3, 10):
    from typing import Annotated
else:
    from typing_extensions import Annotated
from datetime import datetime

import jsonschema

from igs_toolbox.file_utils import read_json_file
from igs_toolbox.formatChecker.seq_metadata_schema import (
    SeqMetadataKeys,
    ValidationError,
    loose_schema,
    seq_metadata_schema,
)
from igs_toolbox.log_utils import setup_logging
from igs_toolbox.version_utils import version_callback

if sys.version_info >= (3, 9):
    from zoneinfo import ZoneInfo
else:
    from backports.zoneinfo import ZoneInfo
NOW = datetime.now(tz=ZoneInfo("Europe/Berlin")).strftime("%Y-%m-%dT%H-%M-%S")
app = typer.Typer()
SCHEMA_NAME = "seqMetadata"


def validate_pathogen_specific_field(pathogen: str, folder: str, value: str) -> bool:
    """Validate pathogen specific field."""
    # get vocabulary for species
    answer_set_path = Path(__file__).parent / f"res/{folder}/txt/valueSet{pathogen}.txt"
    if not answer_set_path.is_file():
        logging.error(f"{answer_set_path} does not point to a file. Aborting.")
        return False

    with Path(answer_set_path).open() as file:
        allowed_values = [line.strip() for line in file]

    if value not in allowed_values:
        return False
    return True


def extract_error_message(schema_error: jsonschema.ValidationError) -> str:
    if len(schema_error.relative_path) == 0:
        return schema_error.message
    if schema_error.relative_path[0] in ["Files", "Uploads"]:
        return schema_error.message

    field_name = schema_error.relative_path.pop()
    constraint = schema_error.validator
    raw_message = schema_error.message
    invalid_value = schema_error.instance

    if isinstance(constraint, str) and constraint == "enum":
        enum_values = schema_error.validator_value
        if len(enum_values) > 3:  # noqa: PLR2004
            values = [repr(v) for v in enum_values[:3]]
            values.append("...")
            enum_string = f"[{', '.join(values)}]"
        else:
            enum_string = repr(enum_values)
        raw_message = f"{repr(invalid_value)} is not one of {enum_string}"  # noqa: RUF010

    return f"{field_name}: {repr(invalid_value)} violates constraint {repr(constraint)} ({raw_message})"  # noqa: RUF010


def check_seq_metadata(
    json_data: Dict[str, Any],
    *,
    strict_mode: bool = False,
) -> None:
    # Remove some constrains from schema if not running in strict mode
    schema = seq_metadata_schema if strict_mode else loose_schema(seq_metadata_schema)

    """Validate the sequence metadata."""
    validator = jsonschema.Draft202012Validator(
        schema=schema,
        # validating "format" constraints is disabled by default
        # https://python-jsonschema.readthedocs.io/en/stable/validate/#validating-formats
        format_checker=jsonschema.Draft202012Validator.FORMAT_CHECKER,
    )
    error_messages = [extract_error_message(error) for error in validator.iter_errors(json_data)]

    if strict_mode:
        # some validation rules cannot be implemented in jsonschema directly, thus check them here programmatically
        pathogen = json_data.get(SeqMetadataKeys.MELDETATBESTAND)
        if pathogen:
            species = json_data.get(SeqMetadataKeys.SPECIES)
            if species and not validate_pathogen_specific_field(pathogen, SeqMetadataKeys.SPECIES.lower(), species):
                error_messages.append(f"{repr(species)} is not a valid species for pathogen {pathogen}.")  # noqa: RUF010

            isolation_source = json_data.get(SeqMetadataKeys.ISOLATION_SOURCE)
            if isolation_source and not validate_pathogen_specific_field(
                pathogen,
                SeqMetadataKeys.ISOLATION_SOURCE.lower(),
                isolation_source,
            ):
                error_messages.append(
                    f"{repr(isolation_source)} is not a valid isolation_source for pathogen {pathogen}.",  # noqa: RUF010
                )
        else:
            error_messages.append(
                "Pathogen is not provided, hence isolation_source and species could not be validated.",
            )

    if error_messages:
        raise ValidationError(error_messages)


@app.command(name="jsonChecker", help="Validate metadata json.")
def check_json(
    input_file: Annotated[
        Path,
        typer.Option(
            "--input",
            "-i",
            dir_okay=False,
            file_okay=True,
            exists=True,
            help="Path to input json file.",
        ),
    ],
    strict_mode: Annotated[  # noqa: FBT002
        Optional[bool],
        typer.Option(
            "--strict",
            help="Perform strict validation.",
        ),
    ] = False,
    log_file: Annotated[
        Path,
        typer.Option("--log_file", "-l", dir_okay=False, help="Path to log file."),
    ] = Path(f"./jsonChecker_{NOW}.log"),
    version: Annotated[  # noqa: ARG001
        Optional[bool],
        typer.Option("--version", "-V", callback=version_callback, is_eager=True),
    ] = None,
) -> None:
    setup_logging(log_file=log_file, debug=False)
    # read json file
    try:
        json_data = read_json_file(input_file)
    except FileNotFoundError as e:
        logging.error(f"{input_file} does not point to a file. Aborting.")  # noqa: TRY400
        raise typer.Abort(1) from e
    except json.JSONDecodeError as e:
        logging.error(f"{input_file} is not a valid json file. Aborting.")  # noqa: TRY400
        raise typer.Abort from e

    # get schema
    try:
        check_seq_metadata(json_data, strict_mode=strict_mode)
    except ValidationError as e:
        logging.error(f"FAILURE: JSON file does not adhere to the {SCHEMA_NAME} schema.")  # noqa: TRY400
        for error_message in e.error_messages:
            logging.error(error_message)  # noqa: TRY400
        raise typer.Abort from e

    logging.info(f"SUCCESS: JSON file adheres to {SCHEMA_NAME} schema.")
    print(f"SUCCESS: JSON file adheres to {SCHEMA_NAME} schema.")  # noqa: T201


def main() -> None:
    """Entry point of CLI tool."""
    app()


if __name__ == "__main__":
    main()
