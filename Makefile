type-check:
	mypy .


test:
	pytest .

clean:
	rm -rf .mypy_cache