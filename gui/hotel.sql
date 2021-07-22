-- -----------------------------------------------------
-- Table `room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `room` (
  `id` INT NOT NULL,
  `price` DECIMAL(18,2) NOT NULL,
  `apart_num` INT NOT NULL,
  `free` BOOL default TRUE,
   PRIMARY KEY (`id`)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;


-- -----------------------------------------------------
-- Table `client-room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_room` (
  `client_id` INT NOT NULL,
  `room_id` INT NOT NULL,		
  `date_in` DATETIME NOT NULL,
  `date_out` DATETIME NOT NULL,
PRIMARY KEY (`client_id`,`room_id`,`date_in`,`date_out`),
INDEX `fk_room_idx` (`room_id` ASC),
CONSTRAINT `fk_room_id`
    FOREIGN KEY (`room_id`)
    REFERENCES `room` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

DELIMITER $$
CREATE TRIGGER client_room_AFINSERT AFTER INSERT
ON client_room
FOR EACH ROW
BEGIN
IF (NEW.date_in<CURRENT_DATE() AND NEW.date_out>CURRENT_DATE()) THEN
	UPDATE room SET room.free = 0 WHERE NEW.room_id=room.id;
/*ELSEIF (NEW.date_in>CURRENT_DATE() OR NEW.date_out<CURRENT_DATE()) THEN
	UPDATE room SET room.free = 1 WHERE NEW.room_id=room.id;*/
END IF;
END$$
DELIMITER ;

-- -----------------------------------------------------
-- Table `service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `service` (
  `id` INT NOT NULL,
  `type` VARCHAR(255) NOT NULL,
  `price` DECIMAL(18,2) NOT NULL,
  PRIMARY KEY (`id`)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;


-- -----------------------------------------------------
-- Table `client-service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_service` (
  `client_id` INT NOT NULL,
  `service_id` INT NOT NULL,
  `date` DATETIME NOT NULL,
PRIMARY KEY (`client_id`,`service_id`,`date`),
INDEX `fk_service_idx` (`service_id` ASC),
CONSTRAINT `fk_service_id`
    FOREIGN KEY (`service_id`)
    REFERENCES `service` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;


-- -----------------------------------------------------
-- Table `client`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client` (
  `id` INT NOT NULL,
  `name` VARCHAR(255) NULL,
  `service_list_id` INT NULL,
  `room_list_id` INT NULL,
  PRIMARY KEY (`id`),
INDEX `fk_room_list_idx` (`room_list_id` ASC),
CONSTRAINT `fk_room_list_id`
    FOREIGN KEY (`room_list_id`)
    REFERENCES `client_room` (`client_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
INDEX `fk_service_list_idx` (`service_list_id` ASC),
CONSTRAINT `fk_service_list_id`
    FOREIGN KEY (`service_list_id`) 
    REFERENCES `client_service` (`client_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;


DELIMITER $$
CREATE TRIGGER client_room_list_AFINSERT AFTER INSERT
ON client_room
FOR EACH ROW
BEGIN
	UPDATE client SET client.room_list_id = NEW.client_id WHERE client.id=NEW.client_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER client_service_list_AFINSERT AFTER INSERT
ON client_service
FOR EACH ROW
BEGIN
	UPDATE client SET client.service_list_id = NEW.client_id WHERE client.id=NEW.client_id;
END$$
DELIMITER ;


-- -----------------------------------------------------
-- Data for table `room`
-- -----------------------------------------------------
INSERT INTO `room` (`id`,`price`,`apart_num`) VALUES (1,3000,2);
INSERT INTO `room` (`id`,`price`,`apart_num`) VALUES (2,2000,3);
INSERT INTO `room` (`id`,`price`,`apart_num`) VALUES (3,3000,2);
INSERT INTO `room` (`id`,`price`,`apart_num`) VALUES (4,3000,2);
INSERT INTO `room` (`id`,`price`,`apart_num`) VALUES (5,4000,2);
INSERT INTO `room` (`id`,`price`,`apart_num`) VALUES (6,5000,2);
INSERT INTO `room` (`id`,`price`,`apart_num`) VALUES (7,9000,5);
INSERT INTO `room` (`id`,`price`,`apart_num`) VALUES (8,4000,2);
INSERT INTO `room` (`id`,`price`,`apart_num`) VALUES (9,1000,2);
INSERT INTO `room` (`id`,`price`,`apart_num`) VALUES (10,5000,2);

-- -----------------------------------------------------
-- Data for table `client-room`
-- -----------------------------------------------------
INSERT INTO `client_room` (`client_id`,`room_id`,`date_in`,`date_out`) VALUES (10,2,'2021.03.25','2021.03.27');
INSERT INTO `client_room` (`client_id`,`room_id`,`date_in`,`date_out`) VALUES (7,1,'2021.02.16','2021.02.17');
INSERT INTO `client_room` (`client_id`,`room_id`,`date_in`,`date_out`) VALUES (2,5,'2021.03.13','2021.03.14');
INSERT INTO `client_room` (`client_id`,`room_id`,`date_in`,`date_out`) VALUES (3,4,'2021.02.12','2021.02.26');
INSERT INTO `client_room` (`client_id`,`room_id`,`date_in`,`date_out`) VALUES (1,2,'2021.02.15','2021.02.18');
INSERT INTO `client_room` (`client_id`,`room_id`,`date_in`,`date_out`) VALUES (5,8,'2021.03.25','2021.03.29');
INSERT INTO `client_room` (`client_id`,`room_id`,`date_in`,`date_out`) VALUES (6,7,'2021.03.6','2021.03.17');
INSERT INTO `client_room` (`client_id`,`room_id`,`date_in`,`date_out`) VALUES (4,3,'2021.03.3','2021.03.14');
INSERT INTO `client_room` (`client_id`,`room_id`,`date_in`,`date_out`) VALUES (8,6,'2021.03.2','2021.03.15');
INSERT INTO `client_room` (`client_id`,`room_id`,`date_in`,`date_out`) VALUES (9,9,'2021.03.5','2021.03.18');


-- -----------------------------------------------------
-- Data for table `service`
-- -----------------------------------------------------
INSERT INTO `service` (`id`, `type`,`price`) VALUES (1, 'cleaning', 500);
INSERT INTO `service` (`id`, `type`,`price`) VALUES (2, 'food', 100);
INSERT INTO `service` (`id`, `type`,`price`) VALUES (3, 'pool', 1000);
INSERT INTO `service` (`id`, `type`,`price`) VALUES (4, 'alcohol', 500);
INSERT INTO `service` (`id`, `type`,`price`) VALUES (5, 'kalian',1000);


-- -----------------------------------------------------
-- Data for table `client-service`
-- -----------------------------------------------------
INSERT INTO `client_service` (`client_id`,`service_id`,`date`) VALUES (1,2,'2021.02.25');
INSERT INTO `client_service` (`client_id`,`service_id`,`date`) VALUES (7,1,'2021.02.21');
INSERT INTO `client_service` (`client_id`,`service_id`,`date`) VALUES (2,5,'2021.03.23');
INSERT INTO `client_service` (`client_id`,`service_id`,`date`) VALUES (3,4,'2021.02.28');
INSERT INTO `client_service` (`client_id`,`service_id`,`date`) VALUES (10,3,'2021.03.25');
INSERT INTO `client_service` (`client_id`,`service_id`,`date`) VALUES (5,5,'2021.03.23');
INSERT INTO `client_service` (`client_id`,`service_id`,`date`) VALUES (6,4,'2021.03.20');
INSERT INTO `client_service` (`client_id`,`service_id`,`date`) VALUES (4,3,'2021.03.28');
INSERT INTO `client_service` (`client_id`,`service_id`,`date`) VALUES (8,2,'2021.03.22');
INSERT INTO `client_service` (`client_id`,`service_id`,`date`) VALUES (9,1,'2021.03.21');


-- -----------------------------------------------------
-- Data for table `client`
-- -----------------------------------------------------
INSERT INTO `client` (`id`, `name`,`service_list_id`,`room_list_id`) VALUES (1, 'Ariel',1,1);
INSERT INTO `client` (`id`, `name`,`service_list_id`,`room_list_id`) VALUES (2, 'Ash',2,2);
INSERT INTO `client` (`id`, `name`,`service_list_id`,`room_list_id`) VALUES (3, 'Johan',3,3);
INSERT INTO `client` (`id`, `name`,`service_list_id`,`room_list_id`) VALUES (4, 'Kiel',4,4);
INSERT INTO `client` (`id`, `name`,`service_list_id`,`room_list_id`) VALUES (5, 'Shinae',5,5);
INSERT INTO `client` (`id`, `name`,`service_list_id`,`room_list_id`) VALUES (6, 'Crys',6,6);
INSERT INTO `client` (`id`, `name`,`service_list_id`,`room_list_id`) VALUES (7, 'Quentana',7,7);
INSERT INTO `client` (`id`, `name`,`service_list_id`,`room_list_id`) VALUES (8, 'Sarvati',8,8);
INSERT INTO `client` (`id`, `name`,`service_list_id`,`room_list_id`) VALUES (9, 'John',9,9);
INSERT INTO `client` (`id`, `name`,`service_list_id`,`room_list_id`) VALUES (10, 'Ainz',10,10);

-- -----------------------------------------------------
-- END
-- -----------------------------------------------------

COMMIT;
