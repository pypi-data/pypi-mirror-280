from setuptools import setup, find_namespace_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='hemopi2',
    version='1.0',
    description='A tool to predict hemolytic activity of peptide',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='LICENSE.txt',
    url='https://github.com/raghavagps/hemopi2',
    packages=find_namespace_packages(where="src"),
    package_dir={'': 'src'},
    package_data={
        'hemopi2.merci': ['*'],
        'hemopi2.Model': ['*'],
        'hemopi2.motif': ['*'],
        'hemopi2.perl_scripts': ['*'],
        'hemopi2.Model.Data':['**/*'],
    },
    entry_points={ 'console_scripts' : ['hemopi2_regression = hemopi2.python_scripts.hemopi2_regression:main', 
                                        'hemopi2_classification = hemopi2.python_scripts.hemopi2_classification:main' ]},
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn==1.3.1',
        'transformers'
    ]
)
