test:
    uv run --group dev pytest

install:
    uv pip install -e .

fmt:
    black ipy2d/ test/

build:
    python3 setup.py sdist bdist_wheel

check:
    twine check dist/*

deploy:
    twine upload dist/*