#/bin/bash
rm -rf ./database/database.db
source env/bin/activate
flask --app main run --debug