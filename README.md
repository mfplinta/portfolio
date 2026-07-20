# Portfolio

Django portfolio packaged as a multi-architecture OCI image for deployment.
The image runs unprivileged with a read-only root filesystem. SQLite and
uploaded media are the only persistent state and live under `/app/data`.

## Local container

```sh
docker compose up --build
```

Open <http://localhost:8000>

## Publishing

Pushes to `main` build `linux/amd64` and `linux/arm64` images and publish
`ghcr.io/mfplinta/portfolio:latest`.
