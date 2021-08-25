.PHONY: all clean

all: build/paper.pdf

clean:
	rm -rf build

build:
	mkdir -p build

build/paper.pdf: preamble.tex build/linkable.pyplot.pdf build/accountable.pyplot.pdf

build/%.pdf: %.tex bibliography.bib | build
	@printf "[ %-8s ]: %-32s ---> %-32s\n" "latexmk" "$<" "$@"
	@latexmk -g -halt-on-error -pdf -output-directory=build "$<" > build/stdout.log 2>&1 || (cat build/stdout.log && false)

build/%.pyplot.pdf: plot.py
	@printf "[ %-8s ]\n" "plot.py"
	@python3 $< > build/stdout.log 2>&1 || (cat build/stdout.log && false)
