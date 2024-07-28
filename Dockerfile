FROM MohammedRD313/Scorpion:slim-buster
RUN git clone https://github.com/MohammedRD313/Scorpion.git/root/JoKeRUB
WORKDIR /root/JoKeRUB
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN python3 -m pip install --upgrade pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm@8.19.4
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/JoKeRUB/bin:$PATH"
CMD ["python3","-m","JoKeRUB"]
CMD python3 ser.py & python3 -m JoKeRUB
