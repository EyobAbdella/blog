FROM nginx:alpine

COPY ./entrypoint.sh ./entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN touch /etc/nginx/conf.d/default.conf

COPY ./proxy_params /etc/nginx/
COPY ./default.conf.tpl /etc/nginx/

ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]