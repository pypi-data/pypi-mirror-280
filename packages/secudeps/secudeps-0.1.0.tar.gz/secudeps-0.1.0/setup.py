from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("CHANGELOG.md", "r") as ch:
    changelog = ch.read()

setup(
    name="secudeps",
    version="0.1.0",
    author="Saber Boukhriss",
    author_email="saber@securas.fr",
    description="A CLI tool to assess vulnerabilities in project dependencies",
    long_description=f"{long_description}\n\n{changelog}",
    long_description_content_type="text/markdown",
    url="https://gitlab.com/saber.bks/secudeps",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
        "pandas",
        "click",
    ],
    entry_points={
        'console_scripts': [
            'secudeps=secudeps.cli:main',
        ],
    },
)
