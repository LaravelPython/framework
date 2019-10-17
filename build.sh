rm -f -r dist/*
python setup.py sdist bdist_wheel
twine upload dist/*