FROM ubuntu
COPY . docker-prakt

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
nano 

WORKDIR "/docker-prakt"

CMD ["bash"]

