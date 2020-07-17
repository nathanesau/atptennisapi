# atptennisapi

Flask API to provide read-only access to database.

## API reference

| Endpoint | Description |
| -------- | ----------- |
| /api/v1/players/get | Get the list of players |
| /api/v1/tournaments/get | Get the list of tournaments |
| /api/v1/draws/get | Get the draw for a given tournament |

## Examples

Get players:

```bash
curl -i http://localhost:8080/api/v1/players/get
```

Get tournaments:

```bash
curl -i http://localhost:8080/api/v1/tournaments/get
```

Get draw:

```bash
curl -i http://localhost:8080/api/v1/draws/get?tournament_name=Rotterdam2019
```