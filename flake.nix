{
  description = "ND-NVim flake";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    nix-systems.url = "github:nix-systems/default";
    tl = {
      url = "github:NewDawn0/tl";
      inputs.nixpkgs.follows = "nixpkgs";
      inputs.nix-systems.follows = "nix-systems";
    };
  };

  outputs = { self, nixpkgs, ... }@inputs:
    let eachSystem = nixpkgs.lib.genAttrs (import inputs.nix-systems);
    in {
      overlays.default =
        (final: prev: { vocab = self.packages.${prev.system}.default; });
      packages = eachSystem (system:
        let
          pkgs = import nixpkgs {
            inherit system;
            config = { };
            overlays = [
              (final: prev: { tl = inputs.tl.packages.${prev.system}.default; })
            ];
          };
        in {
          default = pkgs.python3Packages.buildPythonPackage {
            pname = "vocab";
            version = "1.0.0";
            propagagedBuildInputs = with pkgs; [ tl ];
            buildInputs = with pkgs.python3Packages; [ setuptools ];
            src = ./.;
            meta = {
              description =
                "An efficient CLI-based tool for vocabulary learning";
              longDescription = ''
                This command-line tool helps you learn and memorize vocabulary efficiently.
                It provides a simple way to learn vocabulary from a file, with autocorrection and automatic translation.
              '';
              homepage = "https://github.com/NewDawn0/vocab";
              license = pkgs.lib.licenses.mit;
              maintainers = with pkgs.lib.maintainers; [ NewDawn0 ];
              platforms = pkgs.lib.platforms.all;
            };
          };
        });
    };
}
