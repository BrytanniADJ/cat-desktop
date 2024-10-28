-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: cat_treinee
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `funcionario`
--

DROP TABLE IF EXISTS `funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionario`
--

LOCK TABLES `funcionario` WRITE;
/*!40000 ALTER TABLE `funcionario` DISABLE KEYS */;
INSERT INTO `funcionario` VALUES (1,1,'clara','elieide','2007-03-14','MASCULINO','SOLTEIRO(A)','hyuy','964.156.803-25','ujh','6363525265525-12','55665-556','hjh','hhj','MA','Sete Lagoas','(66)65563-5252','53264','SIM','kjkkik','964056','106.864.156-80','hhjhj','EDUCAÇÃO BÁSICA'),(3,2,'clara','eli','2002-06-23','MASCULINO','SOLTEIRO(A)','hui','hi','nkj','6525645665669-65','63552-563','ujhn','buj','AC','bnj','(66)52252-5555','ujh','sim','hi','555636','665.263.632-25','ujhu','EDUCAÇÃO BÁSICA'),(7,8,'vhsgh','hszyg','2002-12-02','MASCULINO','SOLTEIRO(A)','ghuyj','465.478.545-64','fvyhf','5416546415465-48','41316-614','hygyhg','gtuyhtg','AC','yhgtu','(54)16545-4165','ghy','NÃO','yhgt','412416','465.475.645-46','ygyhg','EDUCAÇÃO BÁSICA'),(44,1,'duda','sil','2007-03-16','MASCULINO','SOLTEIRO(A)','jhnhbj','hhj','hjhn','2063163641524-16','65416-563','hgbh','jk','AC','7l','(33)20555-2415','bjn','sim','hgh','635252','633.355.854-71','vhngb','EDUCAÇÃO BÁSICA'),(55,1,'hb','jhj','2002-12-15','MASCULINO','SOLTEIRO(A)','gyh','yh','hyg','3632202236223-22','63632-222','gujh','hhy','AC','ghygb','(52)52523-6322','tg','hgy','gtgfvy','586665','665.252.656-64','fyhg','EDUCAÇÃO BÁSICA'),(65,20,'clara','eli','2007-02-03','MASCULINO','SOLTEIRO(A)','hgb','146.341.541-65','vhbh','4165416545654-16','45846-954','bnjnj','jhn','AC','bjhn','(54)16541-6541','uhjyg','SIM','hnjbh','541615','145.647.564-93','hbj','EDUCAÇÃO BÁSICA');
/*!40000 ALTER TABLE `funcionario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-26 13:39:49
