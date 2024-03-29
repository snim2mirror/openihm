SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

CREATE SCHEMA IF NOT EXISTS `openihmdb` ;
USE `openihmdb`;

-- -----------------------------------------------------
-- Table `openihmdb`.`projects`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`projects` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`projects` (
  `pid` INT NOT NULL AUTO_INCREMENT ,
  `projectname` VARCHAR(100) NOT NULL ,
  `startdate` DATE NOT NULL ,
  `enddate` DATE NOT NULL ,
  `description` TEXT NOT NULL ,
  `currency` TEXT NOT NULL ,
  PRIMARY KEY (`pid`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`households`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`households` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`households` (
  `hhid` INT NOT NULL ,
  `householdname` VARCHAR(100) NOT NULL ,
  `totalassetvalue` DOUBLE NOT NULL DEFAULT 0 ,
  `totalincomevalue` DOUBLE NOT NULL DEFAULT 0 ,
  `totalexpenditure` DOUBLE NOT NULL DEFAULT 0 ,
  `dateofcollection` DATE NOT NULL ,
  `pid` INT NOT NULL ,
  PRIMARY KEY (`hhid`) ,
  INDEX `fk_household_projects` (`pid` ASC) ,
  CONSTRAINT `fk_household_projects`
    FOREIGN KEY (`pid` )
    REFERENCES `openihmdb`.`projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`expenditure`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`expenditure` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`expenditure` (
  `hhid` INT NOT NULL ,
  `expid` INT NOT NULL AUTO_INCREMENT ,
  `exptype` VARCHAR(100) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `priceperunit` DOUBLE NULL DEFAULT NULL ,
  `kcalperunit` DOUBLE NULL DEFAULT NULL ,
  `totalunits` DOUBLE NULL DEFAULT NULL ,
  PRIMARY KEY (`expid`, `hhid`) ,
  INDEX `fk_expenditure_households1` (`hhid` ASC) ,
  CONSTRAINT `fk_expenditure_households1`
    FOREIGN KEY (`hhid` )
    REFERENCES `openihmdb`.`households` (`hhid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`assets`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`assets` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`assets` (
  `hhid` INT NOT NULL ,
  `assetid` INT NOT NULL AUTO_INCREMENT ,
  `assettype` VARCHAR(100) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  `unitcost` DOUBLE NOT NULL ,
  `totalunits` DOUBLE NOT NULL ,
  PRIMARY KEY (`assetid`, `hhid`) ,
  INDEX `fk_assets_households1` (`hhid` ASC) ,
  CONSTRAINT `fk_assets_households1`
    FOREIGN KEY (`hhid` )
    REFERENCES `openihmdb`.`households` (`hhid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`householdmembers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`householdmembers` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`householdmembers` (
  `hhid` INT NOT NULL ,
  `personid` VARCHAR(20) NOT NULL ,
  `headofhousehold` ENUM('Yes','No') NOT NULL ,
  `dateofbirth` DATE NOT NULL ,
  `sex` ENUM('Male','Female') NOT NULL ,
  `education` VARCHAR(200) NOT NULL ,
  PRIMARY KEY (`personid`, `hhid`) ,
  INDEX `fk_householdmembers_households1` (`hhid` ASC) ,
  CONSTRAINT `fk_householdmembers_households1`
    FOREIGN KEY (`hhid` )
    REFERENCES `openihmdb`.`households` (`hhid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`absencefromhousehold`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`absencefromhousehold` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`absencefromhousehold` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `percentageaway` DOUBLE NOT NULL ,
  `reason` VARCHAR(200) NOT NULL ,
  `whereto` VARCHAR(200) NOT NULL ,
  `personid` VARCHAR(20) NOT NULL ,
  `hhid` INT NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_absencefromhousehold_householdmembers1` (`personid` ASC, `hhid` ASC) ,
  CONSTRAINT `fk_absencefromhousehold_householdmembers1`
    FOREIGN KEY (`personid` , `hhid` )
    REFERENCES `openihmdb`.`householdmembers` (`personid` , `hhid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`diet`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`diet` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`diet` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `fooditem` VARCHAR(45) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  `percentage` DOUBLE NOT NULL ,
  `priceperunit` DOUBLE NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`standardofliving`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`standardofliving` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`standardofliving` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `item` VARCHAR(45) NOT NULL ,
  `usedby` ENUM('Male','Female','All') NOT NULL ,
  `agegroup` VARCHAR(45) NOT NULL ,
  `cost` DOUBLE NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`assettypes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`assettypes` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`assettypes` (
  `assettype` VARCHAR(100) NOT NULL ,
  PRIMARY KEY (`assettype`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`savingscategories`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`savingscategories` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`savingscategories` (
  `savingscategory` VARCHAR(100) NOT NULL ,
  PRIMARY KEY (`savingscategory`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`currencies`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`currencies` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`currencies` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `currencyname` VARCHAR(250) NOT NULL ,
  `abbreviation` VARCHAR(45) NOT NULL ,
  `symbol` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`globalhouseholdcharacteristics`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`globalhouseholdcharacteristics` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`globalhouseholdcharacteristics` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `characteristic` VARCHAR(250) NOT NULL ,
  `datatype` INT NOT NULL ,
  `description` VARCHAR(250) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`globalpersonalcharacteristics`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`globalpersonalcharacteristics` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`globalpersonalcharacteristics` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `characteristic` VARCHAR(250) NULL DEFAULT NULL ,
  `datatype` INT NULL DEFAULT NULL ,
  `description` VARCHAR(250) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`creditandloans`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`creditandloans` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`creditandloans` (
  `id` INT NOT NULL ,
  `creditsource` VARCHAR(200) NULL DEFAULT NULL ,
  `unit` VARCHAR(45) NULL DEFAULT NULL ,
  `creditvalue` DOUBLE NULL DEFAULT NULL ,
  `credituse` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`transfers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`transfers` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`transfers` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `hhid` INT NOT NULL ,
  `assistancetype` VARCHAR(200) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  `sourcetype` ENUM('Internal','External') NOT NULL ,
  `foodperdistribution` DOUBLE NULL DEFAULT NULL ,
  `cashperdistribution` DOUBLE NULL DEFAULT NULL ,
  `numberoftimesreceived` INT NULL DEFAULT NULL ,
  `unitsconsumed` DOUBLE NULL DEFAULT NULL ,
  `cashperyear` DOUBLE NULL DEFAULT NULL ,
  PRIMARY KEY (`id`, `hhid`) ,
  INDEX `fk_transfers_households1` (`hhid` ASC) ,
  CONSTRAINT `fk_transfers_households1`
    FOREIGN KEY (`hhid` )
    REFERENCES `openihmdb`.`households` (`hhid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`employmentincome`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`employmentincome` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`employmentincome` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `hhid` INT NOT NULL ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  `foodtypepaid` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `unitspaid` DOUBLE NULL DEFAULT NULL ,
  `incomekcal` DOUBLE NULL DEFAULT NULL ,
  `cashincome` DOUBLE NULL DEFAULT NULL ,
  PRIMARY KEY (`id`, `hhid`) ,
  INDEX `fk_employmentincome_households1` (`hhid` ASC) ,
  CONSTRAINT `fk_employmentincome_households1`
    FOREIGN KEY (`hhid` )
    REFERENCES `openihmdb`.`households` (`hhid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`livestockincome`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`livestockincome` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`livestockincome` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `hhid` INT NOT NULL ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `unitsconsumed` DOUBLE NULL DEFAULT NULL ,
  `unitssold` DOUBLE NULL DEFAULT NULL ,
  `unitprice` DOUBLE NULL DEFAULT NULL ,
  PRIMARY KEY (`id`, `hhid`) ,
  INDEX `fk_livestockincome_households1` (`hhid` ASC) ,
  CONSTRAINT `fk_livestockincome_households1`
    FOREIGN KEY (`hhid` )
    REFERENCES `openihmdb`.`households` (`hhid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`cropincome`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`cropincome` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`cropincome` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `hhid` INT NOT NULL ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `unitsconsumed` DOUBLE NULL DEFAULT NULL ,
  `unitssold` DOUBLE NULL DEFAULT NULL ,
  `unitprice` DOUBLE NULL DEFAULT NULL ,
  PRIMARY KEY (`id`, `hhid`) ,
  INDEX `fk_cropincome_households1` (`hhid` ASC) ,
  CONSTRAINT `fk_cropincome_households1`
    FOREIGN KEY (`hhid` )
    REFERENCES `openihmdb`.`households` (`hhid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_transfers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`setup_transfers` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_transfers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `assistancetype` VARCHAR(200) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_transfersources`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`setup_transfersources` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_transfersources` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `sourcetype` ENUM('Internal','External') NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_crops`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`setup_crops` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_crops` (
  `foodtype` VARCHAR(100) NOT NULL ,
  `energyvalueperunit` DOUBLE NULL DEFAULT NULL ,
  `measuringunit` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`foodtype`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`lookup_energy_needs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`lookup_energy_needs` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`lookup_energy_needs` (
  `age` INT NOT NULL ,
  `kCalNeedM` INT DEFAULT NULL,
  `kCalNeedF` INT DEFAULT NULL,
  PRIMARY KEY (age) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_treetypes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`setup_treetypes` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_treetypes` (
  `treetype` VARCHAR(100) NOT NULL ,
  `measuringunit` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`treetype`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_employment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`setup_employment` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_employment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_expenditurecategories`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`setup_expenditurecategories` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_expenditurecategories` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `expenditurecategory` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_expendituretypes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`setup_expendituretypes` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_expendituretypes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `expendituretype` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_livestock`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`setup_livestock` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_livestock` (
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  `energyvalueperunit` DOUBLE NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`incomesource`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_landtypes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`setup_landtypes` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_landtypes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `landtype` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_tradablegoods`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`setup_tradablegoods` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_tradablegoods` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `tradablegoodtype` VARCHAR(200) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`wildfoods`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`wildfoods` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`wildfoods` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `hhid` INT NOT NULL ,
  `incomesource` VARCHAR(200) NULL ,
  `unitofmeasure` VARCHAR(45) NULL ,
  `unitsconsumed` DOUBLE NULL ,
  `unitssold` DOUBLE NULL ,
  `unitprice` DOUBLE NULL ,
  PRIMARY KEY (`id`, `hhid`) ,
  INDEX `fk_wildfoods_households1` (`hhid` ASC) ,
  CONSTRAINT `fk_wildfoods_households1`
    FOREIGN KEY (`hhid` )
    REFERENCES `openihmdb`.`households` (`hhid` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_wildfoods`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`setup_wildfoods` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_wildfoods` (
  `incomesource` VARCHAR(200) NULL ,
  `energyvalueperunit` DOUBLE NULL ,
  `unitofmeasure` VARCHAR(45) NULL ,
  PRIMARY KEY (`incomesource`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`incomeseasonality`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openihmdb`.`incomeseasonality` ;

CREATE  TABLE IF NOT EXISTS `openihmdb`.`incomeseasonality` (
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
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- User `openihm@localhost`
-- -----------------------------------------------------

GRANT ALL ON openihmdb.* TO openihm@localhost IDENTIFIED BY 'ihm2010';