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
-- Table structure for table `cat`
--

DROP TABLE IF EXISTS `cat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cat` (
  `cod_cat` int NOT NULL AUTO_INCREMENT,
  `emitente_cat` varchar(30) DEFAULT NULL,
  `data_emissao_cat` date DEFAULT NULL,
  `tipo_cat` varchar(10) DEFAULT NULL,
  `comunicacao_obito` varchar(5) DEFAULT NULL,
  `filiacao` varchar(50) DEFAULT NULL,
  `email_emitente` varchar(40) DEFAULT NULL,
  `cnpj_empresa` varchar(20) NOT NULL,
  `nome_empresa` varchar(20) NOT NULL,
  `tipo_num_doc_empresa` varchar(14) NOT NULL,
  `cnae_empresa` varchar(12) NOT NULL,
  `telefone_empresa` varchar(20) NOT NULL,
  `cep_empresa` varchar(12) NOT NULL,
  `endereco_empresa` varchar(30) DEFAULT NULL,
  `bairro_empresa` varchar(30) DEFAULT NULL,
  `municipio_empresa` varchar(40) DEFAULT NULL,
  `estado_empresa` varchar(25) DEFAULT NULL,
  `cpf_func` varchar(15) NOT NULL,
  `nome_func` varchar(40) NOT NULL,
  `nome_mae_func` varchar(40) DEFAULT NULL,
  `data_nascimento_func` date NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `grau_instrucao_func` varchar(25) DEFAULT NULL,
  `identidade_func` varchar(15) NOT NULL,
  `estado_civil` varchar(20) NOT NULL,
  `ctps_func` varchar(30) NOT NULL,
  `remuneracao_func` varchar(20) NOT NULL,
  `pis_pasep_nit_func` varchar(20) DEFAULT NULL,
  `cep_func` varchar(15) NOT NULL,
  `endereco_func` varchar(40) DEFAULT NULL,
  `bairro_func` varchar(30) DEFAULT NULL,
  `municipio_func` varchar(40) DEFAULT NULL,
  `estado_func` varchar(25) DEFAULT NULL,
  `telefone_func` varchar(20) NOT NULL,
  `cbo_func` varchar(10) NOT NULL,
  `aposentadoria_func` varchar(15) DEFAULT NULL,
  `area_func` varchar(40) NOT NULL,
  `data_acidente` date DEFAULT NULL,
  `hora_acidente` varchar(10) DEFAULT NULL,
  `horas_trabalhadas` varchar(10) DEFAULT NULL,
  `tipo_acidente` varchar(50) DEFAULT NULL,
  `afastamento` varchar(5) DEFAULT NULL,
  `reg_policial` varchar(7) DEFAULT NULL,
  `local_acidente` varchar(40) DEFAULT NULL,
  `esp_local` varchar(30) DEFAULT NULL,
  `cnpj_cgc_empresa` varchar(18) DEFAULT NULL,
  `uf_acidente` varchar(40) DEFAULT NULL,
  `municipio_acidente` varchar(30) DEFAULT NULL,
  `ult_dia_trab` date DEFAULT NULL,
  `parte_corpo` varchar(255) DEFAULT NULL,
  `agente_causador` varchar(150) DEFAULT NULL,
  `sit_geradora` varchar(255) DEFAULT NULL,
  `morte` varchar(5) DEFAULT NULL,
  `data_obito` date DEFAULT NULL,
  `unidade` varchar(100) DEFAULT NULL,
  `data_atendimento_medico` date DEFAULT NULL,
  `hora_atendimento_medico` varchar(10) DEFAULT NULL,
  `houve_internacao` varchar(5) DEFAULT NULL,
  `afastado` varchar(5) DEFAULT NULL,
  `nat_lesao` varchar(255) DEFAULT NULL,
  `cid` varchar(10) DEFAULT NULL,
  `observacao` varchar(255) DEFAULT NULL,
  `crm` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`cod_cat`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cat`
--

LOCK TABLES `cat` WRITE;
/*!40000 ALTER TABLE `cat` DISABLE KEYS */;
INSERT INTO `cat` VALUES (1,'fede','2002-02-03','INICIAL','SIM','vh','hj','10.242.536/4487-99','hhnh','14641564-16','5416-4/15','(23)36552-2155','56415-46','ujhu','uhnju','AC','ujhu','254-136-441-41','gvfjhvhgv','gfghhyh','2002-10-02','MASCULINO','fvyh','SOLTEIRO(A)','hfvhy','123.143.132-41','hngh','2414136524103-54','23514-021','vhh','gvh','hvhj','AC','(13)54152-4163','141523','SIM','ygu','2023-01-06','08:05','03:30','hgj','SIM','SIM','gvhjgbjh','hvhjb','hhgb','AC','gbjhnuj','2002-03-05','bjj','bj','bhkj','SIM','2023-02-05','jujhuj','2023-05-06','02:20','SIM','SIM','hgbuj','hhg','bguj','bgj'),(2,'defasdfd','2001-10-21','INICIAL','SIM','sadasd','sadsadsa','10.242.536/4487-99','sdasdasdsad','14641564-16','5416-4/15','(31)96945-5748','56415-46','ujhu','uhnju','AC','ujhu','123-456-789-10','sadsadasd','sadsadsads','2004-10-11','MASCULINO','sadasdasd','SOLTEIRO(A)','asdsasda','123.456.789-10','sadasddsad','1234567891022-41','12354-674','sadsadasdsad','asdasdsadads','sadasdsaddsa','AC','(65)46546-4646','216546','SIM','dsadadas','2004-06-10','13:00','14:00','asdasdadsd','SIM','SIM','asddasasddas','sadassdadsa','sadasddas','AC','adsadsasddas','2004-05-11','asdsadasd','sdasdasd','sadsaddaas','SIM','2004-12-25','asdsada','2004-06-11','19:00','SIM','SIM','asdasdasd','sadasda','dasds','saddadassa'),(3,'sadasda','2022-02-11','INICIAL','SIM','sasadsadsa','sadsadas','10.242.536/4487-99','link 7','14641564-16','5416-4/15','(69)59645-6464','56415-46','ujhu','uhnju','CE','ujhu','106.864.156-80','clara','elieide','2007-03-14','MASCULINO','EDUCAÇÃO BÁSICA','SOLTEIRO(A)','ujh','964.156.803-25','hyuy','6363525265525-12','55665-556','hjh','hhj','Sete Lagoas','MA','(66)65563-5252','53264','SIM','kjkkik','2022-05-11','12:00','10:00','asdsadas','SIM','SIM','sadasdsa','dsadsa','asdsada','AC','sadasdas','2022-05-10','xczxcz','xcxzcz','xzczxcc','SIM','2022-05-12','sadasd','2022-05-12','14:00','SIM','SIM','asdsadd','sadasd','sadsadsa','sadsadasd');
/*!40000 ALTER TABLE `cat` ENABLE KEYS */;
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
