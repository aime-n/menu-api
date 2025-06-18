.PHONY:	run	dev	test	lint	format	update

run:
	poetry	run	uvicorn	app.main:app	--reload

dev:
	poetry	shell

test:
	poetry	run	pytest

lint:
	bash	scripts/lint.sh

format:
	poetry	run	isort	app/
	poetry	run	black	app/

update:
	bash	scripts/update.sh

clean:
	bash	scripts/clean.sh