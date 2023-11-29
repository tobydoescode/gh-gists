ARG ARCH=
ARG BUILD_IMAGE_TAG=buster-slim
FROM ${ARCH}debian:${BUILD_IMAGE_TAG} AS build

RUN apt-get update && \
    apt-get install \
      -y \
      --no-install-suggests \
      --no-install-recommends \
      python3-venv gcc libpython3-dev && \
    mkdir /app && \
    python3 -m venv /app/venv && \
    /app/venv/bin/pip install --upgrade pip && \
    addgroup --system --gid 10001 gistapp && \
    adduser --uid 10001 --gid 10001 --disabled-login gistapp

COPY requirements.txt /app/requirements.txt
RUN /app/venv/bin/pip install --disable-pip-version-check -r /app/requirements.txt

COPY main.py /app/main.py

RUN chmod +x /app/main.py

FROM gcr.io/distroless/python3-debian10:nonroot

COPY --from=build /etc/passwd /etc/passwd
COPY --from=build /etc/group /etc/group
COPY --from=build /app /app

USER gistapp

ENV PATH="/app/venv/bin:$PATH"

ENTRYPOINT ["python", "/app/main.py"]
