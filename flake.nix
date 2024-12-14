{
  description = "Cisco DevNet Training Shell";

  inputs = {
    nixpkgs.url =
      "github:nixos/nixpkgs?ref=nixos-24.11";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };

      pythonModules = with pkgs.python312Packages; [
        pip
        requests
        ncclient
        pyaml
        netmiko
        xmltodict
      ];
    in {
      devShells.${system}.default = pkgs.mkShellNoCC {
        packages = with pkgs; [
          neovim
          ripgrep
          bat
          meld
          git
          tig
          nixfmt-rfc-style
          curl
          python312Full
        ] ++ pythonModules;
      };
    };
}

