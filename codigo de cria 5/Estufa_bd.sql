CREATE DATABASE funcionalidades;
USE funcionalidades;
DROP DATABASE pessoas;

drop table sensores;
CREATE TABLE sensores(
id int not null auto_increment primary key,
datas date not null, 
temperaturaExterna decimal(5,2) not null,
temperaturaInterna decimal(5,2) not null,
luminosidade decimal(5,2) not null,
umidadeInterna decimal(5,2) not null,
umidadeExterna decimal(5,2) not null,
tanque decimal(5,2) not null

);
USE funcionalidades;

select * from persons


