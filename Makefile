DC := docker-compose
APP := app
ALEMBIC := alembic -c database/tools/alembic/alembic.ini

.PHONY: bash env-start env-stop env-recreate env-dev env-test migration migrate migrate-down migrate-history migrate-current

# Run containers
env-start: env-dev
	$(DC) up -d

# Remove containers + volumes
env-stop:
	$(DC) down -v

# Recreate containers
env-recreate: env-dev env-stop
	@$(DC) build --no-cache
	@$(DC) up -d > /dev/null 2>&1

# Copy .env variables for development
env-dev:
	cp env/vars/.env.local .env

# Copy .env variables for testing
env-test:
	cp env/vars/.env.test .env

# Connect to app container
bash:
	@$(DC) exec $(APP) bash

# Create a new migration, prompting for a migration name
migration:
	@read -p "Enter migration name (optional): " name; \
	if [ -z "$$name" ]; then \
		name=""; \
	fi; \
	$(DC) exec $(APP) $(ALEMBIC) revision --autogenerate -m "$$name"

# Apply migrations
migrate:
	$(DC) exec $(APP) $(ALEMBIC) upgrade head

# Downgrade one revision
migrate-down:
	$(DC) exec $(APP) $(ALEMBIC) downgrade -1

# Show migration history
migrate-history:
	$(DC) exec $(APP) $(ALEMBIC) history

# Show current revision
migrate-current:
	$(DC) exec $(APP) $(ALEMBIC) current
