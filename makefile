
mypy: # check for type errors
	mypy main.py menu_class.py process_order_class.py summary_class.py test_classes.py ui_class.py
pytest: # does a quick unit test
	python3 -m unittest test_classes.py
run: # run program from main 
	python main.py
format: # formats using black
	ruff format --line-length 120 main.py menu_class.py process_order_class.py summary_class.py test_classes.py ui_class.py

install:
	pip install -r requirements.txt

# combined commands 

check: format mypy pytest 