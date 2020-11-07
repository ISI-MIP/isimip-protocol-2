all: definitions.py glossary.py pattern.py schema.py tree.py

%.py:
	python3 build/$@

clean:
	rm -r output;

.PHONY: clean
