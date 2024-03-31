deps:
	python -m pip install poetry
	poetry install

migrate:
	poetry run alembic upgrade head

run:
	poetry run uvicorn src.app:app --reload --host 0.0.0.0

