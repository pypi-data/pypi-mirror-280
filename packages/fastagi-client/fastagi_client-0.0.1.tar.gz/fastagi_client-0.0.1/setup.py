from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="fastagi_client",
    version="0.0.1",
    packages=find_packages(exclude=["tests*"]),
    url="https://app.fastagi.khulnasoft.com",
    license="MIT",
    author="KhulnaSoft",
    author_email="info@khulnasoft.com",
    description="Python package for Fastagi",
    install_requires=["pydantic==1.10.13", "requests==2.32.2", "pytest==7.3.2"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
