SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

-- -----------------------------------------------------
-- Table `openihmdb`.`projectincomesources`
-- -----------------------------------------------------
USE `openihmdb`;

-- -----------------------------------------------------
-- Table `openihmdb`.`cropincome`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`cropincome`;
CREATE  TABLE IF NOT EXISTS `openihmdb`.`cropincome` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hhid` INT(11) NOT NULL ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `unitsproduced` DOUBLE NULL DEFAULT '0' ,
  `unitssold` DOUBLE NULL DEFAULT NULL ,
  `unitprice` DOUBLE NULL DEFAULT NULL ,
  `otheruses` DOUBLE NULL DEFAULT '0' ,
  `unitsconsumed` DOUBLE NULL DEFAULT '0' ,
  `pid` INT(11) NOT NULL ,
  PRIMARY KEY (`id`, `hhid`, `pid`) ,
  INDEX `fk_cropincome_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_cropincome_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `openihmdb`.`livestockincome`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`livestockincome`;
CREATE  TABLE IF NOT EXISTS `openihmdb`.`livestockincome` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hhid` INT(11) NOT NULL ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `unitsproduced` DOUBLE NULL DEFAULT '0' ,
  `unitssold` DOUBLE NULL DEFAULT NULL ,
  `unitprice` DOUBLE NULL DEFAULT NULL ,
  `otheruses` DOUBLE NULL DEFAULT '0' ,
  `unitsconsumed` DOUBLE NULL DEFAULT '0' ,
  `pid` INT(11) NOT NULL ,
  PRIMARY KEY (`id`, `hhid`, `pid`) ,
  INDEX `fk_livestockincome_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_livestockincome_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `openihmdb`.`wildfoods`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`wildfoods`;
CREATE  TABLE IF NOT EXISTS `openihmdb`.`wildfoods` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hhid` INT(11) NOT NULL ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `unitsproduced` DOUBLE NULL DEFAULT '0' ,
  `unitssold` DOUBLE NULL DEFAULT NULL ,
  `unitprice` DOUBLE NULL DEFAULT NULL ,
  `otheruses` DOUBLE NULL DEFAULT '0' ,
  `unitsconsumed` DOUBLE NULL DEFAULT '0' ,
  `pid` INT(11) NOT NULL ,
  PRIMARY KEY (`id`, `hhid`, `pid`) ,
  INDEX `fk_wildfoods_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_wildfoods_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
