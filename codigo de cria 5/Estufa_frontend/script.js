import {service} from "./firebaseConnect.js"
const url=" http://localhost:8080"
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


// ----------------------- EXEMPLO COLOCANDO DADOS NO FIREBASE ----------------------
const pegar=()=>{
    fetch("") 

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

}, 10000);