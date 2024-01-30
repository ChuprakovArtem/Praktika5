FROM ubuntu
COPY . prog

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
xpra \
xterm \
net-tools \
nano 

RUN apt-get update
RUN apt-get update && apt-get install -qqy x11-apps
RUN apt update && apt install -y \
    nano \
    python3 \
    python3-pip

RUN pip install\ 
    pygame \
    numpy \
    pillow


ENV DISPLAY=host.docker.internal:0.0

WORKDIR "/prog"

CMD ["python3 gglit.py"]
