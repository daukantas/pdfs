install:
	python bootstrap.py
	bin/buildout

run:
	bin/django runserver

static:
	bin/django collectstatic --noinput

sync:
	rm var/db
	touch var/db
	chmod 777 var/db
	bin/django syncdb
