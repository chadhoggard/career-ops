CREATE TYPE status AS ENUM ('applied', 'assessment', 'interview', 'rejected', 'offer');

CREATE TABLE applications (
application_id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
company varchar(50) NOT NULL,
position varchar(100) NOT NULL,
status status NOT NULL,
date_applied date NOT NULL,
last_updated date NOT NULL
);
