ARG IMAGE
FROM $IMAGE

ARG LOCAL_SERVICE=FALSE

WORKDIR /tox
WORKDIR /app

COPY . .

RUN pip install --upgrade pip tox --requirement requirements-dev.txt

RUN [ "$LOCAL_SERVICE" = "TRUE" ] && \
    pip install django && \
    python -m manage collectstatic --noinput && \
    apt-get update && \
    exit 0

CMD tox -e "$(tox --listenvs-all | grep "$PYTHON_VERSION-" | tr '\n' ',')"
