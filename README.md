# Elucidat Technical Task

## Prerequisites
- Firefox
- Python (virtual) environment w/ Pip OR Poetry (I've used python 3.10.11 for this project, but any recentish version should work too)

## How to run

### Install requirements
Using pip:
```bash
pip install -r requirements.txt
```

OR

Using poetry:
```bash
poetry install
poetry shell
```

### Running
```bash
behave
```

## Notes
I failed to find any API testing I could perform in the last 20 minutes I had, perhaps I could have with some more time.
I tracked multiple calls to `api.elucidat.com` throughout navigation of the website, but none of the requests/payloads looked easier to use than a Selenium alternative.

See `bugs_observed.txt` for details of the 3 bugs I found.

I've included both a `requirements.txt` file and poetry files `poetry.lock` & `pyproject.toml` as I don't know what dependency manager is going to be used.

Only tested on firefox because of time constraints, although the errors/bug I've noted are not browser specific.

I would have included screenshots with the descriptions of the bugs in the `bugs_observed.txt` file, but I ran out of time.