FROM ubuntu
MAINTAINER Gaston Pisacco

#this is a bug in the ubuntu distro
RUN sed -i "s/exit 101/exit 0/g" /usr/sbin/policy-rc.d
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
RUN apt-get update && apt-get -y install \
  curl \
  gcc \
  git \
  postgresql \
  postgresql-contrib \
  postgresql-server-dev-all \
  nginx \
  python \
  python-dev \
  python-pip \
  python-virtualenv \
  uwsgi \
  uwsgi-plugin-python

RUN mkdir -p /var/data/hype /var/data/local

VOLUME ['/var/data/hype']

COPY scripts/tasks /var/data/hype/scripts/tasks
COPY etc/ /var/data/hype/etc/
COPY web/bower.json /var/data/local/

# RUN git clone git://github.com/gpisacco/hype_test.git /var/data/hype #redo
# RUN chmod 755 /var/data/hype/scripts/config.sh

EXPOSE 80

RUN find /var/data/hype/ -name '*.sh' -exec chmod +x "{}" \;

RUN /var/data/hype/scripts/tasks/virtualenv.sh
RUN /var/data/hype/scripts/tasks/nodejs.sh
RUN /var/data/hype/scripts/tasks/postgres.sh
RUN /var/data/hype/scripts/tasks/webserver.sh

#CMD ls -la /var/data/hype/
CMD /var/data/hype/scripts/run.sh #> /tmp/cfg.log
