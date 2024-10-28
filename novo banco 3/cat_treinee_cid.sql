DROP TABLE IF EXISTS `cid`;
CREATE TABLE `cid` (
  `cod_cid` varchar(30) NOT NULL,
  `descricao_cid` varchar(700) NOT NULL,
  PRIMARY KEY (`cod_cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `cid` WRITE;

INSERT INTO `cid` VALUES ('A00.0','Cólera devida a Vibrio cholerae 01, biótipo cholerae'),('A00.9','Cólera não especificada'),('A03.8','Shiguelose não especificada'),('A96.0','Febre amarela urbana'),('A98.4','Doença do vírus Ebola');

UNLOCK TABLES;
