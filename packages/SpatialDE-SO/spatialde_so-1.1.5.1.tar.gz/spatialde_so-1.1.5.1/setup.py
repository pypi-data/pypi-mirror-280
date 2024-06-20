from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent
ld = """ # SpatialDE

This package wraps SpatialDE so it can be installed and used using PyPI after fixing some bugs.

All SpatialDE credit goes to the SpatialDE authors. Please check the original publication for more details: [Nature Methods](https://www.nature.com/articles/nmeth.4636).

If you use this package, please cite the original SpatialDE publication.

 """

setup(
    name="SpatialDE-SO",
    version="1.1.5.1",
    description="Spatial and Temporal DE test. This is a fork containing some bug fixes.",
    long_description=ld,
    long_description_content_type="text/markdown",
    url="https://github.com/Mena-SA-Kamel/SpatialDE-SO",
    package_dir={"": "Python-module"},
    packages=find_packages(where="Python-module", include=["SpatialDE", "SpatialDE.*"]),
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy >= 1.0",
        "pandas>=0.23",
        "tqdm",
        "NaiveDE",
        "Click",
    ],
    entry_points=dict(
        console_scripts=["spatialde=SpatialDE.scripts.spatialde_cli:main"],
    ),
    author="Valentine Svensson",
    author_email="valentine@nxn.se",
    maintainer="Mena Kamel",
    maintainer_email="mena.kamel@sanofi.com",
    license="MIT",
)
