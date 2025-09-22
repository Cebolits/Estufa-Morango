import { getSensorData } from './apiRequests.js';

document.addEventListener("DOMContentLoaded", async () => {
    const dados = await getSensorData();

    document.querySelector(".sensor-temperatura2").textContent = `${dados.temperaturaInterna ?? 0}°C`;
    document.querySelector(".sensor-umidadesolo").textContent = `${dados.umidadeInterna ?? 0}%`;
    document.querySelector(".sensor-temperatura1").textContent = `${dados.temperaturaExterna ?? 0}°C`;
    document.querySelector(".sensor-umidade").textContent = `${dados.umidadeExterna ?? 0}%`;
    document.querySelector(".sensor-luz").textContent = `${dados.luminosidade ?? 0}%`;
    document.querySelector(".sensor-tanque").textContent = `${dados.tanque ?? 0}%`;


 

});
