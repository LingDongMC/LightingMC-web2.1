DROP TABLE IF EXISTS posts;

CREATE TABLE slogan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    button TEXT NOT NULL,
    content TEXT NOT NULL,
    link TEXT NOT NULL
);
CREATE TABLE introduce (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    button TEXT NOT NULL,
    content TEXT NOT NULL,
    link TEXT NOT NULL
);