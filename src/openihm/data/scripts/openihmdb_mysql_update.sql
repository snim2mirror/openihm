SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

USE `openihmdb`;

-- -----------------------------------------------------
-- Table `openihmdb`.`projectassets`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `openihmdb`.`projectassets` (
  `pid` INT NOT NULL ,
  `assetname` VARCHAR(255) NOT NULL ,
  `assettype` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`pid`, `assetname`) ,
  INDEX `pid` (`pid` ASC) ,
  CONSTRAINT `pid`
    FOREIGN KEY (`pid` )
    REFERENCES `openihmdb`.`projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `openihmdb`.`setup_assets`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_assets` (
  `assetname` VARCHAR(255) NOT NULL ,
  `assettype` VARCHAR(50) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`assetname`) )
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `openihmdb`.`globalcharacteristics`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `openihmdb`.`globalcharacteristics` (
  `characteristic` VARCHAR(250) NOT NULL ,
  `chartype` VARCHAR(50) NOT NULL ,
  `datatype` INT(11) NOT NULL ,
  `description` VARCHAR(250) NULL DEFAULT NULL ,
  PRIMARY KEY (`characteristic`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_swedish_ci;

-- -----------------------------------------------------
-- Table `openihmdb`.`projectcharacteristics`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `openihmdb`.`projectcharacteristics` (
  `pid` INT(11) NOT NULL ,
  `characteristic` VARCHAR(250) NOT NULL ,
  `chartype` VARCHAR(50) NOT NULL ,
  `datatype` INT(11) NOT NULL ,
  PRIMARY KEY (`pid`, `characteristic`) ,
  CONSTRAINT `fk_projectcharacteristics_projects1`
    FOREIGN KEY (`pid` )
    REFERENCES `openihmdb`.`projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_swedish_ci;


-- -----------------------------------------------------
-- Table `openihmdb`.`householdcharacteristics`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `openihmdb`.`householdcharacteristics` (
  `pid` INT(11) NOT NULL ,
  `hhid` INT(11) NOT NULL ,
  `characteristic` VARCHAR(250) NOT NULL ,
  `charvalue` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`pid`, `hhid`, `characteristic`) ,
  CONSTRAINT `fk_householdcharacteristics_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_swedish_ci;

-- -----------------------------------------------------
-- Table `openihmdb`.`personalcharacteristics`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `openihmdb`.`personalcharacteristics` (
  `pid` INT(11) NOT NULL ,
  `hhid` INT(11) NOT NULL ,
  `personid` VARCHAR(20) NOT NULL ,
  `characteristic` VARCHAR(250) NOT NULL ,
  `charvalue` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`pid`, `hhid`, `personid`, `characteristic`) ,
  CONSTRAINT `fk_personalcharacteristics_householdmembers1`
    FOREIGN KEY (`personid` , `hhid` , `pid` )
    REFERENCES `openihmdb`.`householdmembers` (`personid` , `hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_swedish_ci;

-- -----------------------------------------------------
-- Table `openihmdb`.`transferlog`
-- -----------------------------------------------------

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

-- -----------------------------------------------------
-- Enforce referential integrity
-- -----------------------------------------------------

ALTER TABLE `openihmdb`.`personalcharacteristics` DROP FOREIGN KEY `fk_personalcharacteristics_householdmembers1` ;
ALTER TABLE `openihmdb`.`personalcharacteristics` 
  ADD CONSTRAINT `fk_personalcharacteristics_householdmembers1`
  FOREIGN KEY (`personid` , `hhid` , `pid` )
  REFERENCES `openihmdb`.`householdmembers` (`personid` , `hhid` , `pid` )
  ON DELETE CASCADE
  ON UPDATE CASCADE;
  
ALTER TABLE `openihmdb`.`projectcharacteristics` DROP FOREIGN KEY `fk_projectcharacteristics_projects1` ;
ALTER TABLE `openihmdb`.`projectcharacteristics` 
  ADD CONSTRAINT `fk_projectcharacteristics_projects1`
  FOREIGN KEY (`pid` )
  REFERENCES `openihmdb`.`projects` (`pid` )
  ON DELETE CASCADE
  ON UPDATE CASCADE;
  
ALTER TABLE `openihmdb`.`householdcharacteristics` DROP FOREIGN KEY `fk_householdcharacteristics_households1` ;
ALTER TABLE `openihmdb`.`householdcharacteristics` 
  ADD CONSTRAINT `fk_householdcharacteristics_households1`
  FOREIGN KEY (`hhid` , `pid` )
  REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
  ON DELETE CASCADE
  ON UPDATE CASCADE;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
