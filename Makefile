all: definitions.py glossary.py pattern.py schema.py

%.py:
	python3 build/$@

clean:
	rm -r output;

.PHONY: clean
