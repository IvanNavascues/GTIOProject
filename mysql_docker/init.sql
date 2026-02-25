CREATE DATABASE IF NOT EXISTS votacion;

CREATE TABLE IF NOT EXISTS votes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(20) NOT NULL,
            votes INT DEFAULT 0
        );

INSERT INTO votes (`name`) VALUES ("Carlos Fustel");
INSERT INTO votes (`name`) VALUES ("Claudia Arenas");
INSERT INTO votes (`name`) VALUES ("Cristina Lora");
INSERT INTO votes (`name`) VALUES ("Elena Matateyou");
INSERT INTO votes (`name`) VALUES ("Guille Toledano");
INSERT INTO votes (`name`) VALUES ("Guillo Rist");
INSERT INTO votes (`name`) VALUES ("Ivan Rojo");
INSERT INTO votes (`name`) VALUES ("Javier Crespo");
INSERT INTO votes (`name`) VALUES ("Judit Garuz");
INSERT INTO votes (`name`) VALUES ("Laura Munyoz");
INSERT INTO votes (`name`) VALUES ("Lucia Casani");
INSERT INTO votes (`name`) VALUES ("Maria Cruz");
INSERT INTO votes (`name`) VALUES ("Martin Yanyez");
INSERT INTO votes (`name`) VALUES ("Olivia Bay");
INSERT INTO votes (`name`) VALUES ("Salma De Diego");