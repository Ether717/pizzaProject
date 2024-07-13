
mypy: # check for type errors
	mypy main.py menu_class.py process_order_class.py summary_class.py test_classes.py ui_class.py
unittest: # does a quick unit test
	python3 -m unittest test_classes.py
run: # runs program from main 
	python3 main.py
format: # formats using black
	ruff format --line-length 120 main.py menu_class.py process_order_class.py summary_class.py test_classes.py ui_class.py
pylint: # checks for errors and bad practices
	pylint --disable=C0116,C0114,C0301,W0611,C0303,E0602,W0612,C0413,C0305,C0415 main.py menu_class.py process_order_class.py summary_class.py test_classes.py ui_class.py
install: # installs all 3rd party libraries
	pip install -r requirements.txt
install_utility: # installs utilitites for formatting and type checking
	pip install ruff mypy pylint



# combined commands 
check: format mypy unittest 

full: format mypy unittest pylint # does a full check of code using linting, formmating, type checking, and unit testing