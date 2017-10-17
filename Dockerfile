FROM python:3.5
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /apiDamificados
COPY apiDamificados /apiDamificados
COPY script.sh script.sh
CMD sh script.sh
