from setuptools import setup, find_packages

__version__ = "0.0.2"

setup(
    name="Time2Feat",
    version=__version__,
    description="A new method for clustering multivariate time series by adopting the best statistical features.",
    author="Del Buono Francesco, Tiano Donato",
    author_email="donatotiano@gmail.com",
    packages=find_packages(),
    zip_safe=True,
    license="",
    url="https://github.com/protti/time2feat",
    entry_points={},
    install_requires=[
            'tsfresh~=0.20',
            'scikit-learn~=1.3',
            'numpy~=1.25',
            'pandas~=2.1',
            'tqdm~=4.66',
            'numba~=0.58',
            'dask~=2023.10',
            'scipy~=1.11'
        ]
)