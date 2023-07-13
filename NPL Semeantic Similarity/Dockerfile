FROM pypy:latest
WORKDIR /app
COPY . /app
COPY requirements.txt requirements.txt 
RUN pip3 install -r./requirements.txt
CMD python semantic'en_core_web_md'.py 
CMD python semantic'en_core_web_sm'.py
