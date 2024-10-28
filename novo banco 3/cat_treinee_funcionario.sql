DROP TABLE IF EXISTS `funcionario`;
CREATE TABLE `funcionario` (
  `cod_funcionario` int NOT NULL,
  `cod_empresa` int DEFAULT NULL,
  `nome_func` varchar(40) NOT NULL,
  `nome_mae_func` varchar(40) DEFAULT NULL,
  `data_nascimento_func` date NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `estado_civil` varchar(20) NOT NULL,
  `remuneracao_func` varchar(20) NOT NULL,
  `ctps_func` varchar(30) NOT NULL,
  `identidade_func` varchar(15) NOT NULL,
  `pis_pasep_nit_func` varchar(20) DEFAULT NULL,
  `cep_func` varchar(15) NOT NULL,
  `endereco_func` varchar(40) DEFAULT NULL,
  `bairro_func` varchar(30) DEFAULT NULL,
  `estado_func` varchar(25) DEFAULT NULL,
  `municipio_func` varchar(40) DEFAULT NULL,
  `telefone_func` varchar(20) NOT NULL,
  `cbo_func` varchar(10) NOT NULL,
  `aposentadoria_func` varchar(15) DEFAULT NULL,
  `area_func` varchar(40) NOT NULL,
  `ra_func` varchar(8) NOT NULL,
  `cpf_func` varchar(15) NOT NULL,
  `email_func` varchar(40) NOT NULL,
  `grau_instrucao_func` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`cod_funcionario`),
  UNIQUE KEY `cod_funcionario` (`cod_funcionario`),
  UNIQUE KEY `ra_func` (`ra_func`),
  UNIQUE KEY `cpf_func` (`cpf_func`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `funcionario` WRITE;
INSERT INTO `funcionario` VALUES (1,1,'clara','elieide','2007-03-14','MASCULINO','SOLTEIRO(A)','hyuy','964.156.803-25','ujh','6363525265525-12','55665-556','hjh','hhj','MA','Sete Lagoas','(66)65563-5252','53264','SIM','kjkkik','964056','106.864.156-80','hhjhj','EDUCAÇÃO BÁSICA'),(3,2,'clara','eli','2002-06-23','MASCULINO','SOLTEIRO(A)','hui','hi','nkj','6525645665669-65','63552-563','ujhn','buj','AC','bnj','(66)52252-5555','ujh','sim','hi','555636','665.263.632-25','ujhu','EDUCAÇÃO BÁSICA'),(7,8,'vhsgh','hszyg','2002-12-02','MASCULINO','SOLTEIRO(A)','ghuyj','465.478.545-64','fvyhf','5416546415465-48','41316-614','hygyhg','gtuyhtg','AC','yhgtu','(54)16545-4165','ghy','NÃO','yhgt','412416','465.475.645-46','ygyhg','EDUCAÇÃO BÁSICA'),(44,1,'duda','sil','2007-03-16','MASCULINO','SOLTEIRO(A)','jhnhbj','hhj','hjhn','2063163641524-16','65416-563','hgbh','jk','AC','7l','(33)20555-2415','bjn','sim','hgh','635252','633.355.854-71','vhngb','EDUCAÇÃO BÁSICA'),(55,1,'hb','jhj','2002-12-15','MASCULINO','SOLTEIRO(A)','gyh','yh','hyg','3632202236223-22','63632-222','gujh','hhy','AC','ghygb','(52)52523-6322','tg','hgy','gtgfvy','586665','665.252.656-64','fyhg','EDUCAÇÃO BÁSICA'),(65,20,'clara','eli','2007-02-03','MASCULINO','SOLTEIRO(A)','hgb','146.341.541-65','vhbh','4165416545654-16','45846-954','bnjnj','jhn','AC','bjhn','(54)16541-6541','uhjyg','SIM','hnjbh','541615','145.647.564-93','hbj','EDUCAÇÃO BÁSICA');

UNLOCK TABLES;