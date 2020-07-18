# atptennisapi

Flask API to provide read-only access to database.

## API reference

| Endpoint | Description |
| -------- | ----------- |
| /api/v1/players/get | Get the list of players |
| /api/v1/tournaments/get | Get the list of tournaments |
| /api/v1/draws/get | Get the draw for a given tournament |

## Examples

```bash
# get players
curl -i http://localhost:8080/api/v1/players/get

# get tournaments
curl -i http://localhost:8080/api/v1/tournaments/get

# get draw
curl -i http://localhost:8080/api/v1/draws/get?tournament_name=Rotterdam2019
```

## Database Info

The database has the following schema:

![](https://raw.githubusercontent.com/nathanesau/fantasytennis/master/assets/images/atptennisschema.PNG)

Here is a script which creates this schema:

https://github.com/nathanesau/fantasytennis/blob/master/database/atptennisschema.sql

## Unit Tests

To run the unit tests use:

```bash
python3 -m unittest
```
