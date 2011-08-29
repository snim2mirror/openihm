SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

USE `openihmdb`;

DELETE FROM `openihmdb`.`projects`;
DELETE FROM `openihmdb`.`households`;
DELETE FROM `openihmdb`.`householdmembers`;
DELETE FROM `openihmdb`.`expenditure`;
DELETE FROM `openihmdb`.`transfers`;
DELETE FROM `openihmdb`.`wildfoods`;
DELETE FROM `openihmdb`.`employmentincome`;
DELETE FROM `openihmdb`.`livestockincome`;
DELETE FROM `openihmdb`.`cropincome`;
DELETE FROM `openihmdb`.`assets`;

ALTER TABLE `openihmdb`.`households` DROP FOREIGN KEY `fk_household_projects` ;

ALTER TABLE `openihmdb`.`households` 
  ADD CONSTRAINT `fk_households_projects1`
  FOREIGN KEY (`pid` )
  REFERENCES `openihmdb`.`projects` (`pid` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, ADD INDEX `fk_households_projects1` (`pid` ASC) 
, DROP INDEX `fk_household_projects` 
, DROP PRIMARY KEY 
, ADD PRIMARY KEY (`hhid`, `pid`) ;

ALTER TABLE `openihmdb`.`absencefromhousehold` ADD COLUMN `pid` INT(11) NOT NULL  AFTER `hhid` , DROP FOREIGN KEY `fk_absencefromhousehold_householdmembers1` ;

ALTER TABLE `openihmdb`.`assets` ADD COLUMN `pid` INT(11) NOT NULL  AFTER `totalunits` , CHANGE COLUMN `hhid` `hhid` INT(11) NOT NULL  AFTER `assetid` , DROP FOREIGN KEY `fk_assets_households1` ;

ALTER TABLE `openihmdb`.`cropincome` ADD COLUMN `pid` INT(11) NOT NULL  AFTER `unitprice` , DROP FOREIGN KEY `fk_cropincome_households1` ;

ALTER TABLE `openihmdb`.`employmentincome` ADD COLUMN `pid` INT(11) NOT NULL  AFTER `cashincome` , DROP FOREIGN KEY `fk_employmentincome_households1` ;

ALTER TABLE `openihmdb`.`expenditure` ADD COLUMN `pid` INT(11) NOT NULL  AFTER `totalunits` , CHANGE COLUMN `hhid` `hhid` INT(11) NOT NULL  AFTER `expid` , DROP FOREIGN KEY `fk_expenditure_households1` ;

ALTER TABLE `openihmdb`.`householdmembers` ADD COLUMN `pid` INT(11) NOT NULL  AFTER `education` , CHANGE COLUMN `hhid` `hhid` INT(11) NOT NULL  AFTER `personid` , DROP FOREIGN KEY `fk_householdmembers_households1` ;

ALTER TABLE `openihmdb`.`livestockincome` ADD COLUMN `pid` INT(11) NOT NULL  AFTER `unitprice` , DROP FOREIGN KEY `fk_livestockincome_households1` ;

ALTER TABLE `openihmdb`.`transfers` ADD COLUMN `pid` INT(11) NOT NULL  AFTER `cashperyear` , DROP FOREIGN KEY `fk_transfers_households1` ;

ALTER TABLE `openihmdb`.`wildfoods` ADD COLUMN `pid` INT(11) NOT NULL  AFTER `unitprice` 
, DROP PRIMARY KEY 
, ADD PRIMARY KEY (`id`, `hhid`, `pid`) 
, DROP INDEX `fk_wildfoods_households1` 
, ADD INDEX `fk_wildfoods_households1` (`hhid` ASC, `pid` ASC) ;

ALTER TABLE `openihmdb`.`assets` 
  ADD CONSTRAINT `fk_assets_households1`
  FOREIGN KEY (`hhid` , `pid` )
  REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, DROP PRIMARY KEY 
, ADD PRIMARY KEY (`assetid`, `hhid`, `pid`) 
, DROP INDEX `fk_assets_households1` 
, ADD INDEX `fk_assets_households1` (`hhid` ASC, `pid` ASC) ;

ALTER TABLE `openihmdb`.`cropincome` 
  ADD CONSTRAINT `fk_cropincome_households1`
  FOREIGN KEY (`hhid` , `pid` )
  REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, DROP PRIMARY KEY 
, ADD PRIMARY KEY (`id`, `hhid`, `pid`) 
, DROP INDEX `fk_cropincome_households1` 
, ADD INDEX `fk_cropincome_households1` (`hhid` ASC, `pid` ASC) ;

ALTER TABLE `openihmdb`.`employmentincome` 
  ADD CONSTRAINT `fk_employmentincome_households1`
  FOREIGN KEY (`hhid` , `pid` )
  REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, DROP PRIMARY KEY 
, ADD PRIMARY KEY (`id`, `hhid`, `pid`) 
, DROP INDEX `fk_employmentincome_households1` 
, ADD INDEX `fk_employmentincome_households1` (`hhid` ASC, `pid` ASC) ;

ALTER TABLE `openihmdb`.`expenditure` 
  ADD CONSTRAINT `fk_expenditure_households1`
  FOREIGN KEY (`hhid` , `pid` )
  REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, DROP PRIMARY KEY 
, ADD PRIMARY KEY (`expid`, `hhid`, `pid`) 
, DROP INDEX `fk_expenditure_households1` 
, ADD INDEX `fk_expenditure_households1` (`hhid` ASC, `pid` ASC) ;

ALTER TABLE `openihmdb`.`householdmembers` 
  ADD CONSTRAINT `fk_householdmembers_households1`
  FOREIGN KEY (`hhid` , `pid` )
  REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, DROP PRIMARY KEY 
, ADD PRIMARY KEY (`personid`, `hhid`, `pid`) 
, DROP INDEX `fk_householdmembers_households1` 
, ADD INDEX `fk_householdmembers_households1` (`hhid` ASC, `pid` ASC) ;

ALTER TABLE `openihmdb`.`absencefromhousehold` 
  ADD CONSTRAINT `fk_absencefromhousehold_householdmembers1`
  FOREIGN KEY (`personid` , `hhid` , `pid` )
  REFERENCES `openihmdb`.`householdmembers` (`personid` , `hhid` , `pid` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, DROP INDEX `fk_absencefromhousehold_householdmembers1` 
, ADD INDEX `fk_absencefromhousehold_householdmembers1` (`personid` ASC, `hhid` ASC, `pid` ASC) ;

ALTER TABLE `openihmdb`.`livestockincome` 
  ADD CONSTRAINT `fk_livestockincome_households1`
  FOREIGN KEY (`hhid` , `pid` )
  REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, DROP PRIMARY KEY 
, ADD PRIMARY KEY (`id`, `hhid`, `pid`) 
, DROP INDEX `fk_livestockincome_households1` 
, ADD INDEX `fk_livestockincome_households1` (`hhid` ASC, `pid` ASC) ;

ALTER TABLE `openihmdb`.`transfers` 
  ADD CONSTRAINT `fk_transfers_households1`
  FOREIGN KEY (`hhid` , `pid` )
  REFERENCES `openihmdb`.`households` (`hhid` , `pid` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, DROP PRIMARY KEY 
, ADD PRIMARY KEY (`id`, `hhid`, `pid`) 
, DROP INDEX `fk_transfers_households1` 
, ADD INDEX `fk_transfers_households1` (`hhid` ASC, `pid` ASC) ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
