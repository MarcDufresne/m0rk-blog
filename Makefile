.PHONY: content full-content

default:
	@echo "make content: Generate content"
	@echo "make full-content: Delete previous content and generate"

content:
	poetry run pelican content

full-content:
	cd docs && ls | grep -v CNAME | xargs rm -rf
	poetry run pelican content
