## ipy2d

A small library to convert IP addresses to integers

#### Development

* Install dependencies from `setup.py` `python3 setup.py install`
* run *__main__.py* `python3 -m ipy2d`

#### Deploy

* create *dist* `python3 setup.py sdist bdist_wheel`
* check *dist* `twine check dist/*`
* publish *dist* `twine upload dist/* ` 
