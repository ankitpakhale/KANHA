#!/bin/bash

# run the command to register models
echo "Registering Models..."
python -m src.dao.init.register_models

echo ""
echo ""

echo "Migrating Models..."
# run the migration handler command
python -m src.dao.migrations.migration_handler
