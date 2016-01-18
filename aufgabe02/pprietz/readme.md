lkiesow
-------

*Mon Jan 18 01:26:20 CET 2016*

 - Flake8 complains a lot. I know sometimes one has different preferences, but
	if a language has a general coding guide, it usually makes sense to stick
	with that. Have a look at PEP8.
 - Put the code in a function and use `if __name__ == '__main__':` to make sure
	it is not executed if it is imported by another module.
 - You printed neither the pull request's title nor the commit mesage but the
	pull requests description. But you wrapped that nicely ;-P
 - Would be nice to have the token optional
