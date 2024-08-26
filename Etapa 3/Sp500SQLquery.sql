CREATE DATABASE SP500;
USE SP500;

CREATE TABLE CompanyProfiles (
    Symbol varchar(255) NOT NULL,
    Company varchar(255),
    Sector varchar(255),
    Headquarters varchar(255),
    Fechafundada varchar(255),
    CONSTRAINT PK_CompanyProfiles PRIMARY KEY (Symbol)
);

CREATE TABLE Companies (
    Date Date NOT NULL,
    Symbol varchar(255) NOT NULL,
    CloseP float,
    CONSTRAINT PK_Companies PRIMARY KEY (Date, Symbol),
    CONSTRAINT FK_CPCompanies FOREIGN KEY (Symbol) REFERENCES CompanyProfiles(Symbol)
);

SELECT * FROM CompanyProfiles;
SELECT * FROM Companies;
