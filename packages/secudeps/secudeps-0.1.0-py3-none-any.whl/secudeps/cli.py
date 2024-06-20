import click
from secudeps.core import read_dependencies, assess_dependencies, generate_report

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
def main(file_path):
    """SecuDeps: A CLI tool to assess vulnerabilities in project dependencies."""
    dependencies = read_dependencies(file_path)
    assessments = assess_dependencies(dependencies)
    generate_report(assessments)

if __name__ == "__main__":
    main()
