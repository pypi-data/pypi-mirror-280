from pathlib import Path

import scalify
import scalify.tools
import scalify.tools.filesystem
import scalify.tools.python
import scalify.tools.shell
from pydantic import BaseModel, Field
from scalify.beta.applications import Application

scalify.settings.log_level = "DEBUG"
scalify.settings.llm_model = "gpt-4o"


class TestWriterState(BaseModel):
    files_info: dict[str, str] = Field(
        default_factory=dict,
        description=(
            "A place to record notes about specific files, including any details e.g."
            ' {"path/to/file.py": "Main entrypoint"}'
        ),
    )
    tests_passing: bool = False


ROOT_DIR = Path(scalify.__file__).parents[2]

test_app = Application(
    name="TestWriter",
    description=f"""
        You are responsible for writing and maintaining the unit tests for the
        Scalify library, located at {ROOT_DIR}. You may only modify files inside
        {ROOT_DIR}. Scalify's tests are all stored in `tests/` and can be run
        with `pytest` from the directory root. 
        
        The user will give you instructions on what functionality to test or how
        to modify tests. When you write tests, you will need to ensure that the
        work and meet the user's expectation. Remember, you are an expert Python
        developer and you strive to write complete, readable, tests. You believe
        tests are the best form of documentation. Do not write tests that
        already exist, make sure you are adding valuable and interesting tests
        to the codebase.
        """,
    state=TestWriterState(),
    tools=[
        scalify.tools.filesystem.ListFiles(root_dir=ROOT_DIR),
        scalify.tools.filesystem.ReadFile(root_dir=ROOT_DIR),
        scalify.tools.filesystem.ReadFiles(root_dir=ROOT_DIR),
        scalify.tools.filesystem.WriteFiles(
            root_dir=ROOT_DIR, require_confirmation=False
        ),
        scalify.tools.python.Python(require_confirmation=False),
        scalify.tools.shell.Shell(
            require_confirmation=False, working_directory=ROOT_DIR
        ),
    ],
)
