# profile-manager-service
A Python FastAPI Service for password management and language setup

This is a Python based FastAPI service that provides endpoints for user authentication, password management, and language preference modification.

The design decisions of this service have been based on the discussion [here](https://docs.google.com/document/d/1mLHOf_or-cnb1KWkICB5Zk0anKslmjtEpBzc5OEESeY/edit).

### Prerequisites

Project requires python 3.10.8, pyenv, docker, docker-desktop and poetry.

Install `pyenv` tool to manage python version.

#### Install container runtime

```bash
# install docker
brew install docker
brew link docker # optional

# install docker-compose
brew install docker-compose

```

### Running

```bash
# via docker
docker compose up -d
```

The application is accessible at <http://localhost:3000>.

You can also access the API definitons at <http://localhost:3000/docs>

### Create tables

1. Start the containers
```bash
docker-compose up -d
```
2. Exec into the postgres docker container and connect to the database
```bash
docker-compose exec postgres psql -U postgres -d db
```

3.Run the SQL script in [create_table.sql](scripts/create_table.sql) file located in the db folder

### Insert data in the tables

1. Start the containers
```bash
docker-compose up -d
```
2. Exec into the docker container
```bash
docker-compose exec app bash
```
3. Change the working directory to `scripts` directory
```bash
cd scripts
```
4. Run the python command 
```bash
python insert_data.py
```

### Testing

`pytest` will run all unit tests that you specify in your codebase.

As pytest convention, all files matching `test_*.py` will be included.

#### Running tests
```bash
docker-compose exec app bash
poetry run pytest
```

## TODOs
1. Insert the data in the database using the compressed file instead of the uncompressed file 
2. Handle each exception individually during data insertion
3. Test what error you will receive when the input language is anything other than en or de
4. Research the pool size of the database and what will be ideal in our use-case
5. Generate the secure secret key using a cryptographic library or a password manager and also encode it using base64 encoding
6. Research what other fields than customer_id we can use for jwt encoding
7. Research which would be the best library for the password encryption
8. Add rules for the accepted password when creating a new password 
9. Research which is the best algorithm from encoding jwt key
10. Use Enum for the language column in the customer table definition

## Further Improvements
1. Write (more) tests
2. Implement git pre-commit hooks (DONE)
3. Use alembic for database migration (it's not working at present)
4. Set upo CI/CD Pipeline
5. Set up deployment

## Ideas to explore
1. Integrating Github workflows in the repository