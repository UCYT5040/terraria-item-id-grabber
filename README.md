# ID Grabber

Automatically get item IDs from Terraria binaries.

## Installation

Because the script is dealing with decompiling Terraria binaries, it requires that you install `ilspycmd`.

You can quickly install that on Windows:

```bash
winget install Microsoft.DotNet.SDK.6
```

Please accept the license agreement and then run the following commands:

```bash
dotnet nuget add source "https://api.nuget.org/v3/index.json" --name "nuget.org"
dotnet tool install --global ilspycmd
```

After that, make sure you have Python installed.

## Usage

To use the script, run it like you would any other Python script:

```bash
py main.py
# or
python main.py
# or
python3 main.py
```