# Backend 

## Quickstart 
### Installation 
```sh 
$ mkdir env 
$ py -m venv env 
$ source env/scripts/activate 
$ pip install -r requirements.txt 
```

### Migration Set Up 
```sh 
$ py manage.py db init
$ py manage.py db migrate
$ py manage.py db upgrade 
```

### Running the Application 
```sh
$ py app.py 
```

### Additional Note 
Make sure postgres is installed 

## Database Schema 

### User Model 

```json
{
  "firstName": "STRING",
  "lastName": "STRING",
  "age": "INTEGER",
  "id": "INTEGER"
}
```

## Routes 
