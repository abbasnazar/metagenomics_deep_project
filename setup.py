from setuptools import setup, find_packages

setup(
    name='DeepArg',
    version='2.0',
    packages=find_packages(
        exclude=(".git", "data")
    ),
    include_package_data=True,
    package_data={},
    install_requires=[
        BioPython',
        'ete3',
        'h5py',
        'tqdm',
        'pandas',
        'networkx'
    ],
    python_requires=">=3.0",
    entry_points='''
        entry_points='''
        [console_scripts]
        deeparg=GeneTools.entry:cli
    ''',
)
