-- Create Regions Table
CREATE TABLE Regions (
    region_id SERIAL PRIMARY KEY,
    region_name VARCHAR(100) UNIQUE NOT NULL,
    state VARCHAR(50)
);

-- Create Users Table
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    preferred_region_id INT REFERENCES Regions(region_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Categories Table
CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) UNIQUE NOT NULL
);

-- Create Posts Table
CREATE TABLE Posts (
    post_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT,
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE,
    region_id INT REFERENCES Regions(region_id) ON DELETE CASCADE,
    location VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create PostCategories Junction Table
CREATE TABLE PostCategories (
    post_id INT REFERENCES Posts(post_id) ON DELETE CASCADE,
    category_id INT REFERENCES Categories(category_id) ON DELETE CASCADE,
    PRIMARY KEY (post_id, category_id)
);