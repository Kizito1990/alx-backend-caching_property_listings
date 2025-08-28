# 🏡 Django Property Listings with Multi-Level Caching

## 📖 Overview
This project implements a **Django-based property listing application** with **Redis caching at multiple levels**.  
It demonstrates **caching strategies, containerized databases, and cache invalidation techniques** to build scalable and performant web applications.

The app runs with:
- **PostgreSQL** (persistent data storage)
- **Redis** (in-memory caching)
- **Docker & Docker Compose** (containerized services)

---

## 🎯 Learning Objectives
By working through this project, you will learn how to:

- Implement **multi-level caching strategies** in Django applications.
- Configure and integrate **Redis as a cache backend**.
- Set up **PostgreSQL and Redis** with Docker Compose.
- Apply **cache invalidation techniques** using Django signals.
- Monitor **cache performance metrics** and analyze efficiency.
- Write **efficient database query patterns** with caching.
- Structure Django projects for **maintainability and scalability**.

---

## 🔑 Key Concepts
- **Multi-level Caching**: View-level + queryset-level caching.
- **Cache Invalidation**: Keep cache consistent using Django signals.
- **Containerization**: Use Docker to manage PostgreSQL & Redis.
- **Cache Metrics**: Track Redis cache performance via logging.
- **Database Optimization**: Reduce DB load through caching.

---

## 🛠️ Tools and Libraries
- **[Django](https://www.djangoproject.com/):** Web framework.
- **[PostgreSQL](https://www.postgresql.org/):** Relational database.
- **[Redis](https://redis.io/):** In-memory data store for caching.
- **[Docker](https://www.docker.com/):** Containerization platform.
- **[django-redis](https://github.com/jazzband/django-redis):** Redis backend for Django.
- **[psycopg2](https://pypi.org/project/psycopg2/):** PostgreSQL adapter.
- **Python’s logging:** Monitor cache hits/misses.

---

## 🌍 Real-World Use Case
This project simulates a **real estate platform** where:
- Property listings are **frequently accessed but rarely modified**.
- Database load must be minimized during **peak traffic**.
- **Consistency** must be maintained despite caching.
- Performance metrics are tracked for **cache effectiveness**.

Similar caching setups are crucial for:
- High-traffic apps (real estate, e-commerce).
- Expensive database queries.
- Sub-second response time requirements.
- Applications needing **efficient scalability**.

---

🏗️ Project Structure
alx-backend-caching_property_listings/
│── docker-compose.yml         # Docker services for Postgres & Redis
│── manage.py                  # Django project entrypoint
│── requirements.txt           # Python dependencies
│── alx_backend_caching_property_listings/
│   ├── settings.py            # Django settings (Postgres + Redis config)
│   ├── urls.py
│   ├── wsgi.py
│── properties/
│   ├── models.py              # Property model
│   ├── views.py               # Views with caching
│   ├── signals.py             # Cache invalidation logic
│   ├── templates/             # HTML templates

📊 Caching Strategies Implemented

View-level caching → Cache entire rendered views.

Low-level caching → Cache specific database queries.

Cache invalidation → Use Django signals to clear stale data.

Performance logging → Monitor cache hits & misses.
