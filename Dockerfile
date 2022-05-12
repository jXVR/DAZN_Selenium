FROM ubuntu:20.04

# Update & upgrade & install needed packages
RUN DEBIAN_FRONTEND=noninteractive \
  apt-get -qy update && \
  apt-get -qy upgrade && \
  apt-get -qy install \
    wget \
    curl \
    unzip \
    python3 \
    python3-pip

# Prepare Google Chrome and chromedriver
# Download Google Chrome
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# Install stable Gogole Chrome
RUN DEBIAN_FRONTEND=noninteractive \
  apt-get -qy install ./google-chrome-stable_current_amd64.deb
# Download compatible chromedriver
RUN curl https://chromedriver.storage.googleapis.com/100.0.4896.60/chromedriver_linux64.zip -o chromedriver.zip
# Unzip chromedriver
RUN unzip chromedriver.zip
# Copy chromedriver to any dir added to $PATH, this path is pointed in DriverCreator inside out tests
RUN cp chromedriver /usr/local/bin

# Prepare user
RUN useradd -u 1000 jenkinsuser
RUN mkdir /home/jenkinsuser
RUN chown 1000:1000 /home/jenkinsuser

# Add and install python3 requirements
COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt

# Use the user
USER jenkinsuser
