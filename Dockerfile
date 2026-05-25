# using slim to keep the image small — don't need the full Debian image
FROM python:3.12-slim

# set workdir so all paths inside the container are relative to /app
WORKDIR /app

# copy requirements first so Docker can cache this layer
# if I change my Python code but not requirements, it won't reinstall everything
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# now copy the actual source code
COPY src/ ./src/

# this is the script GitHub runs when the action triggers
ENTRYPOINT ["python", "/app/src/main.py"]
