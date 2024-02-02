# lexicom_task_solution

## Task #1

### Requirements

1. [docker](https://www.docker.com)

### Build image

```shell
docker compose build
```

### Up containers

```shell
docker compose up
```

## Task #2

### Solution #1: Using `substring`

```SQL
UPDATE full_names
SET status = (
    SELECT s.status
    FROM short_names s
    WHERE s.name = substring(full_names.name FROM 1 FOR position('.' IN full_names.name) - 1)
)
WHERE EXISTS (
    SELECT 1
    FROM short_names s
    WHERE s.name = substring(full_names.name FROM 1 FOR position('.' IN full_names.name) - 1)
);
```

### Solution #2: Using `JOIN`

```SQL
UPDATE full_names
SET status = s.status
FROM short_names s
WHERE s.name = substring(full_names.name FROM 1 FOR position('.' IN full_names.name) - 1);
```
