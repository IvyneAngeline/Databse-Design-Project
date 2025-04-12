-- List all books with authors and publishers
SELECT b.title, a.first_name, a.last_name, p.name AS publisher
FROM book b
JOIN book_author ba ON b.book_id = ba.book_id
JOIN author a ON ba.author_id = a.author_id
JOIN publisher p ON b.publisher_id = p.publisher_id;

-- Books in English
SELECT title FROM book
JOIN book_language bl ON book.language_id = bl.language_id
WHERE bl.language_name = 'English';
