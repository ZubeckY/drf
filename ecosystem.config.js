module.exports = {
  apps: [
    {
      name: "drf-api",
      script: "drfsite/manage.py",
      // args: ["runserver", "127.0.0.1:8000"],
      args: ["runserver"],
      exec_mode: "fork",
      instances: "1",
      wait_ready: true,
      autorestart: false,
      max_restarts: 5,
      interpreter : "python"
    }
  ]
}
