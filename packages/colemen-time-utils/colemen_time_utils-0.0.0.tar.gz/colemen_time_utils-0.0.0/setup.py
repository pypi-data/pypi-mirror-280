from glob import glob
import os
from setuptools import setup, find_packages
import build_utils as _bu
# import build_utils.general as _gen


VERSION='0.0.0'
DESCRIPTION = 'Colemen Time Utils'
LONG_DESCRIPTION = 'Colemen Time Utils is a library of time related shit I find useful.'

_root_path = f"{os.getcwd()}/colemen_time_utilities"
PY_MODULES = _bu.general.list_py_modules(
    _root_path,
    additions=['colemen_time_utils']
)
_bu.general.purge_dist()

DATA_FILES = [
    # ('Lib/site-packages/colemen_utilities/documentation', glob('documentation/*.md')),
    # ('Lib/site-packages/colemen_utilities/build_utils', glob('colemen_utilities/build_utils/*.template')),
    # ('Lib/site-packages/colemen_utilities/random_utils', glob('colemen_utilities/random_utils/*.txt')),
    # ('', glob('exiftool.exe')),
]

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="colemen_time_utils",
    version=VERSION,
    author="Colemen Atwood",
    author_email="<atwoodcolemen@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    py_modules=PY_MODULES,
    # add any additional packages that
    # need to be installed along with your package. Eg: 'caer'
    install_requires=[
        # 'secure_delete',
    ],
    data_files=DATA_FILES,
    keywords=['python'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

