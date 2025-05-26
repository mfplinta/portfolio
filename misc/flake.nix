{
  description = "Portfolio flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        system = system;
        config.allowUnfree = true;
      };
      django-imagekit = ps: ps.callPackage ./django-imagekit.nix {};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          (python3.withPackages (ps: [
          ps.django
          ps.pillow
          ps.gunicorn
          ps.whitenoise
          ps.django-markdownx
          (django-imagekit ps)
          ]))
        ];
      };
    };
}
