bootstrap:
	@pip install -r requirements.txt
	@pip install -r requirements-dev.txt
	@pippython setup.py develop