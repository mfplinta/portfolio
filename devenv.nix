{ config, pkgs, ... }:
{
  languages.python = {
    enable = true;
    venv = {
      enable = true;
      requirements = ./requirements.txt;
    };
  };

  processes.runserver = {
    ports.http.allocate = 8000;
    exec = "python manage.py runserver ${toString config.processes.runserver.ports.http.value}";
  };

  processes.staticfiles = {
    exec = "python manage.py collectstatic --noinput";
    watch = {
      paths = [ ./main/static/main ];
    };
  };
}
