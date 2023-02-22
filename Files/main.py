# from os import listdir, path
#
#
# def travers_dir(curr_path, files_by_ext):
#      for el in listdir(curr_path):
#         if path.isdir(path.join(curr_path, el)):
#             travers_dir(path.join(curr_path, el), files_by_ext)
#         else:
#             extension = el.split(".")[-1]
#             if extension not in files_by_ext:
#                  files_by_ext[extension] = []
#             files_by_ext[extension].append(el)
#
# files_by_ext = {}
# travers_dir(".", files_by_ext)
#
# for ext, files in sorted(files_by_ext.items()):
#     print(f'.{ext}')
#     for file in sorted(files):
#         print(f'---{file}')

from os import walk

files_by_ext = {}
for root,dirs,files in walk("."):
    for file in files:
        extension = file.split(".")[-1]
        if extension not in files_by_ext:
            files_by_ext[extension] = []
        files_by_ext[extension].append(file)

with open('result.txt','w') as output:
    for extension,files in sorted(files_by_ext.items()):
        output.write(f'.{extension}\n')
        for file in sorted(files):
            output.write(f'---{file}\n')
