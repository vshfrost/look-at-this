FROM nginx:alpine

COPY env/nginx/default.conf.template /etc/nginx/conf.d/default.conf.template
COPY env/nginx/start.sh /nginx-start.sh

RUN chmod +x /nginx-start.sh

ENTRYPOINT ["/nginx-start.sh"]
