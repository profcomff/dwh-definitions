configure: venv
	pip install -U -r requirements.dev.txt -r requirements.txt

venv:
	python -m venv venv

format:
	autoflake -r --in-place --remove-all-unused-imports ./profcomff_definitions
	isort ./profcomff_definitions
	black ./profcomff_definitions

	autoflake -r --in-place --remove-all-unused-imports ./migrations
	isort ./migrations
	black ./migrations

test: venv migrate
	python3 -m pytest --verbosity=2 --showlocals --log-level=DEBUG

migrate: venv
	alembic upgrade head

# ex. make sampler func=upload_sample class_name=Info
sampler: venv
	python sampler.py $(func) $(class_name)