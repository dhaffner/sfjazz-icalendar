.PHONY: clean all
OUTPUT=sfjazz.ics

all: $(OUTPUT)

$(OUTPUT): venv
	curl -f "https://www.sfjazz.org/ace-api/events?startDate=$(shell date "+%F")&endDate=$(shell date --date="next year" "+%F")" 2>/dev/null \
		| $</bin/python sfjazz.py \
		> $@;
	ls -l $@;

venv:
	python3 -mvenv $@;
	$@/bin/pip install ics;

clean:
	rm -fv $(OUTPUT);