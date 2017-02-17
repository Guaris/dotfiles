all: doc.pdf ../README.rst

clean:
	rm doc.pdf
	rm ../README.rst
	rm -rf api

doc.pdf: doc.tex
	pdflatex doc.tex

../README.rst:
	pandoc -f latex -t rst doc.tex > ../README.rst

api:
	sphinx-apidoc -F -o api ../
	cd api && PYTHONPATH=../.. make html
