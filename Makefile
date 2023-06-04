PYTHON:=python3
TASS:=64tass

##########################################################################
##########################################################################

PWD:=$(shell $(PYTHON) submodules/shellcmd.py/shellcmd.py realpath .)

SHELLCMD:=$(PYTHON) "$(PWD)/submodules/shellcmd.py/shellcmd.py"

BUILD:=$(PWD)/build
BEEB_BUILD:=$(PWD)/beeb/ADJI/z
BEEB_BIN:=$(PWD)/submodules/beeb/bin

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

	$(_V)$(PYTHON) tools/print_key_tables.py >"$(BUILD)/generated_key_tables.s65"

	$(_V)$(TASS) $(TASS_ARGS) -Ddebug=false "--list=$(BUILD)/ADJIROM.lst" "--output=$(BUILD)/ADJIROM.bin" "--map=$(BUILD)/ADJIROM.map" ADJIROM.s65
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

##########################################################################
##########################################################################

.PHONY:rel
rel: GIT_VER:=$(shell git log -1 '--format=%cd-%h' '--date=format:%Y%m%d-%H%M%S')
rel: SSD_PATH:=$(BUILD)/adji-$(GIT_VER).ssd
rel: ZIP_PATH:=$(BUILD)/ADJI-$(GIT_VER).zip
rel: DIRTY_CHECK_PREFIX:=$(if $(DIRTY_OK),-,)
rel:
	$(_V)echo Checking for unmodified working copy.
	$(DIRTY_CHECK_PREFIX)$(_V)git diff-index --quiet --cached HEAD --
	$(DIRTY_CHECK_PREFIX)$(_V)git diff-files --quiet
	$(_V)$(MAKE) build
	$(_V)$(SHELLCMD) blank-line
	$(_V)$(PYTHON) $(BEEB_BIN)/ssd_create.py -o "$(SSD_PATH)" "$(BEEB_BUILD)/$$.ADJIROM" "$(BEEB_BUILD)/D.ADJIROM"
	$(_V)zip -9j "$(ZIP_PATH)" "$(BUILD)/ADJIROM.bin" "$(BUILD)/ADJIROM_debug.bin" "$(SSD_PATH)"
	$(_V)echo ZIP file: $(ZIP_PATH)
