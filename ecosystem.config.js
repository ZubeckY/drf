module.exports = {
   apps:
      [{
        name: "apiLavka",
        script: "drfsite/manage.py",
        args: ["runserver", "81.200.119.121:8000"],
        exec_mode: "fork",
        instances: "1",
        wait_ready: true,
        autorestart: false,
        max_restarts: 5,
        interpreter : "python"
      }]
}