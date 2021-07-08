# HTTPS reverse proxy with certificate creation and renewal

Edit the file `nginx/nginx-https.conf` according to your needs.

You need to set the following gitlab variables (Settings -> CI/CD -> Variables):
- `SSH_PRIVATE_KEY`
- `DEPLOY_USER`
- `DEPLOY_HOST`
- `DEPLOY_DIR`: directory where the docker compose file will be copied
- `DEPLOY_VOLUMES_DIR`: base directory containing all docker volumes
- `DOMAIN`