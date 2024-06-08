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
            name = "vocab";
            propagatedBuildInputs = with pkgs; [ tl ];
            src = ./.;
            buildInputs = with pkgs.python3Packages; [ setuptools ];
          };
        });
    };
}
