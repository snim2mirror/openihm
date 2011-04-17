-- -----------------------------------------------------
-- Table `openihmdb`.`projectincomesources`
-- -----------------------------------------------------
USE `openihmdb`;

ALTER TABLE `openihmdb`.`projectincomesources` DROP PRIMARY KEY,
 ADD PRIMARY KEY  USING BTREE(`incomesource`, `pid`, `incometype`);