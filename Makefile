.PHONY:	run	dev	test	lint	format	clean	pre-commit	seed	update

run:
	poetry	run	uvicorn	app.main:app	--reload

test:
	poetry	run	pytest

lint:
	bash	scripts/lint.sh

format:
	bash	scripts/format.sh

clean:
	bash	scripts/clean.sh

pre-commit:
	bash	scripts/pre-commit.sh

seed:
	poetry	run	python	scripts/seed_data.py

update_db:
	bash	scripts/update_db.sh

done:
	bash	scripts/done.sh
