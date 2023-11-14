-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 06-Nov-2023 às 18:53
-- Versão do servidor: 10.4.25-MariaDB
-- versão do PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `candidatos`
--
CREATE DATABASE IF NOT EXISTS `candidatos` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `candidatos`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `candidatos`
--

CREATE TABLE `candidatos` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `minibio` text DEFAULT NULL,
  `entrevista` decimal(5,2) DEFAULT NULL,
  `teste_teórico` decimal(5,2) DEFAULT NULL,
  `teste_prático` decimal(5,2) DEFAULT NULL,
  `soft_skills` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `candidatos`
--

INSERT INTO `candidatos` (`id`, `nome`, `telefone`, `minibio`, `entrevista`, `teste_teórico`, `teste_prático`, `soft_skills`) VALUES
(1, 'Ana', '996335800', 'dedicada', '10.00', '10.00', '10.00', '10.00'),
(2, 'Flaise', '9966335800', 'competente', '10.00', '10.00', '10.00', '10.00'),
(3, 'João', '996335800', 'proativo', '10.00', '10.00', '10.00', '10.00'),
(4, 'Marta', '996335801', 'criativa', '9.50', '9.50', '9.50', '9.50'),
(5, 'Pedro', '996335802', 'inteligente', '8.75', '8.75', '8.75', '8.75'),
(6, 'Lara', '996335803', 'dedicada', '9.80', '9.80', '9.80', '9.80'),
(7, 'Ricardo', '996335804', 'pontual', '9.25', '9.25', '9.25', '9.25'),
(8, 'Sofia', '996335805', 'amigável', '9.60', '9.60', '9.60', '9.60'),
(9, 'Carlos', '996335806', 'organizado', '8.90', '8.90', '8.90', '8.90'),
(10, 'Mariana', '996335807', 'inovador', '9.70', '9.70', '9.70', '9.70'),
(11, 'Antônio', '996335808', 'competente', '9.40', '9.40', '9.40', '9.40'),
(12, 'Beatriz', '996335809', 'carismático', '9.55', '9.55', '9.55', '9.55'),
(13, 'Paulo', '996335810', 'otimista', '9.10', '9.10', '9.10', '9.10'),
(14, 'Isabela', '996335811', 'proativo', '8.50', '8.50', '8.50', '8.50'),
(15, 'Gustavo', '996335812', 'criativo', '9.75', '9.75', '9.75', '9.75'),
(16, 'Laura', '996335813', 'empreendedor', '9.85', '9.85', '9.85', '9.85'),
(17, 'Daniel', '996335814', 'confiável', '8.65', '8.65', '8.65', '8.65'),
(18, 'Ana Clara', '996335815', 'perseverante', '8.45', '8.45', '8.45', '8.45'),
(19, 'Matheus', '996335816', 'sociável', '9.20', '9.20', '9.20', '9.20'),
(20, 'Lívia', '996335817', 'flexível', '8.30', '8.30', '8.30', '8.30');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `candidatos`
--
ALTER TABLE `candidatos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `candidatos`
--
ALTER TABLE `candidatos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
