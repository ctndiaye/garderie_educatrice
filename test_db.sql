-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : dim. 09 juin 2024 à 23:21
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `db_educatrice`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=36953 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(36925, 'Can add log entry', 9232, 'add_logentry'),
(36926, 'Can change log entry', 9232, 'change_logentry'),
(36927, 'Can delete log entry', 9232, 'delete_logentry'),
(36928, 'Can view log entry', 9232, 'view_logentry'),
(36929, 'Can add permission', 9233, 'add_permission'),
(36930, 'Can change permission', 9233, 'change_permission'),
(36931, 'Can delete permission', 9233, 'delete_permission'),
(36932, 'Can view permission', 9233, 'view_permission'),
(36933, 'Can add group', 9234, 'add_group'),
(36934, 'Can change group', 9234, 'change_group'),
(36935, 'Can delete group', 9234, 'delete_group'),
(36936, 'Can view group', 9234, 'view_group'),
(36937, 'Can add content type', 9235, 'add_contenttype'),
(36938, 'Can change content type', 9235, 'change_contenttype'),
(36939, 'Can delete content type', 9235, 'delete_contenttype'),
(36940, 'Can view content type', 9235, 'view_contenttype'),
(36941, 'Can add session', 9236, 'add_session'),
(36942, 'Can change session', 9236, 'change_session'),
(36943, 'Can delete session', 9236, 'delete_session'),
(36944, 'Can view session', 9236, 'view_session'),
(36945, 'Can add user', 9237, 'add_educatrice'),
(36946, 'Can change user', 9237, 'change_educatrice'),
(36947, 'Can delete user', 9237, 'delete_educatrice'),
(36948, 'Can view user', 9237, 'view_educatrice'),
(36949, 'Can add presence', 9238, 'add_presence'),
(36950, 'Can change presence', 9238, 'change_presence'),
(36951, 'Can delete presence', 9238, 'delete_presence'),
(36952, 'Can view presence', 9238, 'view_presence');

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=9239 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(9232, 'admin', 'logentry'),
(9233, 'auth', 'permission'),
(9234, 'auth', 'group'),
(9235, 'contenttypes', 'contenttype'),
(9236, 'sessions', 'session'),
(9237, 'educatrice', 'educatrice'),
(9238, 'educatrice', 'presence');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-06-06 14:11:04.558762'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-06-06 14:11:04.674631'),
(3, 'auth', '0001_initial', '2024-06-06 14:11:05.014630'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-06-06 14:11:05.058631'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-06-06 14:11:05.067632'),
(6, 'auth', '0004_alter_user_username_opts', '2024-06-06 14:11:05.075633'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-06-06 14:11:05.081632'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-06-06 14:11:05.084632'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-06-06 14:11:05.092628'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-06-06 14:11:05.099630'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-06-06 14:11:05.106630'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-06-06 14:11:05.148630'),
(13, 'auth', '0011_update_proxy_permissions', '2024-06-06 14:11:05.155630'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-06-06 14:11:05.162630'),
(15, 'educatrice', '0001_initial', '2024-06-06 14:11:05.766931');

-- --------------------------------------------------------

--
-- Structure de la table `educatrice_educatrice`
--

DROP TABLE IF EXISTS `educatrice_educatrice`;
CREATE TABLE IF NOT EXISTS `educatrice_educatrice` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `adresse` longtext NOT NULL,
  `telephone` varchar(20) NOT NULL,
  `est_qualifie` tinyint(1) NOT NULL,
  `est_active` tinyint(1) NOT NULL,
  `sexe` varchar(10) NOT NULL,
  `nom_contact` varchar(20) NOT NULL,
  `prenom_contact` varchar(30) NOT NULL,
  `telephone_contact` varchar(20) NOT NULL,
  `date_creation` datetime(6) NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  `statut` varchar(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `telephone` (`telephone`)
) ENGINE=MyISAM AUTO_INCREMENT=542 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `educatrice_educatrice_groups`
--

DROP TABLE IF EXISTS `educatrice_educatrice_groups`;
CREATE TABLE IF NOT EXISTS `educatrice_educatrice_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `educatrice_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `educatrice_educatrice_gr_educatrice_id_group_id_147901fc_uniq` (`educatrice_id`,`group_id`),
  KEY `educatrice_educatrice_groups_educatrice_id_963e26f2` (`educatrice_id`),
  KEY `educatrice_educatrice_groups_group_id_11c84214` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `educatrice_educatrice_user_permissions`
--

DROP TABLE IF EXISTS `educatrice_educatrice_user_permissions`;
CREATE TABLE IF NOT EXISTS `educatrice_educatrice_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `educatrice_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `educatrice_educatrice_us_educatrice_id_permission_ba086f74_uniq` (`educatrice_id`,`permission_id`),
  KEY `educatrice_educatrice_user_permissions_educatrice_id_0d1603c2` (`educatrice_id`),
  KEY `educatrice_educatrice_user_permissions_permission_id_42dc15b2` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `educatrice_presence`
--

DROP TABLE IF EXISTS `educatrice_presence`;
CREATE TABLE IF NOT EXISTS `educatrice_presence` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `heure_evenement` datetime(6) NOT NULL,
  `type_evenement` varchar(6) NOT NULL,
  `educatrice_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `educatrice_presence_educatrice_id_142de7ea` (`educatrice_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
