test:
    pytest

install:
    python3 setup.py install

fmt:
    black ipy2d/ test/

build:
    python3 setup.py sdist bdist_wheel

check:
    twine check dist/*

deploy:
    twine upload dist/*