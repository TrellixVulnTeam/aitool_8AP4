rm dist/*
python setup.py bdist_wheel
python setup.py sdist
python -m twine upload dist/*