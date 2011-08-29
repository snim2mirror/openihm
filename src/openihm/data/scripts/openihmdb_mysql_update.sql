SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

-- -----------------------------------------------------
-- Table `openihmdb`.`transferlog`
-- -----------------------------------------------------
USE `openihmdb`;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`transferlog` (
  `pid` INT(11) NOT NULL ,
  `pid_access` INT(11) NOT NULL ,
  `projectname` VARCHAR(45) NOT NULL ,
  `datecollected` VARCHAR(45) NOT NULL ,
  `currency` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`pid`) ,
  CONSTRAINT `fk_transferlog_projects1`
    FOREIGN KEY (`pid` )
    REFERENCES `openihmdb`.`projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_swedish_ci;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
