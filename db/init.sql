CREATE DATABASE credentials;
USE credentials; 
CREATE TABLE credentialstable (
    PersonID int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Firstname varchar(50) NOT NULL,
    Lastname varchar(50) NOT NULL
);
