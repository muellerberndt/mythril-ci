#
# Docker Image with Mythril and Solc for CI/CD of Ethereum Solidity Codes
#

# Pull base image
FROM ubuntu:16.04

# Install Python && Necessary build tools
RUN \
  apt-get update && \
  apt-get install -y build-essential software-properties-common libssl-dev && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*
  
# Install Mythril
RUN \
  pip install mythril
  
# Install Solidity compiler
RUN \
  add-apt-repository ppa:ethereum/ethereum && \
  apt-get update && \
  apt-get -y install solc
