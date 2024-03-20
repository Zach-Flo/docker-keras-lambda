FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install --upgrade pip

RUN pip install tensorflow==2.14.0

RUN pip install -r requirements.txt

COPY src/main.py ${LAMBDA_TASK_ROOT}

COPY src/saved_model/ ${LAMBDA_TASK_ROOT}/saved_model/

CMD [ "main.handler" ]