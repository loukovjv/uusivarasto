"""Pääohjelma projektin tietojen lukemiseen."""

from project_reader import ProjectReader


def main():
    """Pääohjelman suoritus."""
    url = (
        "https://raw.githubusercontent.com/ohjelmistotuotanto-jyu/"
        "tehtavat/refs/heads/main/osa2/stat/pyproject.toml"
    )
    reader = ProjectReader(url)
    print(reader.get_project())


if __name__ == "__main__":
    main()
