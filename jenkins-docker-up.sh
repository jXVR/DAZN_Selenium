#!/bin/bash

dind_name="$1"
if [[ -z "$dind_name" ]]
then
  dind_name='jenkins-docker'
fi

jenkins_vol_name="$2"
if [[ -z "$jenkins_vol_name" ]]
then
  jenkins_vol_name='jenkins-data'
fi

jenkins_image_name="$3"
if [[ -z "$jenkins_image_name" ]]
then
  jenkins_image_name='myjenkins-blueocean'
fi

jenkins_docker_name="$4"
if [[ -z "$jenkins_docker_name" ]]
then
  jenkins_docker_name='myjenkins-blueocean'
fi

jenkins_blueocean_port="$5"
if [[ -z "$jenkins_blueocean_port" ]]
then
  jenkins_blueocean_port=8084
fi

docker network create jenkins

docker run \
  --name $dind_name \
  --restart=unless-stopped \
  --detach \
  --privileged \
  --network jenkins \
  --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume $dind_name-certs:/certs/client \
  --volume $jenkins_vol_name:/var/jenkins_home \
  --publish 2376:2376 \
  docker:dind --storage-driver overlay2

docker build \
  --tag $jenkins_image_name:2.332.3-1 \
  --file JenkinsDockerfile .

docker run \
  --name $jenkins_docker_name \
  --restart=unless-stopped \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish $jenkins_blueocean_port:8080 \
  --publish 50000:50000 \
  --volume $jenkins_vol_name:/var/jenkins_home \
  --volume $dind_name-certs:/certs/client:ro \
  $jenkins_image_name:2.332.3-1

echo "Visiting http://localhost:$jenkins_blueocean_port"
open http://localhost:$jenkins_blueocean_port

echo "When you will see Jenkins Unlock Jenkins Page ready, run:"
echo "docker exec $jenkins_docker_name cat /var/jenkins_home/secrets/initialAdminPassword | pbcopy"
echo "It will copy password for you :)"
