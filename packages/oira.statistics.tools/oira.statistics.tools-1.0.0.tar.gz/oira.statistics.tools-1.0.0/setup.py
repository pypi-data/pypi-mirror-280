from setuptools import find_packages
from setuptools import setup

import os


version = "1.0.0"

setup(
    name="oira.statistics.tools",
    version=version,
    description="Statistics tools for OSHA OiRA",
    long_description=open("README.md").read()
    + "\n"
    + open(os.path.join("docs", "changes.rst")).read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="euphorie osha oira",
    author="syslab.com",
    author_email="info@syslab.com",
    url="http://www.oira.osha.europa.eu/",
    license="GPL",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["oira", "oira.statistics"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "osha.oira",
        "oira.statistics.deployment",
        "setuptools",
    ],
    extras_require={
        "tests": [
            "alchemy_mock",
        ],
    },
    entry_points="""
      [console_scripts]
      update_statistics = oira.statistics.tools.scripts:update_statistics
      """,
)
