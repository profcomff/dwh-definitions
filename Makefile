configure: venv
	source ./venv/bin/activate && pip install -U -r requirements.dev.txt -r requirements.txt

venv:
	python -m venv venv

format: venv
	source ./venv/bin/activate && autoflake -r --in-place --remove-all-unused-imports ./profcomff_definitions
	source ./venv/bin/activate && isort ./profcomff_definitions
	source ./venv/bin/activate && black ./profcomff_definitions

	source ./venv/bin/activate && autoflake -r --in-place --remove-all-unused-imports ./migrations
	source ./venv/bin/activate && isort ./migrations
	source ./venv/bin/activate && black ./migrations

test: venv migrate
	source ./venv/bin/activate && python3 -m pytest --verbosity=2 --showlocals --log-level=DEBUG

migrate: venv
	source ./venv/bin/activate && alembic upgrade head

sampler: venv
	python profcomff_definitions/instruments/sampler.py $(func) $(class_name)                                             