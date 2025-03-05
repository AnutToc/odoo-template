# Specify the Odoo version here
FROM odoo:18.0

USER root
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

COPY --chown=odoo ./docker-images/odoo/development/odoo.conf /etc/odoo/
COPY --chown=odoo ./third-party-modules/ /mnt/third-party-modules/
COPY ./fonts/ /usr/share/fonts/truetype/

USER odoo
