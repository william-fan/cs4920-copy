USE sql12195058;

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
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES user_profile(id)
);

CREATE TABLE IF NOT EXISTS user_meetup_request (
  from_id  INT(11) NOT NULL,
  to_id     INT (11) NOT NULL,
  status    VARCHAR(45) NOT NULL,
  FOREIGN KEY (from_id) REFERENCES user_profile(id),
  FOREIGN KEY (to_id) REFERENCES user_profile(id)
);

INSERT INTO user_profile (id, username, password, firstname, lastname, email, gender, dob, status, imgpath)
VALUES (2, 'testuser1', 'testuser1', 'test1', 'user1', 'testuser1@test.com', 'MALE', '1997-01-01', 'CREATED', 'default.jpg');
INSERT INTO user_profile (id, username, password, firstname, lastname, email, gender, dob, status, imgpath)
VALUES (3, 'testuser2', 'testuser2', 'test2', 'user2', 'testuser2@test.com', 'MALE', '1997-01-01', 'CREATED', 'default.jpg');
INSERT INTO user_profile (id, username, password, firstname, lastname, email, gender, dob, status, imgpath)
VALUES (4, 'testuser3', 'testuser3', 'test3', 'user3', 'testuser3@test.com', 'MALE', '1997-01-01', 'CREATED', 'default.jpg');

