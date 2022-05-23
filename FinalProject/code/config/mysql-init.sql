DROP USER IF EXISTS 'test_qa';
CREATE USER 'test_qa' IDENTIFIED BY 'qa_test';
GRANT ALL PRIVILEGES ON * . * TO 'test_qa';
DROP database IF EXISTS basefinalproject;
CREATE DATABASE basefinalproject;
USE basefinalproject;
CREATE TABLE `test_users` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `surname` varchar(255) NOT NULL,
    `middle_name` varchar(255) DEFAULT NULL,
    `username` varchar(16) DEFAULT NULL,
    `password` varchar(255) NOT NULL,
    `email` varchar(64) NOT NULL,
    `access` smallint DEFAULT NULL,
    `active` smallint DEFAULT NULL,
    `start_active_time` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `email` (`email`),
    UNIQUE KEY `ix_test_users_username` (`username`)
);
FLUSH PRIVILEGES;