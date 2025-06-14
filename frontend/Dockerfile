FROM node:20-alpine

WORKDIR /app/frontend


# add . since this file in alredy in ./frontend 
COPY . . 

RUN --mount=type=secret,id=_env,dst=/etc/secrets/.env cat /etc/secrets/.env

# RUN cd ./frontend
RUN npm install
RUN npm run build

# Serve static files using nginx
FROM nginx:alpine
COPY --from=0 /app/frontend/dist /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
