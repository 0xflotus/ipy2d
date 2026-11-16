#### Development

* Install dependencies with uv: `uv sync --group dev`

#### Lint and Format

`pylint ipy2d/`

`black ipy2d/`

#### Test

Run the test suite with uv: `uv run --group dev pytest -rxXs test/*`

#### Deploy

* create *dist* `python3 setup.py sdist bdist_wheel`
* check *dist* `twine check dist/*`
* publish *dist* `twine upload dist/*` 
