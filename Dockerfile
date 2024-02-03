# Use the Caddy base image
FROM ubuntu:latest

# Install Python 3 and pip
RUN apt update && apt install -y \
        git \
        cmake \
        python3 \
        python3-pip \
        espeak

# Install the PyTorch pip package
RUN pip3 install \
        torch \
        scipy \
        unidecode \
        phonemizer \ 
        inflect \
        typing \
        flask \
        openai

# Install the Caddy plugins
RUN git clone https://github.com/psiphon/glados-tts.git -b me /opt/glados-tts

# Copy the repository to the container
COPY . /opt/sarcan

RUN mkdir -p /opt/glados-tts/audio
RUN mkdir -p /opt/glados-tts/tmp
RUN mkdir -p /opt/sarcan/audio
RUN mkdir -p /opt/sarcan/tmp

# Set the working directory
WORKDIR /opt/sarcan

RUN echo " \
#!/bin/bash \n\
set -m  \n\
cd /opt/glados-tts \n \
python3 /opt/glados-tts/engine.py & \n\
cd /opt/sarcan \n\
python3 /opt/sarcan/src/main.py & \n\
fg %1 \n\
" > /opt/sarcan/start.sh

RUN chmod +x /opt/sarcan/start.sh

# Expose the port
EXPOSE 5000

# Run the server
CMD ["bash", "/opt/sarcan/start.sh"]