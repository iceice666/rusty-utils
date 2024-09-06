.PHONY: lint docs

lint:
	 mypy

docs:
	 lazydocs --overview-file README.md --src-base-url https://github.com/iceice666/rusty-utils/blob/main/ ./rusty_utils