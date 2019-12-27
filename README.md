# dash demo website

### deploying with non-root:
- inside app:

app = dash.Dash(
    /_/_name/_/_,
    server=server,
    routes_pathname_prefix='/dash/'
)

- inside nginx/site-enable

    location /demo {
        proxy_pass http://localhost:8050;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }


- start

> gunicorn -w 4 app:server

the upper does not needed - just start index.py.

DO NOT forget:
- set host='0.0.0.0' in app.run_server() option.
- set routes_pathname_prefix='XXX' in the app.py, where XXX is the web root
your page will be mounter, i.e. '/demo/' if it'll routed as http://your_site/demo
