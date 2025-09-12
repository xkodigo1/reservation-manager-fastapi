USE reservation_manager;

-- =====================
-- Users
-- =====================
INSERT INTO users (name, email, password_hash, role)
VALUES 
('Admin User', 'admin@cowork.com', '$2b$12$hashEjemplo', 'admin'),
('Juan Pérez', 'juan.perez@example.com', '$2b$12$abcdehashEjemplo', 'user'),
('María Gómez', 'maria.gomez@example.com', '$2b$12$zyxwvutzhashEjemplo', 'user');

-- =====================
-- Rooms
-- =====================
INSERT INTO rooms (name, headquarter, capacity, resources)
VALUES
('Sala Innovación', 'Bogotá', 12, JSON_ARRAY('Proyector', 'Pizarra', 'Sonido')),
('Sala Creativa', 'Bogotá', 8, JSON_ARRAY('Pizarra', 'TV')),
('Sala Ejecutiva', 'Medellín', 20, JSON_ARRAY('Proyector', 'Videoconferencia', 'Sonido')),
('Sala Startups', 'Medellín', 10, JSON_ARRAY('Pizarra', 'Proyector'));

-- =====================
-- Reservations
-- =====================
INSERT INTO reservations (user_id, room_id, date, start_time, end_time, status)
VALUES
-- Juan Pérez's Reservations
(1, 1, '2025-09-12', '09:00:00', '10:00:00', 'confirmed'),
(1, 2, '2025-09-13', '14:00:00', '15:00:00', 'pending'),

-- María Gómez's Reservations  
(2, 3, '2025-09-14', '10:00:00', '11:00:00', 'confirmed'),
(2, 3, '2025-09-15', '16:00:00', '17:00:00', 'canceled');
