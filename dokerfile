FROM python:3-alpine

RUN apk update
RUN apk add git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-Juan-Martin-Valverde-Blasco.git
WORKDIR /ajedrez-2024-Juan-Martin-Valverde-Blasco
RUN ls
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m main" ] 