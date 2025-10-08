import {service} from "./firebaseConnect.js"
const urlApi=" http://localhost:8080"
service.user = "Estufa-Morango"

const load_data = async () => {
    const data = await service.load();
}
load_data()

let dbdata={

}

const bot1=document.getElementById("bot1")
const bot2=document.getElementById("bot2")
const bot3=document.getElementById("bot3")
const bot4=document.getElementById("bot4")

const tf=document.getElementById("tf")
const td=document.getElementById("td")
const uf=document.getElementById("uf")
const ud=document.getElementById("ud")
const t=document.getElementById("t")
const l=document.getElementById("l")


// ----------------------- EXEMPLO COLOCANDO DADOS NO FIREBASE ----------------------
const pegar= async ()=>{
    const a = await (
        await (
            fetch(urlApi+"/sensores",{
                method: "GET",
                headers: {
                    "Content-Type" : "application/json"
                }
            })
        )
    ).json()

    console.log(a)

    tf.textContent= a.Temperatura_fora +"°C"
    td.textContent= a.Temperatura_dentro+"°C"
    uf.textContent= a.Umidade_solo+"%"
    ud.textContent= a.Umidade+"%"
    t.textContent= a.Tanque+"%"
    l.textContent= a.Luminosidade+"%"
}

const envia=async ()=>{
    let data = {}
    try{
        data=await service.load()
    }
    catch(e){
        console.log("DATA ESTA VAZIO")
    }
   
    data.Acionadores={"bomba":bot1.checked,"comporta":bot2.checked,"cooler":bot3.checked,"luz":bot4.checked}

    service.set(data)
}

bot1.addEventListener("click", envia)
bot2.addEventListener("click", envia)
bot3.addEventListener("click", envia)
bot4.addEventListener("click", envia)

// ----------------------------------------------------------------------------------
setInterval(() => {
    load_data();
    pegar();
}, 1000);