all:
	python main.py

vim:
	nvim main.py
git-update:
	git add Makefile README documentation/ main.py maze_parser/
	git commit -m "update commit"
	git push origin main
