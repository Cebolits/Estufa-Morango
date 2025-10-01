const sensores = require('../models/sensores.js')

module.exports = {

    async criar(req,res)
    {
        const data=req.body
        // var vaiselascar = await sensores.findAll(
        //     {
        //         where : {
        //             authorId: 2,
        //         }    
        //     }
        // )

        var newsensor = await sensores.create({
            "Temperatura_fora" : data.temperaturaf,
            "Temperatura_dentro" :data.temperaturad,
            "Umidade_solo" : data.umidades,
            "Umidade" : data.umidade,
            "Tanque" : data.tanque,
            "Luminosidade" : data.luminosidade
        })

        res.status(200).json({ message: "Success!" });
    },

    async pega(req, res) {
    try {
        const ultimoSensor = await sensores.findOne({
            order: [['sensores_id', 'DESC']]
        });

        res.status(200).json(ultimoSensor);
    } catch (error) {
        console.error("Erro ao buscar o último sensor:", error);
        res.status(500).json({ message: "Erro ao buscar o último registro dos sensores." });
    }
}

    

}