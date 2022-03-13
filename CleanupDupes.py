import os

# Had an issue with duplicate files being created by a piece of software
# with filenames that included the duplicate's extention.
# Ex: foo.bar, foo.bar.bar, foo.bar.bar.bar, etc.
#
# This script searches for files with extensions in their name and deletes them.
# Speed of the script was not a concern, only the speed of writing it.

def main():
	print("Cleaning up duplicate files\n")
	
	delete_list = []
	path_root = "./"
	folder_scan = os.scandir(path_root)
	for folder in folder_scan:
		if folder.is_dir():
			print("Found folder named: " + folder.name)
			file_scan = os.scandir(path_root + folder.name)
			for file in file_scan:
				file_tup = os.path.splitext(file.name)
				if file_tup[1] in file_tup[0]:
					delete_list.append(file)
	
	print("The following files will be deleted:")
	for victim in delete_list:
		print(victim.path)
	
	user_str = input("Continue? Type [Y] to Confirm:  ")
	if user_str == 'Y' or user_str == 'y':
		for victim in delete_list:
			os.remove(victim.path)
			print("Deleted >" + victim.path)
	else:
		print("Delete Aborted.")
	
	print("Done.")
	
if __name__ == "__main__":
    main()