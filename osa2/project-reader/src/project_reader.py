"""Moduuli lukee projektin tiedot TOML-tiedostosta."""

from urllib import request
from project import Project

# pylint: disable=too-few-public-methods
class ProjectReader:
    """Lukee ja parsii projektin tiedot osoitteesta."""
    def __init__(self, url):
        self._url = url

    def get_project(self):
        """Hakee TOML-tiedoston ja palauttaa Project-olion."""
        content = request.urlopen(self._url).read().decode("utf-8")

        print("--- TIEDOSTON SISÄLTÖ ---")
        print(content)

        name = ""
        description = ""
        dependencies = []
        dev_dependencies = []

        current_section = None

        for line in content.splitlines():
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if line.startswith("[") and line.endswith("]"):
                current_section = line
                continue

            if "=" in line:
                parts = line.split("=", 1)
                key = parts[0].strip()
                value = parts[1].strip().strip('"').strip("'")

                if current_section == "[tool.poetry]":
                    if key == "name":
                        name = value
                    elif key == "description":
                        description = value

                elif (
                    current_section == "[tool.poetry.dependencies]"
                    and key != "python"
                ):
                    dependencies.append(key)
                elif current_section == "[tool.poetry.group.dev.dependencies]":
                    dev_dependencies.append(key)

        return Project(name, description, dependencies, dev_dependencies)
