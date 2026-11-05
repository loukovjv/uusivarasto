"""Moduuli määrittelee Project-olion."""

class Project:
    """Edustaa projektin metatietoja."""

    def __init__(self, name, description, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def __str__(self):
        deps = "\n".join(f"- {dep}" for dep in self.dependencies)
        dev_deps = "\n".join(f"- {dev}" for dev in self.dev_dependencies)

        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Dependencies:\n{deps}\n\n"
            f"Development dependencies:\n{dev_deps}"
        )
