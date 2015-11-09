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

RUN mkdir /var/data
RUN git clone git://github.com/gpisacco/hype_test.git /var/data/hype #redo
RUN chmod 755 /var/data/hype/scripts/config.sh

EXPOSE 80

CMD /var/data/hype/scripts/config.sh > /tmp/cfg.log