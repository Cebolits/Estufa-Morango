const apiBaseUrl = "http://localhost:8080/api/";

async function fetchLatestSensorData() {
    try {
        const response = await fetch(`${apiBaseUrl}/sensores`);
        if (!response.ok) {
            throw new Error(`Erro ao buscar dados: ${response.status}`);
        }
        const data = await response.json();
        console.log("Sensor data recebida:", data);
        updateSensorDisplay(data);
    } catch (error) {
        console.error("Erro ao buscar os dados mais recentes:", error);
    }
}

function updateSensorDisplay(data) {
    const sensorDataElements = document.querySelectorAll(".sensor-data");
    if (sensorDataElements.length >= 6) {
        sensorDataElements[0].textContent = `${data.sensor-umidadesolo ?? 0}%`; // Luminosidade
        sensorDataElements[1].textContent = `${data.sensor-temperatura1 ?? 0}°C`; 
        sensorDataElements[2].textContent = `${data.sensor-temperatura2 ?? 0}°C`;      // Temperatura Interna
        sensorDataElements[3].textContent = `${sensor-umidade ?? 0}%`;      // Umidade Interna
        sensorDataElements[4].textContent = `${sensor-luz ?? 0}%`;
        sensorDataElements[5].textContent = `${data.sensor-tanque ?? 0}%`;    
                // Nível do tanque
    } else {
        console.error("Elementos .sensor-data não encontrados ou insuficientes.");
    }
}

// Executa assim que a página carregar
document.addEventListener("DOMContentLoaded", fetchLatestSensorData);
