from setuptools import setup, find_packages

# Legge il contenuto del file README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="OffSecIta1",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[],
    author="Mr.Manimal",
    description="Biblioteca per consultare i corsi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.youtube.com/@Roby_kali",
)
