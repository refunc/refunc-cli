build: clean
	python -m build --sdist

publish: build
	twine upload -r pypi dist/*


install: build
	pip uninstall -y refunc-cli
	pip install dist/refunc-cli*

clean:
	@rm -rf dist *.egg-info