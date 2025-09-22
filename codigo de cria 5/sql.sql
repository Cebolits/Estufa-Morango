CREATE DATABASE funcionalidades;
USE funcionalidades;

DROP TABLE IF EXISTS sensores;
CREATE TABLE sensores(
    datas DATE NOT NULL, 
    temperaturaExterna DECIMAL(5,2) NOT NULL,
    temperaturaInterna DECIMAL(5,2) NOT NULL,
    luminosidade DECIMAL(5,2) NOT NULL,
    umidadeInterna DECIMAL(5,2) NOT NULL,
    umidadeExterna DECIMAL(5,2) NOT NULL,
    tanque DECIMAL(5,2) NOT NULL,
    comporta BOOL NOT NULL,
    bomba BOOL NOT NULL,
    cooler BOOL NOT NULL
);


SELECT * FROM sensores;

DROP user IF EXISTS 'operador'@'localhost';
CREATE USER 'operador'@'localhost' IDENTIFIED BY 'op';

CREATE VIEW sensores_operador AS
SELECT 
    temperaturaExterna,
    temperaturaInterna,
    luminosidade,
    umidadeInterna,
    umidadeExterna
FROM sensores;


GRANT SELECT ON funcionalidades.sensores_operador TO 'operador'@'localhost';

INSERT INTO sensores (
    datas, temperaturaExterna, temperaturaInterna, luminosidade, 
    umidadeInterna, umidadeExterna, tanque, comporta, bomba, cooler
) VALUES
('2025-06-21', 32.50, 27.30, 450.00, 60.00, 55.00, 80.00, TRUE, FALSE, FALSE),
('2025-06-22', 31.10, 26.50, 470.00, 58.00, 52.50, 75.00, FALSE, TRUE, FALSE),
('2025-06-23', 33.00, 28.20, 490.00, 56.00, 50.80, 70.00, TRUE, TRUE, TRUE),
('2025-06-24', 29.80, 25.10, 420.00, 65.00, 60.00, 85.00, FALSE, FALSE, TRUE),
('2025-06-25', 34.20, 29.00, 500.00, 55.00, 49.00, 65.00, TRUE, FALSE, TRUE);

SELECT * FROM sensores;
