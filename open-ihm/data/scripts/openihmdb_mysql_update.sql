SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

-- -----------------------------------------------------
-- Table `openihmdb`.`projectincomesources`
-- -----------------------------------------------------
USE `openihmdb`;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`projectincomesources` (
  `pid` INT(11) NOT NULL ,
  `incomesource` VARCHAR(255) NOT NULL ,
  `incometype` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`incomesource`, `pid`) ,
  INDEX `fk_projectincomesources_projects` (`pid` ASC) ,
  CONSTRAINT `fk_projectincomesources_projects`
    FOREIGN KEY (`pid` )
    REFERENCES `openihmdb`.`projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
