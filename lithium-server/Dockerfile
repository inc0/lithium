FROM python:3
WORKDIR /usr/src/app
RUN pip install Flask jinja2
COPY . .
CMD python server.py --image="${LITHIUM_IMAGE}" --pubkey="${LITHIUM_PUBKEY}" --host-ip="${LITHIUM_HOST}"
