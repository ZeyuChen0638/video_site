docker stop videoSite-db
docker rm videoSite-db
docker stop videoSite-redis
docker rm videoSite-redis
docker run --rm -d --name videoSite-db -e POSTGRES_PASSWORD=baby123 -p 5432:5432 -v /home/owen/Projects/video_site/backend/db_volume:/var/lib/postgresql/data postgres:14
docker run --rm -d -p 6379:6379 redis:7
cd backend && python3 manage.py runserver 0.0.0.0:8000