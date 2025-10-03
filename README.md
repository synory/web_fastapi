## Модели данных

### Модель User (Пользователь)
- **id** – уникальный идентификатор
- **name** – имя пользователя  
- **email** – уникальный email
- **registered_at** – дата регистрации
- **is_verified_author** – флаг верификации автора
- **avatar** – URL аватара

### Модель News (Новость)
- **id** – уникальный идентификатор
- **title** – заголовок новости
- **content** – содержание в JSON формате
- **published_at** – дата публикации
- **author_id** – ссылка на автора
- **cover** – URL обложки

### Модель Comment (Комментарий)
- **id** – уникальный идентификатор
- **text** – текст комментария
- **published_at** – дата публикации
- **news_id** – ссылка на новость
- **author_id** – ссылка на автора комментария

## Примеры использования API

### Создание пользователя

```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "test", 
    "email": "test@example.com",
    "is_verified_author": true
  }'
```

### Создание новости
```bash
curl -X POST "http://localhost:8000/news/" 
  -H "Content-Type: application/json" 
  -d '{
    "title": "Новые технологии",
    "content": {
      "text": "Содержание новости...",
      "category": "technology"
    },
    "author_id": 1
  }'
```
### Создание комментария
```bash
curl -X POST "http://localhost:8000/comments/" \
  -H "Content-Type: application/json" \
  -d '{
    "text": " комментарий",
    "news_id": 1,
    "author_id": 2
  }'
```
### Обновление новости
```bash
curl -X PUT "http://localhost:8000/news/1" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Обновленный заголовок"
  }'
```
### Обновление комментария
```bash
curl -X PUT "http://localhost:8000/comments/1" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Обновленный комментарий"
  }'
```
### Удаление новости
```bash
curl -X DELETE "http://localhost:8000/news/1"
```
