from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Test to make my own queue class'
LONG_DESCRIPTION = """
A procrastination effort,
i might add features in the future if i think of any.
But this was mostly a way for me to explore the Python Package envirement and experiment.
"""

setup(
        name="pyqueue_test", 
        version=VERSION,
        author="Torak Schoorens/enigma_ZER0",
        author_email="torak.schoorens@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/plain",
        packages=find_packages(),
        install_requires=[],

        keywords=['python3', 'first package', 'experiment'],
        classifiers= [
            "Development Status :: 1 - Planning",
            "Intended Audience :: Other Audience",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent"
        ]
)