.DEFAULT_GOAL = slides.html

slides.html: code-slides/*.py
	python build-slides.py code-slides/[0-9]*.py
