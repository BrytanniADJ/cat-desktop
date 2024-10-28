DROP TABLE IF EXISTS `lesao`;
CREATE TABLE `lesao` (
  `cod_lesao` varchar(30) NOT NULL,
  `descricao_lesao` varchar(700) NOT NULL,
  PRIMARY KEY (`cod_lesao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `lesao` WRITE;
INSERT INTO `lesao` VALUES ('',''),('1','cde ha'),('13','nhzskxd'),('32k','xddfd'),('702010000','Corte, Laceração, ferida contusa, ounctura(ferida aberta)'),('702030000','Luxação'),('702060000','Choque elétrico e eletroplessão(eletrocussão)'),('702080000','Concussão cerebral'),('706050000','Lesões múltiplas'),('g65','bjbsb');

UNLOCK TABLES;
