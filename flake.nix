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
        debugpy
        requests
        ncclient
        pyaml
        netmiko
        xmltodict
        wheel
        setuptools
        mypy
      ];
    in {
      devShells.${system}.default = pkgs.mkShellNoCC {
        packages = with pkgs; [
          direnv
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

        shellHook = ''
          export IOS_XE1="192.168.48.25"
          export IOS_USER="michael"
          export IOS_PW="asdfasdf"
        '';
      };
    };
}

