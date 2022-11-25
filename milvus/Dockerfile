FROM registry.baidubce.com/paddlepaddle/paddle:2.2.2
LABEL maintainer="paddlesl@baidu.com"

RUN apt-get update 
RUN apt-get install -y libsndfile-dev 
RUN apt-get clean 
RUN rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 https://github.com/PaddlePaddle/PaddleSpeech.git /home/PaddleSpeech  
RUN pip3 uninstall mccabe -y ; exit 0;
RUN pip3 install multiprocess==0.70.12 importlib-metadata==4.2.0 dill==0.3.4

WORKDIR /home/PaddleSpeech/
RUN python setup.py bdist_wheel
RUN pip install dist/*.whl 

# For the audio-search example
ADD example_audio .
ADD src .
ADD requirements.txt .
RUN pip install -r requirements.txt

######
# `docker build -t paddlespeech .`
# `docker run -it -rm paddlespeech`
# then run `python ./src/audio_search.py` in the docker terminal
# then open another terminal to this docker (e.g., docker run ...)
# and run `python ./src/test_audio_search.py` to see results.

CMD ['/bin/bash']
