all: definitions glossary pattern schema tree

definitions: definitions.py

glossary: glossary.py

pattern: pattern.py

schema: schema.py

tree: tree.py

%.py:
	python3 build/$@

clean:
	rm -r output;

.PHONY: all definitions glossary pattern schema tree clean
