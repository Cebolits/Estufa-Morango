const express = require('express');
const sensoresroutes = require('../routes/sensores');


module.exports = function (app) {
    app.use(express.json());
    app.use('/api/sensores', sensoresroutes);
    // app.use('/api/manual', manual);
};