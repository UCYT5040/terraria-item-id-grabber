from os import system
from os.path import isfile
from re import findall
from json import dump

STEAM_PATH = '"C:\\Program Files (x86)\\Steam\\steamapps\\common\\Terraria\\TerrariaServer.exe"'
ITEM_ID_REGEX = r'public const short ([A-Za-z]+) = (\d+)'


def main():
    path = None
    if isfile(STEAM_PATH.replace('"', '')):
        print('The Terraria binaries have been found.')
        path = STEAM_PATH
    while not path:
        path = input('Please enter the path to the Terraria directory: ') + '\\TerrariaServer.exe'
        if not isfile(path):
            print('The path you entered is invalid.')
            path = None
    print("Decompiling...")
    system(f'ilspycmd {path} -o Decompiled -t Terraria.ID.ItemID')
    print("Decompilation complete.")
    print("Saving item IDs to item_ids.json...")
    with open('Decompiled/Terraria.ID.ItemID.decompiled.cs') as f:
        item_ids = dict(findall(ITEM_ID_REGEX, f.read()))
    item_ids = {name: int(identifier) for name, identifier in item_ids.items()}
    dump(item_ids, open('item_ids.json', 'w'))
    print("Item IDs saved to item_ids.json.")


if __name__ == '__main__':
    main()
