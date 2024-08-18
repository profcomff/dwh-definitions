configure: venv
	pip install -U -r requirements.dev.txt -r requirements.txt

venv:
	python3.11 -m venv venv

format: venv
	source ./venv/bin/activate && autoflake -r --in-place --remove-all-unused-imports ./profcomff_definitions
	source ./venv/bin/activate && isort ./profcomff_definitions
	source ./venv/bin/activate && black ./profcomff_definitions

	source ./venv/bin/activate && autoflake -r --in-place --remove-all-unused-imports ./migrations
	source ./venv/bin/activate && isort ./migrations
	source ./venv/bin/activate && black ./migrations

test: venv migrate
	python3 -m pytest --verbosity=2 --showlocals --log-level=DEBUG

migrate: venv
	alembic upgrade head
