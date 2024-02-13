server {

    listen 80;

    location /static {
        alias /staticfiles;
    }

    location / {
        proxy_pass      http://app:8000;
        include         /etc/nginx/proxy_params;
    }

}