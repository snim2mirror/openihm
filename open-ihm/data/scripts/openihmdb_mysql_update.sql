SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

-- -----------------------------------------------------
-- Table `openihmdb`.`setup_standardofliving`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_standardofliving` (
  `item` VARCHAR(255) NOT NULL ,
  `type` ENUM('Household','Person','Both') NOT NULL ,
  PRIMARY KEY (`item`) )
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `openihmdb`.`standardofliving`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`standardofliving`;
CREATE  TABLE IF NOT EXISTS `openihmdb`.`standardofliving` (
  `pid` INT(11) NOT NULL ,
  `summary` VARCHAR(255) NOT NULL ,
  `scope` ENUM('Household','Person') NOT NULL ,
  `gender` ENUM('Male','Female','All') NULL DEFAULT NULL ,
  `agebottom` INT NULL DEFAULT 0 ,
  `agetop` INT NULL DEFAULT 0 ,
  `item` VARCHAR(255) NOT NULL ,
  `costperyear` DOUBLE NOT NULL ,
  PRIMARY KEY (`pid`, `summary`) ,
  INDEX `fk_standardofliving_projects1` (`pid` ASC) ,
  CONSTRAINT `fk_standardofliving_projects1`
    FOREIGN KEY (`pid` )
    REFERENCES `openihmdb`.`projects` (`pid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
