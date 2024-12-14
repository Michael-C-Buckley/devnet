# Development Flake

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
    in {
      devShells.${system}.default = pkgs.mkShellNoCC {
        packages = with pkgs; [
          # Local utilities
          neovim
          git
          tig
          nixfmt-rfc-style
          curl

          # Python
          python312Full
          python312Packages.requests
          python312Packages.ncclient
          python312Packages.pyaml
          python312Packages.netmiko
          python312Packages.xmltodict
        ];
      };
    };
}

