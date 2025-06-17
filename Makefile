.PHONY:	run	dev	test	lint	format	update

run:
	poetry	run	uvicorn	app.main:app	--reload

dev:
	poetry	shell

test:
	poetry	run	pytest

lint:
	poetry	run	isort	app/
	poetry	run	black	app/
	poetry	run	flake8	app/

format:
	poetry	run	isort	app/
	poetry	run	black	app/

update:
	bash	scripts/update.sh