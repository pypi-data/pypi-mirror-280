from setuptools import find_packages, setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="randomchessgame",
    author="lot022",
    version="4.0.8",
    license="MIT",
    keywords="chess",
    python_requires=">=3.7",
    url="https://github.com/lot022/randomcg",
    description="Python library to come in handy when random chess game is neeed.",
    long_description=long_description,
    include_package_data=True,
    package_data={
        'randomchessgame': ['data/*.pgn', '*.txt'],
        'randomchessgame' : ['*/.pgn'],
        'randomchessgame' : ['GAMES.pgn'] 
    },
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    zip_safe = False,
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: Unix",
        "License :: OSI Approved :: MIT License",
        "Topic :: Games/Entertainment :: Board Games",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
