FROM python

MAINTAINER salexkidd <salexkidd@gmail.com>

expose 8085

RUN git clone https://github.com/salexkidd/restframework-definable-serializer-example.git

WORKDIR /restframework-definable-serializer-example

RUN pip install -r ./requirements.txt --upgrade
RUN ./manage.py migrate
RUN ./manage.py loaddata ./fixtures/*

ENTRYPOINT ["./manage.py", "runserver", "0.0.0.0:8085"]
