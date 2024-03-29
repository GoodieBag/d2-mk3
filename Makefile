setup-venv:
	pip install virtualenv
	python -m venv venv

setup-dev: requirements-dev.txt
	pip install -r requirements-dev.txt
	pre-commit install

setup: requirements.txt
	pip install -r requirements.txt

lint:
	black . --line-length 79
	flake8 --ignore=E203

test:
	pytest -vv

clean:
	rm -rf __pycache__