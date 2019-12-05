-- MySQL Script generated by MySQL Workbench
-- dom 01 dic 2019 01:58:37 CET
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Langues`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Langues` (
  `upsid` INT NOT NULL,
  `nom` TEXT NOT NULL,
  `biblio` TEXT NULL,
  PRIMARY KEY (`upsid`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Phonemes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Phonemes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `IPA` TEXT NOT NULL,
  `description` TEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Phonemes_Langues`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Phonemes_Langues` (
  `upsid` INT NOT NULL,
  `phoneme` INT NOT NULL,
  INDEX `upsid_idx` (`upsid` ASC),
  INDEX `IPA_idx` (`phoneme` ASC),
  PRIMARY KEY (`upsid`, `phoneme`),
  CONSTRAINT `upsid`
    FOREIGN KEY (`upsid`)
    REFERENCES `mydb`.`Langues` (`upsid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `IPA`
    FOREIGN KEY (`phoneme`)
    REFERENCES `mydb`.`Phonemes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Branches`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Branches` (
  `famille` TEXT NOT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Langues_Branches`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Langues_Branches` (
  `famille` INT NOT NULL,
  `upsid` INT NOT NULL,
  PRIMARY KEY (`famille`, `upsid`),
  INDEX `upsid_fk_idx` (`upsid` ASC),
  INDEX `index3` (`famille` ASC),
  CONSTRAINT `famille_fk`
    FOREIGN KEY (`famille`)
    REFERENCES `mydb`.`Branches` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `upsid_fk`
    FOREIGN KEY (`upsid`)
    REFERENCES `mydb`.`Langues` (`upsid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
