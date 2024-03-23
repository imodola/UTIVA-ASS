# THIS IS NODE JS ASSIGNMENT
### DOCKER CONFIG
---
FROM node:14

WORKDIR /usr/src/app

COPY package*.json app.js ./

RUN npm install

EXPOSE 3000

CMD ["node", "app.js"]

# DOCKER NODE JS CODE

### const express = require ('express')
const app = express()

app.get ('/', (req, res) => res.send('THIS IS JS ASSIGNMENT'))

app.listen (3000,() => console.log('server ready'))