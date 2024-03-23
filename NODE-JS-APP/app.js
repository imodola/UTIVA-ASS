const express = require ('express')
const app = express()

app.get ('/', (req, res) => res.send('THIS IS JS ASSIGNMENT'))
app.listen (3000,() => console.log('server ready'))