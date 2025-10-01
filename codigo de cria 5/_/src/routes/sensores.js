const express = require('express');
const SensorController = require('../controller/SensorController');
const router = express.Router();


   // Rota para criar novos dados de sensores
router.post('/', SensorController.create); // post -> enviar dados para api -> body -> { "nome": "Nicolas", "sobrenome": "Marques"}

// Rota para obter todos os dados de sensores
router.get('/', SensorController.getAll); //get comum -> buscar dados por meio deste endpoint

// Rota para obter os dados mais recentes dos sensores
router.post('/teste', SensorController.sensorTest); 

// Rota para deletar dados de sensores por ID
router.delete('/:id', SensorController.deleteById); //get com params -> é quando o get possui "/:params"


module.exports = router;