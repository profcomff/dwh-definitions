from setuptools import setup

setup(
    name="profcomff_definitions",
    version="2023.08.15",
    description="Data warehouse definitions and schemas",
    packages=["ddl, migrations"],
    author_email="roslavtzev.stanislaw@yandex.ru",
    zip_safe=False,
)
