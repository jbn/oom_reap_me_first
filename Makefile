.PHONY: build
build:
	# See: https://setuptools.pypa.io/en/latest/userguide/quickstart.html
	python -m build

deploy:
	# See: https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives
	python -m twine upload --repository oom_reap_me_first dist/*
