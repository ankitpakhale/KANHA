# define the environment variable from .env or default to 'dev'
ENV := $(shell grep -oP '^ENV=\K.*' .env || echo dev)

# define paths based on ENV
DOCKER_COMPOSE_PATH = infra/$(ENV)/docker-compose.yml
DOCKER_IMAGE = dev_kanha-backend
DOCKER_CONTAINER = kanha_container
DOCKERFILE = infra/$(ENV)/Dockerfile  # Updated this line to reflect correct Dockerfile path
APP_PORT = 7010

ifeq ($(ENV),dev)
  $(info running in dev environment)
endif
ifeq ($(ENV),qa)
  $(info running in qa environment)
endif
ifeq ($(ENV),stage)
  $(info running in stage environment)
endif
ifeq ($(ENV),prod)
  $(info running in prod environment)
endif

# default target: build the docker image
build:
	@echo "building docker image..."
	docker build -t $(DOCKER_IMAGE) -f $(DOCKERFILE) .

# start the application using docker compose
start:
	@echo "starting the application with docker compose..."
	docker-compose -f $(DOCKER_COMPOSE_PATH) up --build

# stop and remove running container
stop:
	@echo "stopping and removing docker container..."
	docker-compose -f $(DOCKER_COMPOSE_PATH) down

# clean the docker environment (images, containers, volumes)
clean:
	@echo "cleaning up docker images, containers, and volumes..."
	docker system prune -f

# rebuild docker image and start the application
rebuild: clean build start

# show docker container logs
logs:
	@echo "showing docker container logs..."
	docker logs -f $(DOCKER_CONTAINER)

# access the docker container shell
bash:
	@echo "accessing the docker container shell..."
	docker exec -it $(DOCKER_CONTAINER) bash

# run the application manually without compose (e.g., entrypoint.sh)
run:
	@echo "running the application manually from entrypoint.sh..."
	docker run -p $(APP_PORT):$(APP_PORT) $(DOCKER_IMAGE)
