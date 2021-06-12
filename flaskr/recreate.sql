DROP TABLE IF EXISTS data;

CREATE TABLE data (
    timestamp TEXT NOT NULL PRIMARY KEY,
    img1 INT NOT NULL,
    img2 INT NOT NULL,
    img3 INT NOT NULL,
    img4 INT NOT NULL,
    img5 INT NOT NULL,
    average INT NOT NULL
);