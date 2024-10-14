CREATE DATABASE BdHornoFundicionDental; 
use Bdhornofundiciondental;
create table Hornos
(
NumeroSerie int primary key not null,
Marca varchar (25) not null,
Modelo varchar (25) not null,
Capacidad varchar (25) not null,
Peso varchar (30) not null,
Potencia varchar(50) not null,
Temperatura_Maxima int not null
);
INSERT INTO Hornos VALUES
("20756", "Indef", "134D", "1,5L", "18Kg", "1,7Kw", "1250"),
("50678", "Tecnodent", "H21E", "2L", "20Kg", "1,8Kw", "1150"),
("80956", "Denstar", "V23", "1,3L", "15Kg","1,5Kw", "1150"),
("70908", "Dentsply", "Qex01", "1,7L", "16Kg", "1,7Kw", "1250"),
("30098", "Indef", "135f", "1,5L", "18Kg", "1,8Kw", "1200"),
("20456", "Dentsply", "Quex03", "1,3L", "13Kg", "1,5Kw", "1150"),
("70987", "Tecnodent", "H234", "2L", "18Kg", "1,8Kw", "1250"),
("30678", "Tecnodent", "Hx534", "1,3L", "15Kg", "1,5Kw", "1200"),
("50789", "Dentsply", "Hvx57", "1,5L", "18Kg", "1,7Kw", "1250"),
("06243", "Denstar", "X567", "2L", "20Kg", "1,8Kw", "1300");
SELECT * FROM Hornos;
SELECT Capacidad, Potencia FROM Hornos;
SELECT * FROM Hornos Where Peso= "20Kg";
SELECT * FROM Hornos where Temperatura_Maxima<1200;
SELECT*FROM Hornos Where Marca=  "Tecnodent";