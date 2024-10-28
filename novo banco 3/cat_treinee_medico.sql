DROP TABLE IF EXISTS `medico`;
CREATE TABLE `medico` (
  `cod_medico` int NOT NULL,
  `nome_medico` varchar(40) NOT NULL,
  `cpf_medico` varchar(15) NOT NULL,
  `email_medico` varchar(40) NOT NULL,
  `especialidade_medico` varchar(40) NOT NULL,
  `crm_medico` varchar(6) NOT NULL,
  PRIMARY KEY (`cod_medico`),
  UNIQUE KEY `cod_medico` (`cod_medico`),
  UNIQUE KEY `crm_medico` (`crm_medico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `medico` WRITE;
INSERT INTO `medico` VALUES (1,'maria Clara','111.111.111-11','clara@gmail','clinico geral','11111'),(2,'sdf','416.354.156-46','hygyhug','fgyhug','jhju');

UNLOCK TABLES;