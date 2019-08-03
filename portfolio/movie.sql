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


CREATE TABLE IF NOT EXISTS `current_movie` (
  `m_no` int(11) NOT NULL AUTO_INCREMENT,
  `current_movie_title` varchar(50) DEFAULT '0' COMMENT 'title',
  `current_movie_img` varchar(300) DEFAULT '0' COMMENT 'image',
  `current_movie_story` varchar(50) DEFAULT '0' COMMENT 'story',
  `current_movie_open` varchar(100) DEFAULT '0' COMMENT 'opendat',
  `current_movie_genre` varchar(100) DEFAULT '0' COMMENT 'genre',
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
  `show_movie_story` varchar(50) DEFAULT NULL,
  `show_movie_open` varchar(100) DEFAULT NULL,
  `show_movie_genre` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`m_no`)
) ENGINE=InnoDB AUTO_INCREMENT=549 DEFAULT CHARSET=utf8;

-- 테이블 movie.test 구조 내보내기
DROP TABLE IF EXISTS `test`;
CREATE TABLE IF NOT EXISTS `test` (
  `title` varchar(200) DEFAULT NULL,
  `codem` varchar(100) NOT NULL,
  PRIMARY KEY (`codem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;