# Distributed Task Queue System

A scalable, distributed task queue system for processing background jobs, with a sleek dashboard inspired by JetBrains' 2020 design. Built with FastAPI, Redis, React, and Tailwind CSS.

## Features
- **Task Management**: Enqueue tasks (e.g., email sending) via REST API with JWT authentication.
- **Real-Time Monitoring**: Dashboard displays job status, queue length, and metrics with animated transitions.
- **Scalable Architecture**: Redis for queuing, FastAPI for API, and containerized workers with Docker.
- **JetBrains-Inspired UI**: Clean typography, dark/light themes, and minimalistic design with hover effects.
- **Responsive Design**: Adapts to desktop and mobile.

## Demo
Try the dashboard at [https://your-username.github.io/distributed-task-queue](https://your-username.github.io/distributed-task-queue).

![Demo GIF](assets/demo.gif)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/distributed-task-queue.git
   ```
2. **Backend Setup** (requires Docker):
   ```bash
   docker-compose up -d
   ```
3. **Frontend Setup**:
   - Open `index.html` in a browser for the dashboard (no server needed).
   - Or host on GitHub Pages (see below).

## Usage
1. Open the dashboard (`index.html` or live URL).
2. Click "Login" (username: `admin`, password: `password`) to authenticate.
3. Enter a task (e.g., "send email") and click "Enqueue Task".
4. View job status and queue length in the dashboard.
5. Toggle dark/light theme for a JetBrains-inspired look.

## Tech Stack
- **Backend**: Python (FastAPI), Redis, JWT
- **Frontend**: React, Tailwind CSS, Axios
- **Deployment**: Docker, Docker Compose
- **Fonts**: JetBrains Mono

## Architecture
- **API**: FastAPI serves endpoints (`/login`, `/tasks`) with JWT authentication.
- **Queue**: Redis stores tasks and manages the queue (`task_queue` list).
- **Workers**: Python scripts process tasks asynchronously, updating status in Redis.
- **Dashboard**: React frontend fetches job data and displays metrics with Tailwind styling.

## Future Enhancements
- Add task retry logic and failure handling.
- Implement WebSocket for real-time job updates.
- Support task prioritization and scheduling.

## License
MIT License