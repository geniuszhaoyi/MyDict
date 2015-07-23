all:
	latex model.tex
	latex model.tex
	#bibtex model
	latex model.tex
	dvipdf model.dvi
	
clean:
	rm *.dvi *.log *.aux *.blg *.bbl
