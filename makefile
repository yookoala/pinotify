PACKAGE_NAME := pinotify

build:
	python3 -m build

clean:
	rm -Rf dist/

publish-test:
	python3 -m twine upload --verbose --repository testpypi dist/*
	python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps $(PACKAGE_NAME)

publish:
	python3 -m twine upload --verbose --repository pypi dist/*
	python3 -m pip install --index-url https://pypi.org/simple/ --no-deps $(PACKAGE_NAME)

.PHONY: clean build publish-test publish deb
