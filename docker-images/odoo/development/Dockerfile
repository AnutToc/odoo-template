FROM odoo:17

USER root
RUN pip3 install -U pip
RUN pip3 install bahttext xlwt num2words xlsxwriter xlrd

COPY --chown=odoo ./docker-images/odoo/development/odoo.conf /etc/odoo/
COPY --chown=odoo ./third-party-modules/ /mnt/third-party-modules/
COPY ./fonts/ /usr/share/fonts/truetype/

USER odoo
