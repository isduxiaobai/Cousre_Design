/*
 Navicat Premium Data Transfer

 Source Server         : duxiaobai
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : Library_System

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 31/12/2021 00:57:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tb_book
-- ----------------------------
DROP TABLE IF EXISTS `tb_book`;
CREATE TABLE `tb_book` (
  `bId` int NOT NULL,
  `bBookName` varchar(40) NOT NULL,
  `bAuthor` varchar(20) NOT NULL,
  `bSex` varchar(10) NOT NULL,
  `bPrice` float NOT NULL,
  `bBookDescription` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `btId` int NOT NULL,
  PRIMARY KEY (`bId`),
  KEY `tb_book_ibfk1` (`btId`),
  CONSTRAINT `tb_book_ibfk1` FOREIGN KEY (`btId`) REFERENCES `tb_booktype` (`btId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of tb_book
-- ----------------------------
BEGIN;
INSERT INTO `tb_book` VALUES (1, '山青院', '杜小白', '男', 45, '来自宇宙中心', 9);
INSERT INTO `tb_book` VALUES (2, '山青院111', 'duxiaobai', '男', 55, '来自奥特曼训练基地', 9);
INSERT INTO `tb_book` VALUES (3, '山青院222', '杜小白', '男', 55, '点点点', 9);
INSERT INTO `tb_book` VALUES (5, '西游记', '吴承恩', '男', 50, '西游记是一部神魔小说。', 2);
INSERT INTO `tb_book` VALUES (9, '三体', '刘慈欣', '男', 100, '科幻巨著。', 7);
INSERT INTO `tb_book` VALUES (10, '醉花阴', '李清照', '女', 5, '词。', 2);
COMMIT;

-- ----------------------------
-- Table structure for tb_booktype
-- ----------------------------
DROP TABLE IF EXISTS `tb_booktype`;
CREATE TABLE `tb_booktype` (
  `btId` int NOT NULL,
  `btName` varchar(40) NOT NULL,
  `btDescription` varchar(1000) NOT NULL,
  PRIMARY KEY (`btId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of tb_booktype
-- ----------------------------
BEGIN;
INSERT INTO `tb_booktype` VALUES (2, '文学', '这些书都是与文学相关的书籍');
INSERT INTO `tb_booktype` VALUES (5, '高数', '高数是一棵神奇的树。');
INSERT INTO `tb_booktype` VALUES (6, '外语', '学会一门外语是很有用处的。');
INSERT INTO `tb_booktype` VALUES (7, '科幻', '对未来的期望。');
INSERT INTO `tb_booktype` VALUES (8, '动漫', '海贼王、火影等。一人之下也是动漫。');
INSERT INTO `tb_booktype` VALUES (9, '生活', '一些生活技能知识的书籍。');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
