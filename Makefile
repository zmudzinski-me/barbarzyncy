PROJECT_NAME=barbarzyncy
BACKEND_CONTAINER_NAME=django
POETRY_VOLUMES=-v $(PWD)/poetry.lock:/opt/pysetup/poetry.lock -v $(PWD)/pyproject.toml:/opt/pysetup/pyproject.toml

build-docker:
	docker build -t $(PROJECT_NAME):build -f docker/Dockerfile --target build .

poetry-add: build-docker
	docker run $(POETRY_VOLUMES) --rm $(PROJECT_NAME):build poetry add -n $(filter-out $@,$(MAKECMDGOALS))

poetry-update: build-docker
	docker run $(POETRY_VOLUMES) --rm $(PROJECT_NAME):build poetry update -n $(filter-out $@,$(MAKECMDGOALS))

poetry-remove: build-docker
	docker run $(POETRY_VOLUMES) --rm $(PROJECT_NAME):build poetry remove -n $(filter-out $@,$(MAKECMDGOALS))

poetry-lock: build-docker
	docker run $(POETRY_VOLUMES) --rm $(PROJECT_NAME):build poetry lock

poetry-show-outdated: build-docker
	docker run $(POETRY_VOLUMES) --rm $(PROJECT_NAME):build poetry show -o -n

manage:
	docker compose run --rm $(BACKEND_CONTAINER_NAME) manage $(filter-out $@,$(MAKECMDGOALS))

lint:
	docker compose run --rm $(BACKEND_CONTAINER_NAME) lint

format:
	docker compose run --rm $(BACKEND_CONTAINER_NAME) fmt

test:
	docker compose run --rm $(BACKEND_CONTAINER_NAME) test

%: #Ignore unknown commands (and extra parameters)
	@:
