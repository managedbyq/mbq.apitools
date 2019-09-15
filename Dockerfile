ARG IMAGE
FROM $IMAGE
ARG INSTALL_DJANGO=FALSE
WORKDIR /tox
WORKDIR /app
COPY . .
RUN pip install --upgrade pip tox tox-venv tox-travis --requirement requirements-dev.txt
CMD tox -e "$(tox --listenvs-all | grep "$PYTHON_VERSION-" | tr '\n' ',')"
