# Use the Caddy base image
FROM ubuntu:latest

# Install Python 3 and pip
RUN apt update && apt install -y \
        git \
        python3 \
        python3-pip \
        espeak

# Copy the repository to the container
COPY . /opt/sarcan

RUN mkdir -p /opt/sarcan/audio
RUN mkdir -p /opt/sarcan/tmp

# Set the working directory
WORKDIR /opt/sarcan

RUN echo " \
#!/bin/bash \n\
set -m  \n\
cd /opt/sarcan \n\
pip3 install -r requirements.txt \n\
python3 /opt/sarcan/app/main.py \n\
" > /opt/sarcan/start.sh

RUN chmod +x /opt/sarcan/start.sh

# Expose the port
EXPOSE 5000

# Run the server
CMD ["bash", "/opt/sarcan/start.sh"]