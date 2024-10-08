"""Setup file for clipea"""

from pathlib import Path

from setuptools import find_packages, setup

with Path("README.md").open(encoding="utf-8") as fp:
    long_description = fp.read()

setup(
    name="clipea-cli",
    version="0.1.0",
    description=" 📎🟢 Like Clippy but for the CLI. A blazing fast AI helper for your command line ",
    url="https://github.com/dave1010/clipea/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dave Hulbert",
    author_email="dave1010@gmail.com",
    keywords="cli, ai, assistant, automation",
    license="MIT",
    packages=find_packages(),
    install_requires=["llm"],
    python_requires=">=3.10",
    package_data={"clipea": ["*.txt", "clipea.zsh"]},
    entry_points={"console_scripts": ["clipea = clipea.__main__:clipea_main"]},
)
