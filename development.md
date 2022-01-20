#### Development

* Install dependencies from `setup.py` `python3 setup.py install`
* run *__main__.py* `python3 -m ipy2d`

#### Lint and Format

`pylint ipy2d/`

`black ipy2d/`

#### Test

If `pytest` is installed, you can run `pytest -rxXs test/*`

#### Deploy

* create *dist* `python3 setup.py sdist bdist_wheel`
* check *dist* `twine check dist/*`
* publish *dist* `twine upload dist/*` 
