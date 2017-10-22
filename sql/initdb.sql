USE sql12195058;

CREATE TABLE IF NOT EXISTS `courses` (
  `faculty` varchar(5) NOT NULL,
  `course_code` int(5) NOT NULL,
  `class_id` varchar(10) NOT NULL,
  `day` int(2) NOT NULL,
  `activity` varchar(15) NOT NULL,
  `start_time` int(3) NOT NULL,
  `length` int(3) NOT NULL,
  UNIQUE KEY `faculty` (`faculty`,`course_code`,`class_id`,`day`,`activity`,`start_time`,`length`)
);

CREATE TABLE IF NOT EXISTS `friend_request` (
  `from_id` int(11) NOT NULL,
  `to_id` int(11) NOT NULL,
  `status` varchar(45) NOT NULL,
  `message` varchar(45) DEFAULT NULL,
  `date` date DEFAULT NULL,
  FOREIGN KEY (`from_id`) REFERENCES `user_profile` (`id`),
  FOREIGN KEY (`to_id`) REFERENCES `user_profile` (`id`)
);

CREATE TABLE IF NOT EXISTS user_profile (
	id 			INT(11) NOT NULL AUTO_INCREMENT,
	username 	VARCHAR(45) NOT NULL,
	password 	VARCHAR(45) NOT NULL,
	firstname 	VARCHAR(45) NOT NULL,
	lastname	VARCHAR(45) NOT NULL,
	email 		VARCHAR(45) NOT NULL,
	gender		VARCHAR(45) DEFAULT NULL,
	dob			VARCHAR(45) DEFAULT NULL,
	status		VARCHAR(45) DEFAULT NULL,
	imgpath		VARCHAR(45) DEFAULT NULL,
	degree          VARCHAR(45) DEFAULT NULL,
  `flags` int(11) DEFAULT NULL,
  `last_update` int(11) DEFAULT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS user_friend (
  user_id1   INT(11) NOT NULL,
  user_id2   INT(11) NOT NULL,
  FOREIGN KEY (user_id1) REFERENCES user_profile(id),
	FOREIGN KEY (user_id2) REFERENCES user_profile(id)
);

CREATE TABLE IF NOT EXISTS user_class (
  id 			INT(11) NOT NULL AUTO_INCREMENT,
  user_id  INT(11) NOT NULL,
  course_name  VARCHAR(45) NOT NULL,
  start_time VARCHAR(45) NOT NULL,
  end_time  VARCHAR(45) NOT NULL,
  `day` int(3) NOT NULL,
  `length` int(3) NOT NULL,
  `activity` varchar(45) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES user_profile(id)
);

CREATE TABLE IF NOT EXISTS user_meetup_request (
  id 			INT(11) NOT NULL AUTO_INCREMENT,
  from_id  INT(11) NOT NULL,
  to_id     INT (11) NOT NULL,
  status    VARCHAR(45) NOT NULL,
  description VARCHAR(45) NOT NULL,
  date VARCHAR(45) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (from_id) REFERENCES user_profile(id),
  FOREIGN KEY (to_id) REFERENCES user_profile(id)
);

CREATE TABLE IF NOT EXISTS user_todo_list (
  id 			INT(11) NOT NULL AUTO_INCREMENT,
  title   VARCHAR(45) NOT NULL,
  description   VARCHAR(200) NOT NULL,
  user_id  INT(11) NOT NULL,
  course_name  VARCHAR(45) NOT NULL,
  create_time VARCHAR(45) NOT NULL,
  end_time  VARCHAR(45) NOT NULL,
  priority INT(11) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES user_profile(id)
);

CREATE TABLE IF NOT EXISTS public_event (
  id 			INT(11) NOT NULL AUTO_INCREMENT,
  title   VARCHAR(45) NOT NULL,
  description   VARCHAR(200) NOT NULL,
  start_time VARCHAR(45) NOT NULL,
  end_time VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);
