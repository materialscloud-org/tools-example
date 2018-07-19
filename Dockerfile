FROM tools-barebone

MAINTAINER Giovanni Pizzi <giovanni.pizzi@epfl.ch>

COPY ./config.yaml /home/app/code/webservice/static/config.yaml
COPY ./user_templates/* /home/app/code/webservice/templates/user_templates/
COPY ./compute/ /home/app/code/webservice/compute/

# Set proper permissions
RUN chown -R app:app $HOME
