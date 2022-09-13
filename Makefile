lint:
	black --config black.toml src/
build:
	docker build -t petrushynskyi/monoboard.api.auth .
publish:
	docker push petrushynskyi/monoboard.api.auth:latest
