-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema SPFCdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema SPFCdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SPFCdb` DEFAULT CHARACTER SET utf8 ;
USE `SPFCdb` ;

-- -----------------------------------------------------
-- Users
-- -----------------------------------------------------
CREATE user 'albin'@'localhost' identified by 'password';
CREATE user 'marco'@'localhost' identified by 'password';
CREATE user 'oscar'@'localhost' identified by 'password';

GRANT ALL PRIVILEGES ON SPFCdb.* TO albin@localhost;
GRANT ALL PRIVILEGES ON SPFCdb.* TO marco@localhost;
GRANT ALL PRIVILEGES ON SPFCdb.* TO oscar@localhost;

-- -----------------------------------------------------
-- Table `SPFCdb`.`Storage`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Storage` (
  `idstorage` INT NOT NULL,
  `adress` VARCHAR(45) NOT NULL,
  `zipcode` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idstorage`),
  UNIQUE INDEX `location_adress_UNIQUE` (`adress` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`product_stored`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`product_stored` (
  `idproduct_stored` INT NOT NULL AUTO_INCREMENT,
  `product_stored` INT NOT NULL,
  `product_min_limit` INT NOT NULL,
  `products_max_limit` INT NOT NULL,
  `Storage_idstorage` INT NOT NULL,
  PRIMARY KEY (`idproduct_stored`),
  INDEX `fk_product_stored_Storage1_idx` (`Storage_idstorage` ASC) VISIBLE,
  CONSTRAINT `fk_product_stored_Storage1`
    FOREIGN KEY (`Storage_idstorage`)
    REFERENCES `SPFCdb`.`Storage` (`idstorage`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`component_model`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`component_model` (
  `idcomponent_model` INT NOT NULL,
  `car_brand` VARCHAR(45) NOT NULL,
  `car_model` VARCHAR(45) NOT NULL,
  `car_model_year` YEAR NULL,
  PRIMARY KEY (`idcomponent_model`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Products` (
  `idProducts` INT NOT NULL,
  `product_name` VARCHAR(100) NOT NULL,
  `product_number` CHAR(10) NOT NULL,
  `description` VARCHAR(500) NULL,
  `sell_price` FLOAT NOT NULL,
  `product_stored_idproduct_stored` INT NOT NULL,
  `component_model_idcomponent_model` INT NOT NULL,
  PRIMARY KEY (`idProducts`),
  UNIQUE INDEX `product_barcode_UNIQUE` (`product_number` ASC) VISIBLE,
  INDEX `fk_Products_product_stored1_idx` (`product_stored_idproduct_stored` ASC) VISIBLE,
  INDEX `fk_Products_component_model1_idx` (`component_model_idcomponent_model` ASC) VISIBLE,
  CONSTRAINT `fk_Products_product_stored1`
    FOREIGN KEY (`product_stored_idproduct_stored`)
    REFERENCES `SPFCdb`.`product_stored` (`idproduct_stored`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Products_component_model1`
    FOREIGN KEY (`component_model_idcomponent_model`)
    REFERENCES `SPFCdb`.`component_model` (`idcomponent_model`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Manufactures`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Manufactures` (
  `idManufactures` INT NOT NULL,
  `company_name` VARCHAR(45) NOT NULL,
  `number_head_office` INT GENERATED ALWAYS AS (1),
  PRIMARY KEY (`idManufactures`),
  UNIQUE INDEX `company_name_UNIQUE` (`company_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Manufactures_offices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Manufactures_offices` (
  `idManufactures_offices` INT NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `zipcode` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `Manufactures_idManufactures` INT NOT NULL,
  PRIMARY KEY (`idManufactures_offices`),
  INDEX `fk_Manufactures_offices_Manufactures1_idx` (`Manufactures_idManufactures` ASC) VISIBLE,
  UNIQUE INDEX `phone_UNIQUE` (`phone` ASC) VISIBLE,
  CONSTRAINT `fk_Manufactures_offices_Manufactures1`
    FOREIGN KEY (`Manufactures_idManufactures`)
    REFERENCES `SPFCdb`.`Manufactures` (`idManufactures`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Manufactures_contact_person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Manufactures_contact_person` (
  `idManufactures_contact_person` INT NOT NULL,
  `phone_number` VARCHAR(45) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `Manufactures_idManufactures` INT NOT NULL,
  `Manufactures_offices_idManufactures_offices` INT NULL,
  PRIMARY KEY (`idManufactures_contact_person`),
  INDEX `fk_Manufactures_contact_person_Manufactures1_idx` (`Manufactures_idManufactures` ASC) VISIBLE,
  UNIQUE INDEX `phone_number_UNIQUE` (`phone_number` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  INDEX `fk_Manufactures_contact_person_Manufactures_offices1_idx` (`Manufactures_offices_idManufactures_offices` ASC) VISIBLE,
  CONSTRAINT `fk_Manufactures_contact_person_Manufactures1`
    FOREIGN KEY (`Manufactures_idManufactures`)
    REFERENCES `SPFCdb`.`Manufactures` (`idManufactures`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Manufactures_contact_person_Manufactures_offices1`
    FOREIGN KEY (`Manufactures_offices_idManufactures_offices`)
    REFERENCES `SPFCdb`.`Manufactures_offices` (`idManufactures_offices`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Products_has_Manufactures`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Products_has_Manufactures` (
  `Products_idProducts` INT NOT NULL,
  `Manufactures_idManufactures` INT NOT NULL,
  `purchase_price` FLOAT GENERATED ALWAYS AS (0),
  `quality_rating` INT NULL,
  PRIMARY KEY (`Products_idProducts`, `Manufactures_idManufactures`),
  INDEX `fk_Products_has_Manufactures_Manufactures1_idx` (`Manufactures_idManufactures` ASC) VISIBLE,
  INDEX `fk_Products_has_Manufactures_Products1_idx` (`Products_idProducts` ASC) VISIBLE,
  CONSTRAINT `fk_Products_has_Manufactures_Products1`
    FOREIGN KEY (`Products_idProducts`)
    REFERENCES `SPFCdb`.`Products` (`idProducts`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Products_has_Manufactures_Manufactures1`
    FOREIGN KEY (`Manufactures_idManufactures`)
    REFERENCES `SPFCdb`.`Manufactures` (`idManufactures`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Company`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Company` (
  `idContactPersons` INT NOT NULL,
  `company_name` VARCHAR(45) NOT NULL,
  `phone_number` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idContactPersons`),
  UNIQUE INDEX `phone_number_UNIQUE` (`phone_number` ASC) VISIBLE,
  UNIQUE INDEX `idContactPersons_UNIQUE` (`idContactPersons` ASC) VISIBLE,
  UNIQUE INDEX `company_name_UNIQUE` (`company_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`offices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`offices` (
  `idoffices` INT NOT NULL,
  `city` VARCHAR(100) NOT NULL,
  `phone_number` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(100) NOT NULL,
  `state` VARCHAR(100) NOT NULL,
  `country` VARCHAR(100) NOT NULL,
  `zipcode` INT NOT NULL,
  `Storage_idOffice_storage` INT NOT NULL,
  PRIMARY KEY (`idoffices`),
  INDEX `fk_offices_Storage1_idx` (`Storage_idOffice_storage` ASC) VISIBLE,
  CONSTRAINT `fk_offices_Storage1`
    FOREIGN KEY (`Storage_idOffice_storage`)
    REFERENCES `SPFCdb`.`Storage` (`idstorage`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Employees` (
  `idEmployees` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `Jobtitle` VARCHAR(45) NULL,
  `offices_idoffices` INT NOT NULL,
  `boss` INT NOT NULL,
  PRIMARY KEY (`idEmployees`),
  INDEX `fk_Employees_offices1_idx` (`offices_idoffices` ASC) VISIBLE,
  INDEX `fk_Employees_Employees1_idx` (`boss` ASC) VISIBLE,
  UNIQUE INDEX `idEmployees_UNIQUE` (`idEmployees` ASC) VISIBLE,
  CONSTRAINT `fk_Employees_offices1`
    FOREIGN KEY (`offices_idoffices`)
    REFERENCES `SPFCdb`.`offices` (`idoffices`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Employees_Employees1`
    FOREIGN KEY (`boss`)
    REFERENCES `SPFCdb`.`Employees` (`idEmployees`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`private_person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`private_person` (
  `idprivate_person` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idprivate_person`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`delivery_adress`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`delivery_adress` (
  `iddelivery_adress` INT NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `zipcode` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`iddelivery_adress`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Customers` (
  `idCustomers` INT NOT NULL,
  `created` DATE NOT NULL,
  `private_person_or_company` TINYINT NOT NULL,
  `Company_idContactPersons` INT NULL,
  `Employees_idEmployees` INT NULL,
  `private_person_idprivate_person` INT NULL,
  `delivery_adress_iddelivery_adress` INT NOT NULL,
  PRIMARY KEY (`idCustomers`),
  INDEX `fk_Customers_Company1_idx` (`Company_idContactPersons` ASC) VISIBLE,
  INDEX `fk_Customers_Employees1_idx` (`Employees_idEmployees` ASC) VISIBLE,
  INDEX `fk_Customers_private_person1_idx` (`private_person_idprivate_person` ASC) VISIBLE,
  INDEX `fk_Customers_delivery_adress1_idx` (`delivery_adress_iddelivery_adress` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_Company1`
    FOREIGN KEY (`Company_idContactPersons`)
    REFERENCES `SPFCdb`.`Company` (`idContactPersons`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Customers_Employees1`
    FOREIGN KEY (`Employees_idEmployees`)
    REFERENCES `SPFCdb`.`Employees` (`idEmployees`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Customers_private_person1`
    FOREIGN KEY (`private_person_idprivate_person`)
    REFERENCES `SPFCdb`.`private_person` (`idprivate_person`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Customers_delivery_adress1`
    FOREIGN KEY (`delivery_adress_iddelivery_adress`)
    REFERENCES `SPFCdb`.`delivery_adress` (`iddelivery_adress`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Orders` (
  `idOrders` INT NOT NULL,
  `Customers_idCustomers` INT NOT NULL,
  `purchase_date` DATETIME NOT NULL,
  `requireddate` DATE NULL,
  `shippeddate` DATE NULL,
  `status` VARCHAR(45) NOT NULL,
  `comments` TEXT NULL,
  PRIMARY KEY (`idOrders`, `Customers_idCustomers`),
  INDEX `fk_Orders_Customers1_idx` (`Customers_idCustomers` ASC) VISIBLE,
  CONSTRAINT `fk_Orders_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `SPFCdb`.`Customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Orderdetails`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Orderdetails` (
  `idOrderdetails` INT NOT NULL,
  `product_number` VARCHAR(45) NOT NULL,
  `quantityordered` INT NOT NULL,
  `price` FLOAT NOT NULL,
  `Orders_idOrders` INT NOT NULL,
  `Orders_Customers_idCustomers` INT NOT NULL,
  PRIMARY KEY (`idOrderdetails`),
  INDEX `fk_Orderdetails_Orders1_idx` (`Orders_idOrders` ASC, `Orders_Customers_idCustomers` ASC) VISIBLE,
  CONSTRAINT `fk_Orderdetails_Orders1`
    FOREIGN KEY (`Orders_idOrders` , `Orders_Customers_idCustomers`)
    REFERENCES `SPFCdb`.`Orders` (`idOrders` , `Customers_idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Carinfo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Carinfo` (
  `idCarinfo` INT NOT NULL,
  `reg_number` VARCHAR(15) NOT NULL,
  `manufacture_name` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year_model` YEAR NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `Customers_idCustomers` INT NOT NULL,
  PRIMARY KEY (`idCarinfo`),
  INDEX `fk_Carinfo_Customers1_idx` (`Customers_idCustomers` ASC) VISIBLE,
  CONSTRAINT `fk_Carinfo_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `SPFCdb`.`Customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Suppliers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Suppliers` (
  `idSuppliers` INT NOT NULL,
  `company_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `zipcode` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idSuppliers`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Supplier_contactperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Supplier_contactperson` (
  `idSupplier_contactperson` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `Suppliers_idSuppliers` INT NOT NULL,
  PRIMARY KEY (`idSupplier_contactperson`),
  INDEX `fk_Supplier_contactperson_Suppliers1_idx` (`Suppliers_idSuppliers` ASC) VISIBLE,
  CONSTRAINT `fk_Supplier_contactperson_Suppliers1`
    FOREIGN KEY (`Suppliers_idSuppliers`)
    REFERENCES `SPFCdb`.`Suppliers` (`idSuppliers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`company_contact_employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`company_contact_employees` (
  `idcompany_contact_employees` INT NOT NULL AUTO_INCREMENT,
  `Company_idContactPersons` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idcompany_contact_employees`),
  INDEX `fk_company_contact_employees_Company1_idx` (`Company_idContactPersons` ASC) VISIBLE,
  CONSTRAINT `fk_company_contact_employees_Company1`
    FOREIGN KEY (`Company_idContactPersons`)
    REFERENCES `SPFCdb`.`Company` (`idContactPersons`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SPFCdb`.`Suppliers_has_Products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SPFCdb`.`Suppliers_has_Products` (
  `Suppliers_idSuppliers` INT NOT NULL,
  `Products_idProducts` INT NOT NULL,
  PRIMARY KEY (`Suppliers_idSuppliers`, `Products_idProducts`),
  INDEX `fk_Suppliers_has_Products_Products1_idx` (`Products_idProducts` ASC) VISIBLE,
  INDEX `fk_Suppliers_has_Products_Suppliers1_idx` (`Suppliers_idSuppliers` ASC) VISIBLE,
  CONSTRAINT `fk_Suppliers_has_Products_Suppliers1`
    FOREIGN KEY (`Suppliers_idSuppliers`)
    REFERENCES `SPFCdb`.`Suppliers` (`idSuppliers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Suppliers_has_Products_Products1`
    FOREIGN KEY (`Products_idProducts`)
    REFERENCES `SPFCdb`.`Products` (`idProducts`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
