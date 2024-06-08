{
  description = "ND-NVim flake";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    nix-systems.url = "github:nix-systems/default";
  };

  outputs = { self, nixpkgs, ... }@inputs:
    let eachSystem = nixpkgs.lib.genAttrs (import inputs.nix-systems);
    in {
      packages = eachSystem (system:
        let pkgs = nixpkgs.legacyPackages.${system};
        in {
          default = pkgs.python3Packages.buildPythonPackage {
            name = "vocab";
            src = ./.;
            buildInputs = with pkgs.python3Packages; [ setuptools ];
          };
        });
    };
}
