-- --------------------------------------------------------
-- ホスト:                          127.0.0.1
-- サーバーのバージョン:                   10.3.13-MariaDB - mariadb.org binary distribution
-- サーバー OS:                      Win64
-- HeidiSQL バージョン:               9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
DROP DATABASE movie;
create database movie;
USE movie;

-- 테이블 movie.board 구조 내보내기
DROP TABLE IF EXISTS `board`;
CREATE TABLE IF NOT EXISTS `board` (
  `b_no` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `b_title` varchar(100) NOT NULL,
  `b_content` longtext DEFAULT NULL,
  `m_no` int(11) NOT NULL,
  `writer` varchar(100) NOT NULL,
  `b_date` timestamp NULL DEFAULT NULL,
  `good` int(11) DEFAULT NULL,
  PRIMARY KEY (`b_no`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

--  テーブル movie.current_movie の構造をダンプしています
CREATE TABLE IF NOT EXISTS `current_movie` (
  `m_no` int(11) NOT NULL AUTO_INCREMENT,
  `current_movie_title` varchar(50) DEFAULT '0' COMMENT '현재상영영화제목',
  `current_movie_img` varchar(300) DEFAULT '0' COMMENT '현재상영영화이미지',
  `current_movie_genre` varchar(50) DEFAULT '0' COMMENT '현재상영영화연령제한',
  `current_movie_open` varchar(50) DEFAULT '0' COMMENT '현재상영영화개봉일',
  `current_movie_story` varchar(2000) DEFAULT '0' COMMENT '현재상영영화줄거리',
  PRIMARY KEY (`m_no`)
) ENGINE=InnoDB AUTO_INCREMENT=2760 DEFAULT CHARSET=utf8;

-- テーブル movie.current_movie: ~0 rows (約) のデータをダンプしています
/*!40000 ALTER TABLE `current_movie` DISABLE KEYS */;
/*!40000 ALTER TABLE `current_movie` ENABLE KEYS */;

--  テーブル movie.movie_to_be_screened の構造をダンプしています
CREATE TABLE IF NOT EXISTS `movie_to_be_screened` (
  `m_no` int(11) NOT NULL AUTO_INCREMENT,
  `show_movie_title` varchar(50) DEFAULT NULL,
  `show_movie_img` varchar(300) DEFAULT NULL,
  `show_movie_open` varchar(50) DEFAULT NULL,
  `show_movie_story` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`m_no`)
) ENGINE=InnoDB AUTO_INCREMENT=549 DEFAULT CHARSET=utf8;

-- 테이블 movie.test 구조 내보내기
DROP TABLE IF EXISTS `test`;
CREATE TABLE IF NOT EXISTS `test` (
  `title` varchar(200) DEFAULT NULL,
  `codem` varchar(100) NOT NULL,
  PRIMARY KEY (`codem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- テーブル movie.movie_to_be_screened: ~0 rows (約) のデータをダンプしています
/*!40000 ALTER TABLE `movie_to_be_screened` DISABLE KEYS */;
/*!40000 ALTER TABLE `movie_to_be_screened` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
