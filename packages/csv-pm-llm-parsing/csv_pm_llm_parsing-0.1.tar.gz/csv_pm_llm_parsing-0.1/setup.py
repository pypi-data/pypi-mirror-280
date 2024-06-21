import runpy
from os.path import dirname, join
from pathlib import Path
from setuptools import setup, find_packages


# Import only the metadata of the pm4py to use in the setup. We cannot import it directly because
# then we need to import packages that are about to be installed by the setup itself.
meta_path = Path(__file__).parent.absolute() / "csv_pm_llm_parsing" / "meta.py"
meta = runpy.run_path(str(meta_path))


def read_file(filename):
    with open(join(dirname(__file__), filename)) as f:
        return f.read()


setup(
    name=meta['__name__'],
    version=meta['__version__'],
    description=meta['__doc__'].strip(),
    long_description=read_file('README.md'),
    author=meta['__author__'],
    author_email=meta['__author_email__'],
    py_modules=['csv_pm_llm_parsing'],
    include_package_data=True,
    packages=[x for x in find_packages() if x.startswith("csv_pm_llm_parsing")],
    url='https://github.com/fit-alessandro-berti/csv-pm-llm-parsing',
    license='Apache 2.0',
    install_requires=read_file("requirements.txt").split("\n"),
    project_urls={
        'Documentation': 'https://github.com/fit-alessandro-berti/csv-pm-llm-parsing',
        'Source': 'https://github.com/fit-alessandro-berti/csv-pm-llm-parsing',
        'Tracker': 'https://github.com/fit-alessandro-berti/csv-pm-llm-parsing/issues',
    }
)
