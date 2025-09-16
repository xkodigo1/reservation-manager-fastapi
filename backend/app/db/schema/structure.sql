/* For security, avoid using root user for database connections in production */

CREATE USER 'manager_user'@'localhost' IDENTIFIED BY 'reservManager#25'; /* Create a dedicated DB user */
GRANT ALL PRIVILEGES ON reservation_manager.* TO 'manager_user'@'localhost'; /* Grant necessary privileges */
FLUSH PRIVILEGES;# /* Apply changes */

/* Database schema for Reservation Manager application */

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS reservation_manager;

-- Switch to the database
USE reservation_manager;

-- =====================
-- Table: Users
-- =====================
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('user', 'admin') NOT NULL DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================
-- Table: Rooms
-- =====================
CREATE TABLE rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    headquarter ENUM('Bogotá', 'Medellín') NOT NULL,
    capacity INT NOT NULL CHECK (capacity > 0),
    resources JSON NOT NULL, -- E.g., {"projector": true, "whiteboard": false}
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================
-- Table: Reservations
-- =====================
CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    room_id INT NOT NULL,
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status ENUM('pending', 'confirmed', 'canceled') NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Relationships
    CONSTRAINT fk_reservation_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_reservation_room FOREIGN KEY (room_id) REFERENCES rooms(id) ON DELETE CASCADE,
    
    -- Validation to ensure end_time is after start_time
    CHECK (start_time < end_time)
);
