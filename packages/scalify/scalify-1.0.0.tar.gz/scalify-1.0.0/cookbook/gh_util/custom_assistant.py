from gh_util.api import functions  # pip install gh-util
from pydantic import BaseModel, Field
from scalify.beta.applications import Application


class Memory(BaseModel):
    notes: list[str] = Field(default_factory=list)


octocat = Application(
    name="octocat",
    state=Memory(),
    tools=[f for f in functions if f.__name__ != "run_git_command"],
)

# $ scalify assistant register cookbook/gh_util/custom_assistant.py:octocat

# > what's the latest release of khulnasoft/scalify?

# see https://github.com/KhulnaSoft/scalify/pull/875
