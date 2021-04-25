FROM python:3.8-alpine

ENV MYHOME=/grainchain2
RUN mkdir ${MYHOME}

WORKDIR ${MYHOME}
COPY ./ ${MYHOME}

RUN pip install --user -r requirements.txt

ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["app.py"]