SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

USE `openihmdb`;

-- -----------------------------------------------------
-- Update Table `openihmdb`.`projects`
-- -----------------------------------------------------

ALTER TABLE `openihmdb`.`projects` CHANGE COLUMN `projectname` `projectname` VARCHAR(255) NOT NULL  ;

-- -----------------------------------------------------
-- Table `openihmdb`.`transferlog`
-- -----------------------------------------------------

ALTER TABLE `openihmdb`.`transferlog` CHANGE COLUMN `projectname` `projectname` VARCHAR(255) NOT NULL  ; 


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
