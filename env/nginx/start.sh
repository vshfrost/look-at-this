#!/bin/sh

# Replace env vars in the nginx config template
envsubst '$APP_PORT $NGINX_PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

# Start nginx in foreground
nginx -g 'daemon off;'