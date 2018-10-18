import sys
import re

# Convert a linux path to windows path
# Should handle cases with spaces like:
# Test cases:
#
# 1. with spaces, should return path with quotes
# ./abc\ def/file -> ".\abc def\file"
#
# 2. handle different drives in windows subsystems: C drive is in pth /mnt/c/
# /mnt/c -> C:\
#
# 3. Check invalid path: in this case, throw exceptions
#
def linuxPathToWindows( linuxPath ):

	# Deal with drive symbol, like /mnt/c
	drivePattern = "/mnt/[a-z]"
	if re.match(drivePattern, linuxPath):
		driveSymbol = re.match(drivePattern, linuxPath).group(0)[-1].upper() # last character is drive symbol
		print("drive symbol=", driveSymbol);
		linuxPath = re.sub(drivePattern, driveSymbol+":", linuxPath)

	spaceFlag = False # by default no spaces in linux Path

	if linuxPath.find(" ") != -1:
		spaceFlag = True

	windowsPath = linuxPath.replace("\\", "")
	windowsPath = windowsPath.replace("/", "\\")

	if spaceFlag:
		return "\"" + windowsPath + "\""
	else:
		return windowsPath



if __name__ == "__main__":
	path = "test\\ 1/"

	if len(sys.argv) > 1:
		path = sys.argv[1]
		print(path)

	print(linuxPathToWindows(path) )


	