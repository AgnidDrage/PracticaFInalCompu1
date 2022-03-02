FROM python:3

RUN git clone https://github.com/AgnidDrage/PracticaFInalCompu1.git

RUN pip install pip

RUN pip install parameterized

RUN python3 -m Final-17-12-20-main.unittest

CMD ["python3","-m","Final-20-05-21-main.unittest"]