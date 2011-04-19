SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

CREATE SCHEMA IF NOT EXISTS `openihmdb` DEFAULT CHARACTER SET latin1 ;
USE `openihmdb`;

-- -----------------------------------------------------
-- Table `openihmdb`.`projects`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`projects` (
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
-- Table `openihmdb`.`projectincomesources`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`projectincomesources` (
  `pid` INT(11) NOT NULL ,
  `incomesource` VARCHAR(255) NOT NULL ,
  `incometype` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`incomesource`, `pid`, `incometype`) ,
  INDEX `fk_projectincomesources_projects` (`pid` ASC) ,
  CONSTRAINT `fk_projectincomesources_projects`
    FOREIGN KEY (`pid` )
    REFERENCES `openihmdb`.`projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openihmdb`.`households`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`households` (
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
    REFERENCES `openihmdb`.`projects` (`pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`householdmembers`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`householdmembers` (
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
    REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`absencefromhousehold`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`absencefromhousehold` (
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
    REFERENCES `openihmdb`.`householdmembers` (`personid` , `hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`assets`
-- -----------------------------------------------------
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
-- Table `openihmdb`.`assettypes`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`assettypes` (
  `assettype` VARCHAR(100) NOT NULL ,
  PRIMARY KEY (`assettype`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`creditandloans`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`creditandloans` (
  `id` INT(11) NOT NULL ,
  `creditsource` VARCHAR(200) NULL DEFAULT NULL ,
  `unit` VARCHAR(45) NULL DEFAULT NULL ,
  `creditvalue` DOUBLE NULL DEFAULT NULL ,
  `credituse` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`cropincome`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`cropincome` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hhid` INT(11) NOT NULL ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `unitsconsumed` DOUBLE NULL DEFAULT NULL ,
  `unitssold` DOUBLE NULL DEFAULT NULL ,
  `unitprice` DOUBLE NULL DEFAULT NULL ,
  `pid` INT(11) NOT NULL ,
  PRIMARY KEY (`id`, `hhid`, `pid`) ,
  INDEX `fk_cropincome_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_cropincome_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`currencies`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`currencies` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `currencyname` VARCHAR(250) NOT NULL ,
  `abbreviation` VARCHAR(45) NOT NULL ,
  `symbol` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`diet`
-- -----------------------------------------------------
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
-- Table `openihmdb`.`employmentincome`
-- -----------------------------------------------------
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
-- Table `openihmdb`.`expenditure`
-- -----------------------------------------------------
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


-- -----------------------------------------------------
-- Table `openihmdb`.`globalhouseholdcharacteristics`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`globalhouseholdcharacteristics` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `characteristic` VARCHAR(250) NOT NULL ,
  `datatype` INT(11) NOT NULL ,
  `description` VARCHAR(250) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`globalpersonalcharacteristics`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`globalpersonalcharacteristics` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `characteristic` VARCHAR(250) NULL DEFAULT NULL ,
  `datatype` INT(11) NULL DEFAULT NULL ,
  `description` VARCHAR(250) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`incomeseasonality`
-- -----------------------------------------------------
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
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`livestockincome`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`livestockincome` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hhid` INT(11) NOT NULL ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `unitsconsumed` DOUBLE NULL DEFAULT NULL ,
  `unitssold` DOUBLE NULL DEFAULT NULL ,
  `unitprice` DOUBLE NULL DEFAULT NULL ,
  `pid` INT(11) NOT NULL ,
  PRIMARY KEY (`id`, `hhid`, `pid`) ,
  INDEX `fk_livestockincome_households1` (`hhid` ASC, `pid` ASC) ,
  CONSTRAINT `fk_livestockincome_households1`
    FOREIGN KEY (`hhid` , `pid` )
    REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `openihmdb`.`lookup_energy_needs`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`lookup_energy_needs` (
  `age` INT(11) NOT NULL ,
  `kCalNeedM` INT(11) NULL DEFAULT NULL ,
  `kCalNeedF` INT(11) NULL DEFAULT NULL ,
  PRIMARY KEY (`age`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `openihmdb`.`savingscategories`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`savingscategories` (
  `savingscategory` VARCHAR(100) NOT NULL ,
  PRIMARY KEY (`savingscategory`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_crops`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_crops` (
  `foodtype` VARCHAR(100) NOT NULL ,
  `energyvalueperunit` DOUBLE NULL DEFAULT NULL ,
  `measuringunit` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`foodtype`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_employment`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_employment` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_expenditurecategories`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_expenditurecategories` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `expenditurecategory` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_expendituretypes`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_expendituretypes` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `expendituretype` VARCHAR(200) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_landtypes`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_landtypes` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `landtype` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_livestock`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_livestock` (
  `incomesource` VARCHAR(200) NOT NULL DEFAULT '' ,
  `energyvalueperunit` DOUBLE NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`incomesource`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_tradablegoods`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_tradablegoods` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `tradablegoodtype` VARCHAR(200) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_transfers`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_transfers` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `assistancetype` VARCHAR(200) NOT NULL ,
  `unitofmeasure` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_transfersources`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_transfersources` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `sourcetype` ENUM('Internal','External') NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openihmdb`.`setup_treetypes`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_treetypes` (
  `treetype` VARCHAR(100) NOT NULL ,
  `measuringunit` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`treetype`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `openihmdb`.`setup_foods_crops`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_foods_crops` (
  `name` VARCHAR(200) NOT NULL ,
  `category` VARCHAR(200) NOT NULL ,
  `energyvalueperunit` DOUBLE NULL ,
  `unitofmeasure` VARCHAR(45) NULL ,
  PRIMARY KEY (`name`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `openihmdb`.`setup_wildfoods`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_wildfoods` (
  `incomesource` VARCHAR(200) NOT NULL DEFAULT '' ,
  `energyvalueperunit` DOUBLE NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`incomesource`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

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


-- -----------------------------------------------------
-- Table `openihmdb`.`transfers`
-- -----------------------------------------------------
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
-- Table `openihmdb`.`setup_foods_crops`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`setup_foods_crops` (
  `name` VARCHAR(200) NOT NULL ,
  `category` VARCHAR(200) NOT NULL ,
  `energyvalueperunit` DOUBLE NULL ,
  `unitofmeasure` VARCHAR(45) NULL ,
  PRIMARY KEY (`name`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `openihmdb`.`wildfoods`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `openihmdb`.`wildfoods` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hhid` INT(11) NOT NULL ,
  `incomesource` VARCHAR(200) NULL DEFAULT NULL ,
  `unitofmeasure` VARCHAR(45) NULL DEFAULT NULL ,
  `unitsconsumed` DOUBLE NULL DEFAULT NULL ,
  `unitssold` DOUBLE NULL DEFAULT NULL ,
  `unitprice` DOUBLE NULL DEFAULT NULL ,
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

-- -----------------------------------------------------
-- User `openihm@localhost`
-- -----------------------------------------------------

GRANT ALL ON openihmdb.* TO openihm@localhost IDENTIFIED BY 'ihm2010'; 
