SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

USE `openihmdb`;

-- -----------------------------------------------------
-- Table `openihmdb`.`assets`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`assets`;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`assets` (
  `assetid` INT(11) NOT NULL AUTO_INCREMENT ,
  `hhid` INT(11) NOT NULL ,
  `assetcategory` VARCHAR(255) NOT NULL ,
  `assettype` VARCHAR(100) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  `unitcost` DOUBLE NOT NULL ,
  `totalunits` DOUBLE NOT NULL ,
  `pid` INT(11) NOT NULL ,
  PRIMARY KEY (`assetid`, `hhid`, `pid`) ,
  INDEX `fk_assets_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_assets_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `openihmdb`.`diet`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`diet`;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`diet` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `pid` INT(11) NOT NULL ,
  `fooditem` VARCHAR(45) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  `percentage` DOUBLE NOT NULL ,
  `priceperunit` DOUBLE NOT NULL ,
  PRIMARY KEY (`id`, `pid`) ,
  INDEX `fk_diet_projects1` (`pid` ASC) ,
  CONSTRAINT `fk_diet_projects1`
    FOREIGN KEY (`pid` )
    REFERENCES `openihmdb`.`projects` (`pid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

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
AUTO_INCREMENT = 3
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
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `openihmdb`.`employmentincome`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`employmentincome`;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`employmentincome` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hhid` INT(11) NOT NULL ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  `foodtypepaid` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `unitspaid` DOUBLE NULL DEFAULT NULL ,
  `incomekcal` DOUBLE NULL DEFAULT NULL ,
  `cashincome` DOUBLE NULL DEFAULT NULL ,
  `pid` INT(11) NOT NULL ,
  PRIMARY KEY (`id`, `hhid`, `pid`) ,
  INDEX `fk_employmentincome_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_employmentincome_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `openihmdb`.`transfers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`transfers`;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`transfers` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hhid` INT(11) NOT NULL ,
  `pid` INT(11) NOT NULL ,
  `sourcetype` ENUM('Internal','External') NOT NULL ,
  `sourceoftransfer` VARCHAR(255) NOT NULL ,
  `cashperyear` DOUBLE NULL DEFAULT 0.00 ,
  `foodtype` VARCHAR(255) NULL ,
  `unitofmeasure` VARCHAR(45) NULL ,
  `unitsgiven` DOUBLE NULL DEFAULT 0.00 ,
  `unitsconsumed` DOUBLE NULL DEFAULT 0.00 ,
  `unitssold` DOUBLE NULL DEFAULT 0.00 ,
  `priceperunit` DOUBLE NULL DEFAULT 0.00 ,
  PRIMARY KEY (`id`, `hhid`, `pid`) ,
  INDEX `fk_transfers_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_transfers_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
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
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `openihmdb`.`expenditure`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`expenditure`;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`expenditure` (
  `expid` INT(11) NOT NULL AUTO_INCREMENT ,
  `hhid` INT(11) NOT NULL ,
  `exptype` VARCHAR(100) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `priceperunit` DOUBLE NULL DEFAULT NULL ,
  `kcalperunit` DOUBLE NULL DEFAULT NULL ,
  `totalunits` DOUBLE NULL DEFAULT NULL ,
  `pid` INT(11) NOT NULL ,
  PRIMARY KEY (`expid`, `hhid`, `pid`) ,
  INDEX `fk_expenditure_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_expenditure_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;