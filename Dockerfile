# tensorflow base-image
FROM tensorflow/tensorflow:2.10.0
# apple silicon >
# FROM armswdev/tensorflow-arm-neoverse:r22.09-tf-2.10.0-eigen

WORKDIR /prod

# need to strip the requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY yogi yogi
RUN pip install .

COPY Makefile Makefile
RUN make reset_local_files

CMD uvicorn ## xxxxxxxx
