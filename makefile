PACKAGE_NAME := pinotify

build:
	python3 -m build

clean:
	rm -Rf .venv/ dist/ deb_dist/

publish-test:
	python3 -m twine upload --verbose --repository testpypi dist/*
	python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps $(PACKAGE_NAME)

publish:
	python3 -m twine upload --verbose --repository pypi dist/*
	python3 -m pip install --index-url https://pypi.org/simple/ --no-deps $(PACKAGE_NAME)

deb: build
	py2dsc dist/$(PACKAGE_NAME)-*.tar.gz
	cd deb_dist/$(PACKAGE_NAME)-* && dpkg-buildpackage -b -uc -us

.PHONY: clean build publish-test publish deb
