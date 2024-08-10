FROM silverlogic/python3.8

RUN curl -fssL https://deb.nodesource.com/setup_18.x | sudo -E bash && sudo apt install nodejs -y
RUN apt install ffmpeg -y
COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD bash start
