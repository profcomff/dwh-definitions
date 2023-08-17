from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="profcomff_definitions",
    version="2023.08.17",
    author="Stanislav Roslavtsev",
    url="https://github.com/profcomff/dwh-definitions",
    description="Data warehouse definitions and schemas",
    license='BDS',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["SQLAlchemy", "alembic", "setuptools"],
    author_email="roslavtzev.stanislaw@yandex.ru",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: BSD License"
    ],
)
