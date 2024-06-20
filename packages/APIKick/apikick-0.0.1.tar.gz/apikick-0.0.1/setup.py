from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="APIKick",
    description="Fast and easy to use Kick.com API",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["requests"],
    license="MIT",
    keywords=["kick", "api", "kickapi"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sikriet",
    url="https://github.com/Sikriet/KickApi",
)
