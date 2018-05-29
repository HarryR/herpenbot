all: data/topics-erowid.txt

data:
	mkdir -p $@

clean:
	rm -f *.pyc

data/topics-erowid.txt: data/erowid.json
	./erowid-extract.py > $@

data/erowid.json: data/erowid.json.gz
	gunzip $<

data/erowid.json.gz:
	wget -O $@ https://github.com/christianbundy/erowid-research-project/raw/master/erowid.json.gz

