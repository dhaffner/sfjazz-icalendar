src/data.json:
	mkdir -vp $(dir $@);
	curl -f "https://www.sfjazz.org/ace-api/events?startDate=2018-06-01&endDate=2019-06-30" > $@;
	\ls -l $@;

all: src/data.json