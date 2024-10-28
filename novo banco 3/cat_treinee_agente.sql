DROP TABLE IF EXISTS `agente`;
CREATE TABLE `agente` (
  `cod_agente` varchar(30) NOT NULL,
  `nome_agente` varchar(200) NOT NULL,
  `descricao_agente` varchar(700) NOT NULL,
  PRIMARY KEY (`cod_agente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `agente` WRITE;
INSERT INTO `agente` VALUES ('','',''),('1','dd','dfe'),('30.20.70.100','Escavação','Para edifício, estrada, etc'),('30.30.15.100','Talhadeira','Ferramenta portátil com força motriz ou aquecimento'),('30.30.20.040','Serra','Máquina'),('30.30.50.200','Caldeira','Sem descrição');
UNLOCK TABLES;