SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

-- -----------------------------------------------------
-- Table `openihmdb`.`householdmembers`
-- -----------------------------------------------------

ALTER TABLE `openihmdb`.`householdmembers` ADD COLUMN `periodaway` INT(11) NULL DEFAULT 0  AFTER `pid` , 
ADD COLUMN `reason` VARCHAR(200) NULL DEFAULT NULL  AFTER `periodaway` , 
ADD COLUMN `whereto` VARCHAR(200) NULL DEFAULT NULL  AFTER `reason` ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
