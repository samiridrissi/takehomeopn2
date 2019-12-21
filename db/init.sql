CREATE DATABASE credentials;
USE credentials; 
CREATE TABLE credentialstable (
    PersonID int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    FirstName varchar(50) NOT NULL,
    LastName varchar(50) NOT NULL
);
