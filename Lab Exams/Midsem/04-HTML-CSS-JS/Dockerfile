FROM ubuntu:bionic
LABEL "maintainer"="bodhitree"
LABEL version="1.0"
LABEL description="Regex"
RUN apt-get update \
  && apt-get install -y man-db manpages-posix nano \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
  
RUN apt-get install --reinstall -y locales
# uncomment chosen locale to enable it's generation
RUN sed -i 's/# pl_PL.UTF-8 UTF-8/pl_PL.UTF-8 UTF-8/' /etc/locale.gen
# generate chosen locale
RUN locale-gen pl_PL.UTF-8
# expand the image
RUN yes | unminimize
# set system-wide locale settings
ENV LANG pl_PL.UTF-8
ENV LANGUAGE pl_PL
ENV LC_ALL pl_PL.UTF-8

RUN pip3 install requests==2.22.0 beautifulsoup4==4.11.1 js2py==0.74
RUN mkdir /home/.evaluationScripts /home/labDirectory
RUN echo "cd /home/labDirectory" > /root/.bashrc

ENV INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
ENV LAB_DIRECTORY="/home/labDirectory"
ENV PATH="/home/.evaluationScripts:${PATH}"
