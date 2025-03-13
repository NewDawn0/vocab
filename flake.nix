{
  description = "Easily learn your vocabulary";

  inputs.utils.url = "github:NewDawn0/nixUtils";

  outputs = { self, utils, ... }: {
    overlays.default = final: prev: {
      vocab = self.packages.${prev.system}.default;
    };
    packages = utils.lib.eachSystem { } (pkgs: {
      default = pkgs.python3Packages.buildPythonPackage {
        pname = "vocab";
        version = "1.0.0";
        propagagedBuildInputs = with pkgs; [ translate ];
        buildInputs = with pkgs.python3Packages; [ setuptools ];
        src = ./.;
        meta = {
          description = "Easily learn your vocabulary";
          longDescription =
            "A CLI tool to help you learn and memorize vocabulary efficiently with features such as autocorrection and automatic translation";
          homepage = "https://github.com/NewDawn0/vocab";
          license = pkgs.lib.licenses.mit;
          maintainers = with pkgs.lib.maintainers; [ NewDawn0 ];
          platforms = pkgs.lib.platforms.all;
        };
      };
    });
  };
}
