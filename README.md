

<!-- ABOUT THE PROJECT -->
## 🚀 Python Microservices
A Python-based microservices application that allows searching for meal based on categories and view search history.

<!-- GETTING STARTED -->
<!--## Description-->
<!--A grocery recommendation system that uses the Apriori algorithm to suggest related items based on user input. The API is built with Django, containerized using Docker, and deployed on Render. GitHub Actions automates CI/CD to streamline the deployment process.-->
## 📌 Project Highlights
**Django Rest Framework:** Built an api using django rest framework for searching meal which retrieves meal data from an external api.

**Flask:** Built a Flask application to display previously searched meal categories, allowing users to view their search history.

**PostgreSQL:** Used PostgreSQL as the database for each service, storing meal search data and user history in separate databases.

**RabbitMQ:** Implemented RabbitMQ as a message broker to facilitate asynchronous communication between the Django and Flask services.

**Nginx:** Configured Nginx as a reverse proxy server to route client requests to the appropriate backend service.

**Docker Compose:** Used Docker Compose to manage and run all services in isolated containers.

### 🔧 Tech Stack
* [![Django Rest Framework][DRF.img]][DRF-url]
* [![Flask][Flask.img]][Flask-url]
* [![PostgreSQL][PostgreSQL.img]][PostgreSQL-url]
* [![RabbitMQ][RabbitMQ.img]][RabbitMQ-url]
* [![Nginx][Nginx.img]][Nginx-url]
* [![Docker][Docker.img]][Docker-url]

### ⚙️ Installation with Docker


1. Clone the Repository
    ```bash
    git clone https://github.com/SA-K1B/python_microservices_drf_flask.git
    ```
2. Navigate to the project directory
    ```sh
    cd python_microservices_drf_flask
    ```
3. Build Image 
   ```sh
   docker compose build
   ```
4. Start the services
   ```sh
   docker compose up -d
   ```
Now, the app will be available at https://localhost:8080
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[DRF-url]: https://www.django-rest-framework.org/
[DRF.img]: https://img.shields.io/badge/Django%20Rest%20Framework-2E8B57?style=for-the-badge&logo=django&logoColor=white

[Flask-url]: https://palletsprojects.com/p/flask/
[Flask.img]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white

[PostgreSQL-url]: https://www.postgresql.org/
[PostgreSQL.img]: https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white

[RabbitMQ-url]: https://www.rabbitmq.com/
[RabbitMQ.img]: https://img.shields.io/badge/RabbitMQ-61D0E7?style=for-the-badge&logo=rabbitmq&logoColor=white

[Nginx-url]: https://www.nginx.com/
[Nginx.img]: https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white

[Docker-url]: https://www.docker.com/
[Docker.img]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white