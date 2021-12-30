/*
 Navicat Premium Data Transfer

 Source Server         : duxiaobai
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : lesson

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 30/12/2021 19:56:17
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `classID` int NOT NULL,
  `className` char(20) DEFAULT NULL,
  PRIMARY KEY (`classID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of class
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `courseID` int NOT NULL,
  `courseName` char(20) DEFAULT NULL,
  PRIMARY KEY (`courseID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of course
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for course_schdule
-- ----------------------------
DROP TABLE IF EXISTS `course_schdule`;
CREATE TABLE `course_schdule` (
  `classID` int NOT NULL,
  `teacherID` int NOT NULL,
  `courseID` int NOT NULL,
  `weeks` int NOT NULL,
  `lessons` int NOT NULL,
  `remark` char(100) DEFAULT NULL,
  PRIMARY KEY (`classID`,`teacherID`,`courseID`,`weeks`,`lessons`),
  KEY `fk_teacherID` (`teacherID`),
  KEY `fk_courseID` (`courseID`),
  CONSTRAINT `fk_classID` FOREIGN KEY (`classID`) REFERENCES `class` (`classID`),
  CONSTRAINT `fk_courseID` FOREIGN KEY (`courseID`) REFERENCES `course` (`courseID`),
  CONSTRAINT `fk_teacherID` FOREIGN KEY (`teacherID`) REFERENCES `teacher` (`teacherID`),
  CONSTRAINT `course_schdule_chk_1` CHECK (((`weeks` > 0) and (`weeks` < 8))),
  CONSTRAINT `course_schdule_chk_2` CHECK (((`lessons` > 0) and (`lessons` < 9)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of course_schdule
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `studentID` int NOT NULL,
  `name` char(15) NOT NULL,
  `sex` char(5) NOT NULL,
  `classID` int DEFAULT NULL,
  PRIMARY KEY (`studentID`),
  KEY `ffk_classID` (`classID`),
  CONSTRAINT `ffk_classID` FOREIGN KEY (`classID`) REFERENCES `class` (`classID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `student_chk_1` CHECK (((`sex` = _utf8mb4'男') or (`sex` = _utf8mb4'女')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of student
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `teacherID` int NOT NULL,
  `name` char(15) NOT NULL,
  `sex` char(5) NOT NULL,
  `age` int NOT NULL,
  PRIMARY KEY (`teacherID`),
  CONSTRAINT `teacher_chk_1` CHECK (((`sex` = _utf8mb4'男') or (`sex` = _utf8mb4'女')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of teacher
-- ----------------------------
BEGIN;
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
