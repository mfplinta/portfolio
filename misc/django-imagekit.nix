{
  lib,
  buildPythonPackage,
  django,
  fetchFromGitHub,
  pillow,
  pythonOlder,
  pilkit,
  django-appconf,
  setuptools,
}:

buildPythonPackage rec {
  pname = "django-webp";
  version = "5.0.0";
  pyproject = true;

  disabled = pythonOlder "3.7";

  src = fetchFromGitHub {
    owner = "matthewwithanm";
    repo = "django-imagekit";
    rev = "master";
    hash = "sha256-OESWH2Gw2HdubfxWocG1Os3grN4IdbbJKW1n6fl94Dc=";
  };

  nativeBuildInputs = [ setuptools ];

  propagatedBuildInputs = [
    django
    pillow
    pilkit
    django-appconf
  ];

  # tests only executable in vagrant
  doCheck = false;

  meta = with lib; {
    description = "Speeds up static file load times by generating a webp image to load to a webpage instead of a jpg, gif or png";
    homepage = "https://github.com/Zima2115/django-webp";
    changelog = "https://github.com/Zima2115/django-webp";
    license = licenses.bsd2;
  };
}
