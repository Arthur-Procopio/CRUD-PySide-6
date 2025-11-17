CREATE DATABASE crud_empresas;
USE crud_empresas;

CREATE TABLE empresas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    cnpj VARCHAR(20),
    endereco TEXT
);

CREATE TABLE funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    cargo VARCHAR(255),
    salario DECIMAL(10,2),
    empresa_id INT,
    FOREIGN KEY (empresa_id) REFERENCES empresas(id)
);