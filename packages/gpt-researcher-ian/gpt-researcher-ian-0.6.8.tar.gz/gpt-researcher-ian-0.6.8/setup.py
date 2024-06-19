from setuptools import find_packages, setup

exclude_packages = ["selenium", "webdriver", "fastapi", "fastapi.*", "uvicorn", "jinja2"]

with open(r"README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    reqs = [line.strip() for line in f if not any(pkg in line for pkg in exclude_packages)]

setup(
    name="gpt-researcher-ian",
    version="0.6.8",
    description="GPT Researcher is an autonomous agent designed for comprehensive online research on a variety of tasks.",
    package_dir={'gpt_researcher_ian': 'gpt_researcher_ian'},
    packages=find_packages(include=["gpt_researcher_ian", "gpt_researcher_ian.*"], exclude=exclude_packages),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/assafelovic/gpt-researcher",
    author="Ian de Jesus",
    author_email="iandjx@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    install_requires=reqs,


)