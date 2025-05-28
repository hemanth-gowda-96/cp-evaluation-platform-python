# Project Portal in python (collage Project)

## set up virtual environment

```
$ python3 -m venv env

$ souce env/bin/activate
```

## install dependencies

```
(env) $ pip install -r requirements.txt
```

## run development environment

```
flask --app app run --debug
```

## Open App in

[Click here : http://localhost:5000](http://localhost:5000)

## flaks db migration command

```
flask db init        # Initialize migrations folder
flask db migrate -m "Initial migration"  # Create migration script
flask db upgrade    # Apply migration (creates database.db)
```
