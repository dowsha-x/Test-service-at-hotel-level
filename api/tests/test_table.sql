-- Удаление таблиц и индекса, если они существуют
DROP TABLE IF EXISTS test_reservations_bookings CASCADE;
DROP TABLE IF EXISTS test_reservations_rooms CASCADE;
DROP TABLE IF EXISTS test_rooms CASCADE;
DROP INDEX IF EXISTS test_unique_booking_dates;

-- Таблица для модели Rooms
CREATE TABLE test_reservations_rooms (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Таблица для модели Bookings
CREATE TABLE test_reservations_bookings (
    id SERIAL PRIMARY KEY,
    room_id INT NOT NULL REFERENCES test_reservations_rooms(id) ON DELETE CASCADE,
    date_start DATE NOT NULL,
    date_end DATE NOT NULL,
    guest_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT test_unique_booking_dates UNIQUE (room_id, date_start, date_end)
);