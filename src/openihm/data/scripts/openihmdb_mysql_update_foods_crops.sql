SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

USE `openihmdb`;

-- -----------------------------------------------------
-- Table `openihmdb`.`setup_foods_crops`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`setup_foods_crops` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_foods_crops` (
  `name` VARCHAR(200) NOT NULL ,
  `category` VARCHAR(200) NOT NULL ,
  `energyvalueperunit` DOUBLE NULL ,
  `unitofmeasure` VARCHAR(45) NULL ,
  PRIMARY KEY (`name`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;