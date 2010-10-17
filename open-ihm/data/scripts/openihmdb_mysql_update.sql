SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

USE `openihmdb`;

DELETE FROM `openihmdb`.`householdmembers`;

ALTER TABLE `openihmdb`.`householdmembers` CHANGE COLUMN `dateofbirth` `yearofbirth` INT(11) NOT NULL  , 
CHANGE COLUMN `education` `education` VARCHAR(200) NULL DEFAULT NULL  ;

ALTER TABLE `openihmdb`.`cropincome` ADD COLUMN `otheruses` DOUBLE NULL DEFAULT 0  AFTER `unitprice` ,
ADD COLUMN `unitsproduced` DOUBLE NULL DEFAULT 0  AFTER `unitsconsumed`;

ALTER TABLE `openihmdb`.`cropincome`
CHANGE COLUMN `unitsconsumed` `unitsconsumed` DOUBLE NULL DEFAULT 0  AFTER `otheruses` ;

ALTER TABLE `openihmdb`.`livestockincome` ADD COLUMN `otheruses` DOUBLE NULL DEFAULT 0  AFTER `unitprice` ,
ADD COLUMN `unitsproduced` DOUBLE NULL DEFAULT 0  AFTER `unitsconsumed`;

ALTER TABLE `openihmdb`.`livestockincome`
CHANGE COLUMN `unitsconsumed` `unitsconsumed` DOUBLE NULL DEFAULT 0  AFTER `otheruses` ;

ALTER TABLE `openihmdb`.`wildfoods` ADD COLUMN `otheruses` DOUBLE NULL DEFAULT 0  AFTER `unitprice` ,
ADD COLUMN `unitsproduced` DOUBLE NULL DEFAULT 0  AFTER `unitsconsumed`;

ALTER TABLE `openihmdb`.`wildfoods`
CHANGE COLUMN `unitsconsumed` `unitsconsumed` DOUBLE NULL DEFAULT 0  AFTER `otheruses` ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

