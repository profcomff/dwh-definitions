import argparse

import instruments.functions as functions


parser = argparse.ArgumentParser(
    description="A simple python script to load data from prod/test database to your local database",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

parser.add_argument(
    "func", help=f"Function, witch you want to run. Available fuctions: {[f for f in functions.__all__]}"
)
parser.add_argument("class_name", help="Database table class name, from witch you want to load data")
parser.add_argument("-l", "--limit", help="Amout of records you want to load", type=int, default=20)

args = parser.parse_args()
config = vars(args)
if config["func"] not in functions.__all__:
    raise ValueError(f"Function {config['func']} not found")
else:
    func = getattr(functions, config["func"])
    func(config["class_name"], config["limit"])
