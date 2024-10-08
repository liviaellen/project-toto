install:
	@pip install -e .

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -f */.ipynb_checkpoints
	@rm -Rf build
	@rm -Rf */__pycache__
	@rm -Rf */*.pyc

all: install clean

test:
	pytest -v

ggp:
	git add .
	git commit -m "update"
	git push origin master
