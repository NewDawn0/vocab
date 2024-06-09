# Vocab

A cli vocabulary learning tool

## Table of contents

<!-- vim-markdown-toc GFM -->

* [Installation](#installation)
    * [Using Nix](#using-nix)
    * [From source](#from-source)
* [Usage](#usage)
    * [Basic usage](#basic-usage)
    * [Flags](#flags)
        * [File path](#file-path)
        * [Swapping answers and questions](#swapping-answers-and-questions)
        * [Setting the seperator](#setting-the-seperator)
        * [Automatic translation](#automatic-translation)
    * [Defining vocab files](#defining-vocab-files)

<!-- vim-markdown-toc -->

## Installation

### Using Nix

1. Add the vocab to your inputs

   ```nix
   {
       inputs.vocab = {
           url = "github:NewDawn0/vocab";
           inputs.nixpkgs.follows = "nixpkgs";
           # Optional if you use nix-systems
           inputs.nix-systems.follows = "nix-systems";
       };
   }
   ```

2. The overlay

   ```nix
   overlays = [ inputs.vocab.overlays.default ];
   ```

3. Add it to your packages

   ```nix
    home.packages = with pkgs; [ vocab ];
    # Or
    environment.systemPackages = with pkgs; [ vocab ];

   ```

### From source

1. Install [Rust](https://www.rust-lang.org) using [rustup](https://rustup.rs)
2. Install [tl](https://github.com/NewDawn0/tl) using the below command:
   ```bash
   cargo install --git https://github.com/NewDawn0/tl
   ```
3. Clone the repo:
   ```bash
   git clone --depth 1 https://github.com/NewDawn0/vocab
   cd vocab
   ```
4. Install vocab using pip:
   ```bash
   pip install .
   ```

## Usage

```bash
vocab -f <your vocab file>
```

### Basic usage

Use the `-f <path>` or `--file <path>` flags to point to your wordlist.

This is the **only required argument**

### Flags

#### File path

Use the `-f <path>` or `--file <path>` flags to point to your wordlist.

- This is the **only required argument**

#### Swapping answers and questions

To swap answers and questions meaning for a given answer you have to provide the question, use the `--switch` flag

#### Setting the seperator

Use `-s <seperator string>` | `--seperator <string>` to set the seperator string

- This argument is useless when vocab is in translation mode

#### Automatic translation

Use the `-t <source lang> <target lang>` or `--translate <source lang> <target lang>` to automatically translate the questions thereby generating the answers

- For all available languages either run `tl --help` and check the languages section or visit [the repo](https://github.com/NewDawn0/tl) and check the languages section in the program description

### Defining vocab files

A vocab file is a list of questions and answers seperated by a seperator string
In the `examples` directory you'll find example word lists/vocab files
The default seperator is a pipe `|` symbol however this can easily be changed by setting the seperator using `-s <seperator string>` or `--seperator <seperator string>`
Writing anwers can be omitted by letting the program automatically translate them using the `-t <source lang> <target lang>` or `--translate <source lang> <target lang>` flags which enable translation using [Google translate](https://translate.google.com)
