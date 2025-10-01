const express = require('express')
const routes = express.Router()


const sensores = require('./controllers/sensores.js')
routes.post('/sensores', sensores.criar)

routes.get('/sensores', sensores.pega)


module.exports = routes
