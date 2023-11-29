FROM jenkins/jenkins:jdk17

USER root
RUN apt update && curl -fsSL https://get.docker.com | sh && \
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

RUN usermod -aG docker jenkins
