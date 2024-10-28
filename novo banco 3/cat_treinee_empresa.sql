DROP TABLE IF EXISTS `empresa`;
CREATE TABLE `empresa` (
  `cod_empresa` int NOT NULL,
  `nome_empresa` varchar(20) NOT NULL,
  `tipo_num_doc_empresa` varchar(14) NOT NULL,
  `cnpj_empresa` varchar(20) NOT NULL,
  `cnae_empresa` varchar(12) NOT NULL,
  `cep_empresa` varchar(12) NOT NULL,
  `endereco_empresa` varchar(30) DEFAULT NULL,
  `bairro_empresa` varchar(30) DEFAULT NULL,
  `municipio_empresa` varchar(40) DEFAULT NULL,
  `estado_empresa` varchar(25) DEFAULT NULL,
  `telefone_empresa` varchar(20) NOT NULL,
  `email_empresa` varchar(40) NOT NULL,
  PRIMARY KEY (`cod_empresa`),
  UNIQUE KEY `cnpj_empresa` (`cnpj_empresa`),
  UNIQUE KEY `cod_empresa` (`cod_empresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `empresa` WRITE;
INSERT INTO `empresa` VALUES (1,'link 7','14641564-16','10.242.536/4487-99','5416-4/15','56415-46','uhnju','ujhu','ujhu','CE','(69)59645-6464','hniuju');

UNLOCK TABLES;