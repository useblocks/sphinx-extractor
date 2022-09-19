import os
import re

from docutils.parsers.rst import Directive, directives
from sphinx.util import logging

logger = logging.getLogger(__name__)


class ExtractDirective(Directive):
    """Directive to extract rst code from text-based files."""

    required_arguments = 1
    option_spec = {
        "start": directives.unchanged_required,
        "end": directives.unchanged_required,
    }

    def run(self):
        env = self.state.document.settings.env

        extract_file_path = self.arguments[0]
        # check given file path
        if not os.path.isabs(extract_file_path):
            # relative path should starts from current rst file directory
            curr_dir = os.path.dirname(env.docname)
            found_extract_file_path = os.path.join(env.app.srcdir, curr_dir, extract_file_path)
        else:
            if not os.path.exists(extract_file_path):
                # check if given abs path starting from source directory
                # abs path starts with /, which need to be stripped
                found_extract_file_path = os.path.join(env.app.srcdir, extract_file_path[1:])
            else:
                found_extract_file_path = extract_file_path

        if not os.path.exists(found_extract_file_path):
            raise FileNotFoundError(f"Could not find file {found_extract_file_path}")

        # get option values
        pattern_start = self.options.get("start", None)
        pattern_end = self.options.get("end", None)

        # calculate extract pattern
        pattern = re.compile(f"{pattern_start}(.+){pattern_end}", flags=re.DOTALL)

        # get rst code
        found_rst_code = ""
        with open(found_extract_file_path, "r") as f:
            contents = f.read()

            # check if option value of start and end exists in given file
            if pattern_start not in contents:
                raise ExtractException(
                    f"Given value for option start: {pattern_start} not found "
                    f"in given file: {found_extract_file_path}."
                )
            if pattern_end not in contents:
                raise ExtractException(
                    f"Given value for option end: {pattern_end} not found in given file: {found_extract_file_path}."
                )

            match = re.search(pattern, contents)
            if match:
                found_rst_code = match.group(1)

        if found_rst_code:
            # check if extracted contents are rst code style
            rst_directive_role_match = re.search(r".. [A-Za-z-:_ ]+::|:[A-Za-z-:_ ]+:", found_rst_code)
            if not rst_directive_role_match:
                logger.warning(
                    f"Oops! Looks like the contents you are extracting are not rst code style like. "
                    f"Please check the file: {found_extract_file_path}"
                )

            rst_content = found_rst_code.splitlines()
            self.state_machine.insert_input(rst_content, self.state_machine.document.attributes["source"])
        else:
            logger.info(f"Could not find rst code based on given pattern from given file {found_extract_file_path}.")

        return []


class ExtractException(BaseException):
    """Errors during Extract handling."""
