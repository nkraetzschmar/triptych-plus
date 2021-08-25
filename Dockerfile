FROM ubuntu:latest
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -qy install make texlive-full biber python3-matplotlib
WORKDIR /data
