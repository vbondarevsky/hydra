import io
import os

from setuptools import find_packages, setup

NAME = "hydra"
here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, NAME, "__version__.py")) as f:
    exec(f.read(), about)


setup(
    name=NAME,
    version=about[NAME],
    description="Hydra agents management center",
    author="Vladimir Bondarevskiy",
    author_email="vbondarevsky@gmail.com",
    url="https://github.com/vbondarevsky/hydra",
    license="https://www.gnu.org/licenses/gpl-3.0",
    packages=find_packages(exclude=["tests", "tests.*", "front"]),
    python_requires=">=3",
    install_requires=[
        "aiohttp",
        "pyyaml",
        "SQLAlchemy",
    ],
    zip_safe=True,
    entry_points={
        "console_scripts": [
            "hydra = hydra.main:run"
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
