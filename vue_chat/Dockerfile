FROM node:10

RUN npm i -g http-server

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 8083
#CMD ["http-server", "dist"]
