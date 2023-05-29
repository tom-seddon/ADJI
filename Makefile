PYTHON:=python3
TASS:=64tass

##########################################################################
##########################################################################

PWD:=$(shell $(PYTHON) submodules/shellcmd.py/shellcmd.py realpath .)

SHELLCMD:=$(PYTHON) "$(PWD)/submodules/shellcmd.py/shellcmd.py"

BUILD:=$(PWD)/build
BEEB_BUILD:=$(PWD)/beeb/ADJI/z

##########################################################################
##########################################################################

_V:=$(if $(VERBOSE),time ,@)

##########################################################################
##########################################################################

TASS_ARGS:=--quiet --nostart --case-sensitive -Wall --verbose-list --long-branch

##########################################################################
##########################################################################

.PHONY:build
build:
	$(_V)$(SHELLCMD) mkdir "$(BUILD)"
	$(_V)$(SHELLCMD) mkdir "$(BEEB_BUILD)"

	$(_V)$(TASS) $(TASS_ARGS) -Ddebug=false "--list=$(BUILD)/ADJIROM.lst" "--output=$(BUILD)/ADJIROM.bin" ADJIROM.s65
	$(_V)$(TASS) $(TASS_ARGS) -Ddebug=true "--list=$(BUILD)/ADJIROM_debug.lst" "--output=$(BUILD)/ADJIROM_debug.bin" ADJIROM.s65

	$(_V)$(SHELLCMD) copy-file "$(BUILD)/ADJIROM.bin" "$(BEEB_BUILD)/$$.ADJIROM"
	$(_V)$(SHELLCMD) copy-file "$(BUILD)/ADJIROM_debug.bin" "$(BEEB_BUILD)/D.ADJIROM"
	$(_V)$(SHELLCMD) blank-line
	$(_V)$(SHELLCMD) stat "$(BUILD)/ADJIROM.bin"
	$(_V)$(SHELLCMD) stat "$(BUILD)/ADJIROM_debug.bin"

##########################################################################
##########################################################################

.PHONY:clean
clean:
	$(_V)$(SHELLCMD) rm-tree "$(BUILD)"
	$(_V)$(SHELLCMD) rm-tree "$(BEEB_BUILD)"
