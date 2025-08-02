PACKAGE_NAME := pinotify

build:
	python3 -m build

publish-test:
	python3 -m twine upload --verbose --repository testpypi dist/*
	python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps $(PACKAGE_NAME)

publish:
	python3 -m twine upload --verbose --repository pypi dist/*
	python3 -m pip install --index-url https://pypi.org/simple/ --no-deps $(PACKAGE_NAME)

.PHONY: build publish-test publish
