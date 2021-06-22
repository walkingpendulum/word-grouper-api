# word-grouper-api
Backend for words viewer. Words are grouped by the most descriptive prefix.


## How to test
First if all you should install requirements with `pip install -r requirements.txt -r requirements-test.txt`.

Then just run `pytest -vs tests`

## How to run application
First if all you should install requirements with `pip install -r requirements.txt.

Then just run `python main.py` and application will be ready on http://localhost:8080


## Endpoints
### Get all words
```bash
$ curl localhost:8080/api/v1/words
{}
```

### Add word
```bash
$ curl -XPUT localhost:8080/api/v1/words/this_is_a_word -d '{"folder": "this"}'
$ curl localhost:8080/api/v1/words
{
    "this": [
        "this_is_a_word"
    ]
}
```

### Remove a word
```bash
$ curl -XDELETE localhost:8080/api/v1/words/this_is_a_word
```
