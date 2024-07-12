
mypy: # check for type errors
	mypy main.py menu_class.py process_order_class.py summary_class.py test_classes.py ui_class.py
pytest: # test code
	pytest test_classes.py