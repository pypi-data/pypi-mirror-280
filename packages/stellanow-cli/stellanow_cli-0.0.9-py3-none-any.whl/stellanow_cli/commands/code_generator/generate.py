"""
Copyright (C) 2022-2024 Stella Technologies (UK) Limited.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
"""

import importlib
import os
from typing import Any, List

import click
from loguru import logger
from prettytable import PrettyTable

from stellanow_cli.core.helpers import ensure_destination_exists
from stellanow_cli.exceptions.cli_exceptions import StellaNowCLIException, StellaNowCLILanguageNotSupportedException
from stellanow_cli.services.code_generator.code_generator import CodeGeneratorService, pass_code_generator_service


class SkippedFile:
    def __init__(self, filename: str, reason: str):
        self.filename = filename
        self.reason = reason

    def __iter__(self):
        return iter([self.filename, self.reason])


def print_skipped_result(skipped_files: List[SkippedFile]):
    if skipped_files:
        logger.info("\n==============================\n         SUMMARY\n==============================\n")

        table = PrettyTable(["File", "Skipping Reason"])

        # Populate the table with data from your SkippedFile instances
        for skipped_file in skipped_files:
            table.add_row([skipped_file.filename, skipped_file.reason])

        logger.info(table)

        logger.info("\nSkipped Reason - Explanation:\n")
        logger.info(
            "- File Already Exist - Existing classes can't be overriden. Use --force to override this protection."
        )
        logger.info(
            "- Missing Event Configuration - Check if the specified event does exists in then Operators Console."
        )
        logger.info("- No Entity Associated With Event - Event exists, but it is not attached to any entity type.")


@click.command()
@click.option("--namespace", "-n", default="", help="The namespace for the generated classes.")
@click.option("--destination", "-d", default=".", help="The directory to save the generated classes.")
@click.option("--force", "-f", is_flag=True, help="Overwrite existing files.")
@click.option("--events", "-e", multiple=True, help="List of specific events to generate.")
@click.option(
    "--language",
    "-l",
    type=click.Choice(["csharp"], case_sensitive=False),
    default="csharp",
    help="The programming language for the generated classes.",
)
@pass_code_generator_service
def generate(
    service: CodeGeneratorService,
    destination: str,
    force: bool,
    events: List[str],
    language: str,
    **kwargs: dict[str, Any],
):
    """Fetches the latest event specifications from the API and generates corresponding class code in the desired
    programming language."""
    logger.info("Generating...")

    generator_class_name = f"{language.capitalize()}CodeGenerator"
    try:
        generator_class = getattr(
            importlib.import_module(f"stellanow_cli.code_generators.{language}_code_generator"), generator_class_name
        )
    except ImportError:
        raise StellaNowCLILanguageNotSupportedException(language)

    events_not_found = set(events) if events else set()
    events_skipped = set()

    _events = service.get_events()
    for event in _events:
        if events and event.name not in events:
            continue

        events_not_found.discard(event.name)  # remove event from 'not found' list
        logger.info(f"Generating class for event: {event.name}")

        generator = generator_class()

        # Save the code to a file
        file_path = os.path.join(destination, generator.get_file_name_for_event_name(event.name))
        if not force and os.path.exists(file_path):
            logger.info("Skipped ...")
            events_skipped.add(SkippedFile(event.name, "File Already Exist"))  # add event to skipped list
            continue

        code = None

        try:
            code = generator.generate_class(service.get_event_details(event.id), **kwargs)
        except StellaNowCLIException as e:
            logger.info("Skipped ...")
            events_skipped.add(SkippedFile(event.name, e.message))  # add event to skipped list
            continue

        if code:
            ensure_destination_exists(destination)
            with open(file_path, "w") as file:
                file.write(code)

    print_skipped_result(
        list(events_skipped) + [SkippedFile(file_name, "Missing Event Configuration") for file_name in events_not_found]
    )


generate_cmd = generate
