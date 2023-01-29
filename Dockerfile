# using a python small basic image
FROM python:3.9.13
# creates a dir for our application
WORKDIR /app
# copy our requirements.txt file and install dependencies
COPY requirements.txt constraints.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt -c constraints.txt
# copy the rest of our application
COPY . .
