-- Удаление таблиц и индекса, если они существуют
DROP TABLE IF EXISTS reservations_bookings CASCADE;
DROP TABLE IF EXISTS reservations_rooms CASCADE;
DROP INDEX IF EXISTS unique_booking_dates;

-- Таблица для модели Rooms
CREATE TABLE reservations_rooms (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Таблица для модели Bookings
CREATE TABLE reservations_bookings (
    id SERIAL PRIMARY KEY,
    room_id INT NOT NULL REFERENCES reservations_rooms(id) ON DELETE CASCADE,
    date_start DATE NOT NULL,
    date_end DATE NOT NULL,
    guest_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_booking_dates UNIQUE (room_id, date_start, date_end)
);