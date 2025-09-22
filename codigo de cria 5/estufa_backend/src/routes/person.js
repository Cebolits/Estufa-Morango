const express = require('express');
const sensorController = require('../controller/PersonController');
const router = express.Router();
router
    .get('/', sensorController.getAllPeople)
    .get('/:id', sensorController.getById)
    .post('/', sensorController.create)
    .patch('/:id', sensorController.updateById)
    .delete('/:id', sensorController.deleteById)
module.exports = router;