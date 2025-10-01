const { Sequelize } = require('sequelize');
const database = require("../config/db.js")

const sensores = database.define("sensores_tb", {

    sensores_id : {
        type: Sequelize.INTEGER,
        allowNull: false,
        autoIncrement: true,
        primaryKey: true
    },
    Temperatura_fora : {
        type: Sequelize.INTEGER,
        allowNull: false

    },
    Temperatura_dentro : {
        type: Sequelize.INTEGER,
        allowNull: false

    },
        Umidade_solo : {
        type: Sequelize.INTEGER,
        allowNull: false

    },
        Umidade : {
        type: Sequelize.INTEGER,
        allowNull: false

    },
        Tanque: {
        type: Sequelize.INTEGER,
        allowNull: false

    },
      Luminosidade: {
        type: Sequelize.INTEGER,
        allowNull: false

    },
})

module.exports = sensores;
