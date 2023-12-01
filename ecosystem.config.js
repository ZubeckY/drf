module.exports = {
   apps:
      [{
        name: "apiLavka",
        script: "drfsite/manage.py",
        args: ["runserver", "31.129.111.110:8000"],
        exec_mode: "fork",
        instances: "1",
        wait_ready: true,
        autorestart: false,
        max_restarts: 5,
        interpreter : "python"
      }]
}