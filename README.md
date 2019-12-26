# dash demo website

### deploying with non-root:
- inside app:

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/'
)

- inside nginx/site-enable

    location /demo {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }


- start

gunicorn -w 4 app:server

