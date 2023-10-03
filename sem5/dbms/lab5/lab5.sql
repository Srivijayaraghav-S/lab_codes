CREATE TABLE Employee ( 
     Empid INT PRIMARY KEY, 
     Lastname VARCHAR(255), 
     Firstname VARCHAR(255), 
     Email VARCHAR(255), 
     Department VARCHAR(255), 
     Designation VARCHAR(255), 
     DOJ DATE, 
     Phone_no VARCHAR(15) 
 ); 
  
 CREATE TABLE EmployeeLog ( 
     LogID INT PRIMARY KEY AUTO_INCREMENT, 
     ActionDate DATETIME, 
     Username VARCHAR(255), 
     Action VARCHAR(255) 
 ); 
 --1 
 DELIMITER // 
 CREATE OR REPLACE TRIGGER count_rows_trigger 
 AFTER INSERT ON Employee 
 FOR EACH ROW 
 BEGIN 
     DECLARE row_count INT; 
     SELECT COUNT(*) INTO row_count FROM Employee; 
     INSERT INTO EmployeeLog (ActionDate, Username, Action) VALUES (NOW(), USER(), CONCAT('Inserted ', row_count, ' rows into Employee table.')); 
 END; 
 // 
 DELIMITER ; 
 --2 
 DELIMITER // 
 CREATE OR REPLACE TRIGGER display_message_trigger 
 BEFORE INSERT ON employee 
 FOR EACH ROW 
 BEGIN 
     SIGNAL SQLSTATE '45000' 
     SET MESSAGE_TEXT = 'You are about to insert a new record into the Employee table.'; 
 END; 
 // 
 DELIMITER ; 
 --3 
 DELIMITER // 
 CREATE OR REPLACE TRIGGER add_prefix_to_phone_trigger 
 BEFORE INSERT ON Employee 
 FOR EACH ROW 
 BEGIN 
     SET NEW.Phone_no = CONCAT('+91', NEW.Phone_no); 
 END; 
 // 
 DELIMITER ; 
 --4 
 DELIMITER // 
 CREATE OR REPLACE TRIGGER prevent_duplicate_firstname_trigger 
 BEFORE INSERT ON Employee 
 FOR EACH ROW 
 BEGIN 
     IF NEW.Firstname IS NULL OR EXISTS (SELECT 1 FROM Employee WHERE Firstname = NEW.Firstname) THEN 
         SIGNAL SQLSTATE '45000' 
         SET MESSAGE_TEXT = 'First name cannot be NULL or a duplicate.'; 
     END IF; 
 END; 
 // 
 DELIMITER ; 
 --5 
 DELIMITER // 
 CREATE OR REPLACE TRIGGER log_employee_actions_trigger 
 AFTER INSERT ON Employee 
 FOR EACH ROW 
 BEGIN 
     INSERT INTO EmployeeLog (ActionDate, Username, Action) 
     VALUES (NOW(), USER(), 'Inserted a new record into Employee table.'); 
 END; 
 // 
 DELIMITER ; 
  
 DELIMITER // 
 CREATE OR REPLACE TRIGGER log_employee_actions_trigger_update 
 AFTER UPDATE ON Employee 
 FOR EACH ROW 
 BEGIN 
     INSERT INTO EmployeeLog (ActionDate, Username, Action) 
     VALUES (NOW(), USER(), 'Updated a record in Employee table.'); 
 END; 
 // 
 DELIMITER ; 
  
 DELIMITER // 
 CREATE OR REPLACE TRIGGER log_employee_actions_trigger_delete 
 AFTER DELETE ON Employee 
 FOR EACH ROW 
 BEGIN 
     INSERT INTO EmployeeLog (ActionDate, Username, Action) 
     VALUES (NOW(), USER(), 'Deleted a record from Employee table.'); 
 END; 
 // 
 DELIMITER ; 
 --6 
 DELIMITER // 
 CREATE OR REPLACE TRIGGER insert_if_doj_gt_2018_trigger 
 BEFORE INSERT ON Employee 
 FOR EACH ROW 
 BEGIN 
     IF NEW.DOJ <= '2018-01-01' THEN 
         SIGNAL SQLSTATE '45000' 
         SET MESSAGE_TEXT = 'DOJ must be greater than 2018-01-01.'; 
     END IF; 
 END; 
 // 
 DELIMITER ; 
 --7 
 DELIMITER // 
 CREATE OR REPLACE TRIGGER prevent_john_insert_trigger 
 BEFORE INSERT ON Employee 
 FOR EACH ROW 
 BEGIN 
     IF NEW.Firstname = 'John' THEN 
         SIGNAL SQLSTATE '45000' 
         SET MESSAGE_TEXT = 'Employees named John are not allowed.'; 
     END IF; 
 END; 
 // 
 DELIMITER ; 
 --8 
 DELIMITER // 
 CREATE OR REPLACE TRIGGER prevent_empid_change_trigger 
 BEFORE UPDATE ON Employee 
 FOR EACH ROW 
 BEGIN 
     IF NEW.Empid <> OLD.Empid THEN 
         SIGNAL SQLSTATE '45000' 
         SET MESSAGE_TEXT = 'Empid cannot be changed.'; 
     END IF; 
 END; 
 // 
 DELIMITER ; 
 --9 
 CREATE VIEW IF EXISTS EmployeeView AS 
 SELECT Empid, Lastname, Firstname, Department 
 FROM Employee; 
 DELIMITER // 
 CREATE OR REPLACE TRIGGER insert_into_view_trigger 
 AFTER INSERT ON Employee 
 FOR EACH ROW 
 BEGIN 
     INSERT INTO EmployeeView (Empid, Lastname, Firstname, Department) 
     VALUES (NEW.Empid, NEW.Lastname, NEW.Firstname, NEW.Department); 
 END; 
 // 
 DELIMITER ; 
  
 -- Testing Trigger 2 (Display Message Before Insert) 
 -- This should display an error message. 
 INSERT INTO Employee (Empid, Lastname, Firstname, Email, Department, Designation, DOJ, Phone_no) 
 VALUES (1, 'Doe', 'James', 'john.doe@example.com', 'HR', 'Manager', '2023-01-15', '+123456789'); 
  
 -- Testing Trigger 4 (Prevent Duplicate or Null Firstnames) 
 -- This should display an error message. 
 INSERT INTO Employee (Empid, Lastname, Firstname, Email, Department, Designation, DOJ, Phone_no) 
 VALUES (2, 'Smith', 'James', 'james.smith@example.com', 'Finance', 'Analyst', '2023-05-20', '+987654321'); 
  
 -- Testing Trigger 6 (Insert Only if DOJ > 2018) 
 -- This should display an error message. 
 INSERT INTO Employee (Empid, Lastname, Firstname, Email, Department, Designation, DOJ, Phone_no) 
 VALUES (3, 'Johnson', 'Alice', 'alice.johnson@example.com', 'IT', 'Developer', '2017-10-10', '+111222333'); 
  
 -- Testing Trigger 7 (Prevent John from Being Inserted) 
 -- This should display an error message. 
 INSERT INTO Employee (Empid, Lastname, Firstname, Email, Department, Designation, DOJ, Phone_no) 
 VALUES (4, 'Brown', 'John', 'john.brown@example.com', 'Marketing', 'Coordinator', '2023-03-25', '+444555666'); 
  
 -- Inserting a valid record 
 INSERT INTO Employee (Empid, Lastname, Firstname, Email, Department, Designation, DOJ, Phone_no) 
 VALUES (5, 'Wilson', 'Johnson', 'johnson.wilson@example.com', 'Sales', 'Manager', '2019-08-01', '+777888999'); 

 -- Updating Empid (Testing Trigger 8) 
 -- This should display an error message. 
 UPDATE Employee SET Empid = 6 WHERE Empid = 5; 
  
 -- Updating other fields (Testing Trigger 5) 
 -- This should log an update action. 
 UPDATE Employee SET Lastname = 'Smith' WHERE Empid = 6; 
  
 -- Deleting a record (Testing Trigger 5) 
 -- This should log a delete action. 
 DELETE FROM Employee WHERE Empid = 6;
