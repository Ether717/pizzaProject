mypy: # check for type errors
	mypy --check-untyped-defs main.py menu_class.py process_order_class.py summary_class.py test_classes.py ui_class.py
unittest: # does a quick unit test
	python3 -m unittest test_classes.py
run: # runs program from main 
	python3 main.py
format: # formats using black
	ruff format --line-length 120 main.py menu_class.py process_order_class.py summary_class.py test_classes.py ui_class.py
pylint: # checks for errors and bad practices
	pylint --disable=C0116,C0114,C0301,W0611,C0303,E0602,W0612,C0413,C0305,C0415 main.py menu_class.py process_order_class.py summary_class.py test_classes.py ui_class.py
ruff:
	ruff check main.py menu_class.py process_order_class.py summary_class.py test_classes.py ui_class.py
fix:
	ruff --fix main.py menu_class.py process_order_class.py summary_class.py test_classes.py ui_class.py
coverage: # checks code coverage
	coverage run -m unittest discover
	coverage report
	coverage html
install: # installs all 3rd party libraries
	pip install -r requirements.txt
install_utility: # installs utilitites for formatting and type checking
	pip install ruff mypy pylint coverage
uninstall:
	pip uninstall -r requirements.txt
clean: # cleans temporary files
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf htmlcov

# combined commands 
check: format mypy unittest 

full: format mypy unittest pylint # does a full check of code using linting, formatting, type checking, and unit testing

