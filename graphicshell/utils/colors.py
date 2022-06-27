"""
@author: jormungandr1105
@desc: defines colors to be used by the terminal
@created: 06/25/2022
"""

reg = {}
reg["black"] = "\033[30m"
reg["red"] = "\033[31m"
reg["green"] = "\033[32m"
reg["yellow"] = "\033[33m"
reg["blue"] = "\033[34m"
reg["purple"] = "\033[35m"
reg["cyan"] = "\033[36m"
reg["white"] = "\033[37m"

bold = {}
bold["black"] = "\033[1;30m"
bold["red"] = "\033[1;31m"
bold["green"] = "\033[1;32m"
bold["yellow"] = "\033[1;33m"
bold["blue"] = "\033[1;34m"
bold["purple"] = "\033[1;35m"
bold["cyan"] = "\033[1;36m"
bold["white"] = "\033[1;37m"

underline = {}
underline["black"] = "\033[4;30m"
underline["red"] = "\033[4;31m"
underline["green"] = "\033[4;32m"
underline["yellow"] = "\033[4;33m"
underline["blue"] = "\033[4;34m"
underline["purple"] = "\033[4;35m"
underline["cyan"] = "\033[4;36m"
underline["white"] = "\033[4;37m"

back = {}
back["black"] = "\033[40m"
back["red"] = "\033[41m"
back["green"] = "\033[42m"
back["yellow"] = "\033[43m"
back["blue"] = "\033[44m"
back["purple"] = "\033[45m"
back["cyan"] = "\033[46m"
back["white"] = "\033[47m"

reset = "\033[0m"


if __name__ == '__main__':
	pass
