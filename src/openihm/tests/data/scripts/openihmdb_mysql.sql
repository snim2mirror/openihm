SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

USE `test_openihm`;

-- -----------------------------------------------------
-- Table `projects`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `projects` (
  `pid` INT(11) NOT NULL AUTO_INCREMENT ,
  `projectname` VARCHAR(100) NOT NULL ,
  `startdate` DATE NOT NULL ,
  `enddate` DATE NOT NULL ,
  `description` TEXT NOT NULL ,
  `currency` TEXT NOT NULL ,
  PRIMARY KEY (`pid`) )
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `projectincomesources`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `projectincomesources` (
  `pid` INT(11) NOT NULL ,
  `incomesource` VARCHAR(255) NOT NULL ,
  `incometype` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`incomesource`, `pid`, `incometype`) ,
  INDEX `fk_projectincomesources_projects` (`pid` ASC) ,
  CONSTRAINT `fk_projectincomesources_projects`
    FOREIGN KEY (`pid` )
    REFERENCES `projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `households`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `households` (
  `hhid` INT(11) NOT NULL ,
  `householdname` VARCHAR(100) NOT NULL ,
  `totalassetvalue` DOUBLE NOT NULL DEFAULT '0' ,
  `totalincomevalue` DOUBLE NOT NULL DEFAULT '0' ,
  `totalexpenditure` DOUBLE NOT NULL DEFAULT '0' ,
  `dateofcollection` DATE NOT NULL ,
  `pid` INT(11) NOT NULL ,
  PRIMARY KEY (`hhid`, `pid`) ,
  INDEX `fk_households_projects1` (`pid` ASC) ,
  CONSTRAINT `fk_households_projects1`
    FOREIGN KEY (`pid` )
    REFERENCES `projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `householdmembers`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `householdmembers` (
  `personid` VARCHAR(20) NOT NULL ,
  `hhid` INT(11) NOT NULL ,
  `headofhousehold` ENUM('Yes','No') NOT NULL ,
  `yearofbirth` INT(11) NOT NULL ,
  `sex` ENUM('Male','Female') NOT NULL ,
  `education` VARCHAR(200) NULL DEFAULT NULL ,
  `pid` INT(11) NOT NULL ,
  `periodaway` INT(11) NULL DEFAULT '0' ,
  `reason` VARCHAR(200) NULL DEFAULT NULL ,
  `whereto` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`personid`, `hhid`, `pid`) ,
  INDEX `fk_householdmembers_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_householdmembers_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `absencefromhousehold`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `absencefromhousehold` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `percentageaway` DOUBLE NOT NULL ,
  `reason` VARCHAR(200) NOT NULL ,
  `whereto` VARCHAR(200) NOT NULL ,
  `personid` VARCHAR(20) NOT NULL ,
  `hhid` INT(11) NOT NULL ,
  `pid` INT(11) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_absencefromhousehold_householdmembers1` (`personid` ASC, `hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_absencefromhousehold_householdmembers1`
    FOREIGN KEY (`personid` , `hhid` , `pid` )
    REFERENCES `householdmembers` (`personid` , `hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `assets`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `assets` (
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
    REFERENCES `households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `assettypes`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `assettypes` (
  `assettype` VARCHAR(100) NOT NULL ,
  PRIMARY KEY (`assettype`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `creditandloans`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `creditandloans` (
  `id` INT(11) NOT NULL ,
  `creditsource` VARCHAR(200) NULL DEFAULT NULL ,
  `unit` VARCHAR(45) NULL DEFAULT NULL ,
  `creditvalue` DOUBLE NULL DEFAULT NULL ,
  `credituse` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `cropincome`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `cropincome` (
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
  `preferenceprice` DOUBLE NULL DEFAULT '100' ,
  `preferenceproduction` DOUBLE NULL DEFAULT '100' ,
  PRIMARY KEY (`id`, `hhid`, `pid`) ,
  INDEX `fk_cropincome_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_cropincome_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `currencies`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `currencies` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `currencyname` VARCHAR(250) NOT NULL ,
  `abbreviation` VARCHAR(45) NOT NULL ,
  `symbol` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `diet`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `diet` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `pid` INT(11) NOT NULL ,
  `fooditem` VARCHAR(45) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  `percentage` DOUBLE NOT NULL ,
  `priceperunit` DOUBLE NOT NULL ,
  `modelprice` DOUBLE NOT NULL DEFAULT 0.0 ,
  PRIMARY KEY (`id`, `pid`) ,
  INDEX `fk_diet_projects1` (`pid` ASC) ,
  CONSTRAINT `fk_diet_projects1`
    FOREIGN KEY (`pid` )
    REFERENCES `projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `employmentincome`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `employmentincome` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hhid` INT(11) NOT NULL ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  `foodtypepaid` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `unitspaid` DOUBLE NULL DEFAULT NULL ,
  `incomekcal` DOUBLE NULL DEFAULT NULL ,
  `cashincome` DOUBLE NULL DEFAULT NULL ,
  `pid` INT(11) NOT NULL ,
  `preferenceincome` DOUBLE NULL DEFAULT '100' ,
  PRIMARY KEY (`id`, `hhid`, `pid`) ,
  INDEX `fk_employmentincome_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_employmentincome_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `expenditure`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `expenditure` (
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
    REFERENCES `households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `globalhouseholdcharacteristics`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `globalhouseholdcharacteristics` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `characteristic` VARCHAR(250) NOT NULL ,
  `datatype` INT(11) NOT NULL ,
  `description` VARCHAR(250) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `globalpersonalcharacteristics`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `globalpersonalcharacteristics` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `characteristic` VARCHAR(250) NULL DEFAULT NULL ,
  `datatype` INT(11) NULL DEFAULT NULL ,
  `description` VARCHAR(250) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `incomeseasonality`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `incomeseasonality` (
  `incometype` VARCHAR(45) NOT NULL ,
  `jan` DOUBLE NOT NULL ,
  `feb` DOUBLE NOT NULL ,
  `mar` DOUBLE NOT NULL ,
  `apr` DOUBLE NOT NULL ,
  `may` DOUBLE NOT NULL ,
  `jun` DOUBLE NOT NULL ,
  `jul` DOUBLE NOT NULL ,
  `aug` DOUBLE NOT NULL ,
  `sep` DOUBLE NOT NULL ,
  `oct` DOUBLE NOT NULL ,
  `nov` DOUBLE NOT NULL ,
  `dec` DOUBLE NOT NULL ,
  PRIMARY KEY (`incometype`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `livestockincome`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `livestockincome` (
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
  `preferenceprice` DOUBLE NULL DEFAULT '100' ,
  `preferenceproduction` DOUBLE NULL DEFAULT '100' ,
  PRIMARY KEY (`id`, `hhid`, `pid`) ,
  INDEX `fk_livestockincome_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_livestockincome_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `lookup_energy_needs`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `lookup_energy_needs` (
  `age` INT(11) NOT NULL ,
  `kCalNeedM` INT(11) NULL DEFAULT NULL ,
  `kCalNeedF` INT(11) NULL DEFAULT NULL ,
  PRIMARY KEY (`age`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `savingscategories`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `savingscategories` (
  `savingscategory` VARCHAR(100) NOT NULL ,
  PRIMARY KEY (`savingscategory`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `setup_crops`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_crops` (
  `foodtype` VARCHAR(100) NOT NULL ,
  `energyvalueperunit` DOUBLE NULL DEFAULT NULL ,
  `measuringunit` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`foodtype`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `setup_employment`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_employment` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `setup_expenditurecategories`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_expenditurecategories` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `expenditurecategory` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `setup_expendituretypes`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_expendituretypes` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `expendituretype` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `setup_landtypes`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_landtypes` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `landtype` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `setup_livestock`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_livestock` (
  `incomesource` VARCHAR(200) NOT NULL DEFAULT '' ,
  `energyvalueperunit` DOUBLE NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`incomesource`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `setup_tradablegoods`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_tradablegoods` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `tradablegoodtype` VARCHAR(200) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `setup_transfers`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_transfers` (
  `assistancetype` VARCHAR(200) NOT NULL ,
  `sourceoftransfer` VARCHAR(200) NOT NULL ,
  `unitofmeasure` VARCHAR(45),
  PRIMARY KEY (`assistancetype`,`sourceoftransfer`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `setup_transfersources`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_transfersources` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `sourcetype` ENUM('Internal','External') NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `setup_treetypes`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_treetypes` (
  `treetype` VARCHAR(100) NOT NULL ,
  `measuringunit` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`treetype`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `setup_foods_crops`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_foods_crops` (
  `name` VARCHAR(200) NOT NULL ,
  `category` VARCHAR(200) NOT NULL ,
  `energyvalueperunit` DOUBLE NULL ,
  `unitofmeasure` VARCHAR(45) NULL ,
  PRIMARY KEY (`name`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `setup_wildfoods`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_wildfoods` (
  `incomesource` VARCHAR(200) NOT NULL DEFAULT '' ,
  `energyvalueperunit` DOUBLE NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`incomesource`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `setup_standardofliving`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_standardofliving` (
  `item` VARCHAR(255) NOT NULL ,
  `type` ENUM('Household','Person','Both') NOT NULL ,
  PRIMARY KEY (`item`) )
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `standardofliving`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `standardofliving` (
  `pid` INT(11) NOT NULL ,
  `summary` VARCHAR(255) NOT NULL ,
  `scope` ENUM('Household','Person') NOT NULL ,
  `gender` ENUM('Male','Female','All') NULL DEFAULT NULL ,
  `agebottom` INT NULL DEFAULT 0 ,
  `agetop` INT NULL DEFAULT 0 ,
  `item` VARCHAR(255) NOT NULL ,
  `costperyear` DOUBLE NOT NULL ,
  `modelprice` DOUBLE NULL DEFAULT 0.0,
  PRIMARY KEY (`pid`, `summary`) ,
  INDEX `fk_standardofliving_projects1` (`pid` ASC) ,
  CONSTRAINT `fk_standardofliving_projects1`
    FOREIGN KEY (`pid` )
    REFERENCES `projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `transfers`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `transfers` (
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
  `preferenceprice` DOUBLE NULL DEFAULT '100' ,
  `preferenceproduction` DOUBLE NULL DEFAULT '100' ,
  PRIMARY KEY (`id`, `hhid`, `pid`) ,
  INDEX `fk_transfers_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_transfers_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `setup_foods_crops`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `setup_foods_crops` (
  `name` VARCHAR(200) NOT NULL ,
  `category` VARCHAR(200) NOT NULL ,
  `energyvalueperunit` DOUBLE NULL ,
  `unitofmeasure` VARCHAR(45) NULL ,
  PRIMARY KEY (`name`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `wildfoods`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `wildfoods` (
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
  `preferenceprice` DOUBLE NULL DEFAULT '100' ,
  `preferenceproduction` DOUBLE NULL DEFAULT '100' ,
  PRIMARY KEY (`id`, `hhid`, `pid`) ,
  INDEX `fk_wildfoods_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_wildfoods_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `transferlog`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `transferlog` (
  `pid` INT(11) NOT NULL ,
  `pid_access` INT(11) NOT NULL ,
  `projectname` VARCHAR(45) NOT NULL ,
  `datecollected` VARCHAR(45) NOT NULL ,
  `currency` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`pid`) ,
  CONSTRAINT `fk_transferlog_projects1`
    FOREIGN KEY (`pid` )
    REFERENCES `projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_swedish_ci;

-- -----------------------------------------------------
-- Table `globalcharacteristics`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `globalcharacteristics` (
  `characteristic` VARCHAR(250) NOT NULL ,
  `chartype` VARCHAR(50) NOT NULL ,
  `datatype` INT(11) NOT NULL ,
  `description` VARCHAR(250) NULL DEFAULT NULL ,
  PRIMARY KEY (`characteristic`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_swedish_ci;

-- -----------------------------------------------------
-- Table `projectcharacteristics`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `projectcharacteristics` (
  `pid` INT(11) NOT NULL ,
  `characteristic` VARCHAR(250) NOT NULL ,
  `chartype` VARCHAR(50) NOT NULL ,
  `datatype` INT(11) NOT NULL ,
  PRIMARY KEY (`pid`, `characteristic`) ,
  CONSTRAINT `fk_projectcharacteristics_projects1`
    FOREIGN KEY (`pid` )
    REFERENCES `projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_swedish_ci;


-- -----------------------------------------------------
-- Table `householdcharacteristics`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `householdcharacteristics` (
  `pid` INT(11) NOT NULL ,
  `hhid` INT(11) NOT NULL ,
  `characteristic` VARCHAR(250) NOT NULL ,
  `charvalue` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`pid`, `hhid`, `characteristic`) ,
  CONSTRAINT `fk_householdcharacteristics_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_swedish_ci;

-- -----------------------------------------------------
-- Table `personalcharacteristics`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `personalcharacteristics` (
  `pid` INT(11) NOT NULL ,
  `hhid` INT(11) NOT NULL ,
  `personid` VARCHAR(20) NOT NULL ,
  `characteristic` VARCHAR(250) NOT NULL ,
  `charvalue` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`pid`, `hhid`, `personid`, `characteristic`) ,
  CONSTRAINT `fk_personalcharacteristics_householdmembers1`
    FOREIGN KEY (`personid` , `hhid` , `pid` )
    REFERENCES `householdmembers` (`personid` , `hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_swedish_ci;

-- -----------------------------------------------------
-- Table `projectassets`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `projectassets` (
  `pid` INT NOT NULL ,
  `assetname` VARCHAR(255) NOT NULL ,
  `assettype` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`pid`, `assetname`) ,
  INDEX `pid` (`pid` ASC) ,
  CONSTRAINT `pid`
    FOREIGN KEY (`pid` )
    REFERENCES `projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `setup_assets`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `setup_assets` (
  `assetname` VARCHAR(255) NOT NULL ,
  `assettype` VARCHAR(50) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`assetname`) )
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Table `dbupdate`
-- -----------------------------------------------------

CREATE  TABLE IF NOT EXISTS `dbupdate` (

  `lastupdate` VARCHAR(50) NOT NULL ,

  PRIMARY KEY (`lastupdate`) );

-- -----------------------------------------------------
-- User `openihm@localhost`
-- -----------------------------------------------------

