FROM python:3

RUN git clone https://github.com/AgnidDrage/PracticaFInalCompu1.git

RUN pip install pip

RUN pip install parameterized

WORKDIR /PracticaFInalCompu1/Final-17-12-20-main

CMD ["python3","-m","testtatety"]