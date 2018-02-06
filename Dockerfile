#
# Docker Image with Mythril and Solc for CI/CD of Ethereum Solidity Codes
#

# Pull base image
FROM python:3.5.4

# Install Mythril
RUN \
  pip install mythril
  
# Install Solidity compiler
RUN \
  add-apt-repository ppa:ethereum/ethereum && \
  apt-get update && \
  apt-get -y install solc
 
COPY origin.sol ~/origin.sol

RUN myth -x origin.sol
