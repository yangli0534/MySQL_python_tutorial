/*
'Sn': Sn, 'RunMode': RunMode, 'StartTime': StartTime, 'StopTime': StopTime, 'Station': Station, 'Status': Status,
                      'UserName': UserName, 'ProductNumber': ProductNumber, 'TestType': TestType, 'Rstate': Rstate,
                      'TpName': 'RuVue', 'TpVer': TpVer, 'MpgName': MpgName, 'MpgTestTime': MpgTestTime, 'AppRev': AppRev,
                      'MpgDescription': MpgDescription, 'MpName': MpName, 'MpStatus': MpStatus, 'MpTestTime': MpTestTime, 'MpDataType': MpDataType,
                      'MpDescription': MpDescription, 'LimitDown': LimitDown, 'LimitUp': LimitUp, 'Unit': Unit, 'Result': Result
*/
DROP DATABASE IF EXISTS `oru1226n78a`;
CREATE DATABASE `oru1226n78a`; 
USE `oru1226n78a`;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;

CREATE TABLE `test_result_tbl` (
	`cnt` INT,
	`Sn` varchar(19) NOT NULL, 
	`RunMode` varchar(10) DEFAULT 'Auto',
	`StartTime` timestamp NOT NULL, 
	`StopTime` timestamp DEFAULT NULL, 
	`Station` varchar(10) DEFAULT 'PA0001', 
	`Status` varchar(10) DEFAULT NULL,
	`UserName` varchar(10) DEFAULT 'Z0030', 
    `ProductNumber` varchar(15) DEFAULT 'RHS11660061', 
    `TestType` varchar(10) DEFAULT 'Prod', 
    `Rstate` varchar(5) DEFAULT 'R1D',  
	`TpName` varchar(10) DEFAULT 'RuVue',
    `TpVer` varchar(10) DEFAULT '20210505', 
    `MpgName` varchar(30) NOT NULL, 
    `MpgTestTime` timestamp NOT NULL, 
    `AppRev` varchar(30) NOT NULL,
	`MpgDescription` varchar(100) DEFAULT NULL, 
    `MpName` varchar(50) NOT NULL, 
    `MpStatus` varchar(10) DEFAULT NULL, 
    `MpTestTime` timestamp NOT NULL, 
    `MpDataType` varchar(10) DEFAULT NULL,
	`MpDescription` varchar(100) DEFAULT NULL, 
    `LimitDown` DOUBLE NOT NULL,
    `LimitUp` DOUBLE NOT NULL,
    `Unit` varchar(10) DEFAULT NULL, 
    `Result` DOUBLE NOT NULL DEFAULT 0.00,
	PRIMARY KEY(`cnt`)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*
INSERT INTO `test_result_tbl`(
	`Sn`, 
	`RunMode`,
	`StartTime`, 
    `MpgName`, 
    `MpgTestTime`, 
    `AppRev`,
    `MpName`, 
    `MpTestTime`, 
    `LimitDown`,
    `LimitUp`,
    `Result`
)
VALUES (
	'Z122601202102000015', 
	'Auto',
	now(), 
    'Calibration', 
    now(), 
    'ZSM_20210407_ST_Cpri_Clock_01',
    'Rx calib', 
    now(), 
    -99.0,
    -45.0,
    -50);
*/

SELECT * FROM oru1226n78a.test_result_tbl;
