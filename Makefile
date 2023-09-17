ifeq ($(OS),Windows_NT)
TASS?=bin\64tass.exe
PYTHON?=py -3
else
TASS?=64tass
PYTHON?=python3
endif

##########################################################################
##########################################################################

PWD:=$(shell $(PYTHON) submodules/shellcmd.py/shellcmd.py realpath .)

SHELLCMD:=$(PYTHON) "$(PWD)/submodules/shellcmd.py/shellcmd.py"

BUILD:=$(PWD)/build
BEEB_BUILD:=$(PWD)/beeb/ADJI/z
BEEB_BIN:=$(PWD)/submodules/beeb/bin

##########################################################################
##########################################################################

_V:=$(if $(VERBOSE),,@)

##########################################################################
##########################################################################

BUILD_TIME:=$(shell $(SHELLCMD) strftime -d _ _Y_m_d-_H_M_S)

TASS_ARGS:=$(if $(VERBOSE),,--quiet) --nostart --case-sensitive -Wall --verbose-list --long-branch "-Dbuild_time=\"$(BUILD_TIME)\""

TASS_OUTPUTS="--output=$(BUILD)/$1.bin" "--list=$(BUILD)/$1.lst" "--map=$(BUILD)/$1.map"


##########################################################################
##########################################################################

.PHONY:build
build: _DEBUG_TIME:=
build:
	$(_V)$(SHELLCMD) mkdir "$(BUILD)"
	$(_V)$(SHELLCMD) mkdir "$(BEEB_BUILD)"

	$(_V)$(PYTHON) tools/print_key_tables.py >"$(BUILD)/generated_key_tables.s65"

	$(_V)$(TASS) $(TASS_ARGS) -Dsingle_fire_button=false -Ddebug=false $(call TASS_OUTPUTS,ADJIROM) ADJIROM.s65
	$(_V)$(TASS) $(TASS_ARGS) -Dsingle_fire_button=false -Ddebug=true $(call TASS_OUTPUTS,ADJIROM_debug) ADJIROM.s65
	$(_V)$(TASS) $(TASS_ARGS) -Dsingle_fire_button=true -Ddebug=false $(call TASS_OUTPUTS,ADJIROM_1fire) ADJIROM.s65
	$(_V)$(TASS) $(TASS_ARGS) -Dsingle_fire_button=true -Ddebug=true $(call TASS_OUTPUTS,ADJIROM_1fire_debug) ADJIROM.s65

	$(_V)$(SHELLCMD) copy-file "$(BUILD)/ADJIROM.bin" "$(BEEB_BUILD)/$$.ADJI"
	$(_V)$(SHELLCMD) copy-file "$(BUILD)/ADJIROM_debug.bin" "$(BEEB_BUILD)/D.ADJI"
	$(_V)$(SHELLCMD) copy-file "$(BUILD)/ADJIROM_1fire.bin" "$(BEEB_BUILD)/$$.ADJI1F"
	$(_V)$(SHELLCMD) copy-file "$(BUILD)/ADJIROM_1fire_debug.bin" "$(BEEB_BUILD)/D.ADJI1F"

	$(_V)$(SHELLCMD) blank-line
	$(_V)$(SHELLCMD) stat --size-budget 4096 "$(BUILD)/ADJIROM.bin"
	$(_V)$(SHELLCMD) stat --size-budget 4096 "$(BUILD)/ADJIROM_1fire.bin"
	$(_V)$(SHELLCMD) stat "$(BUILD)/ADJIROM_debug.bin"
	$(_V)$(SHELLCMD) stat "$(BUILD)/ADJIROM_1fire_debug.bin"
	$(_V)$(SHELLCMD) blank-line
	$(_V)$(SHELLCMD) sha1 "$(BUILD)/ADJIROM.bin"

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
	$(_V)$(PYTHON) $(BEEB_BIN)/ssd_create.py -o "$(SSD_PATH)" "$(BEEB_BUILD)/$$.ADJI" "$(BEEB_BUILD)/D.ADJI" "$(BEEB_BUILD)/$$.ADJI1F" "$(BEEB_BUILD)/D.ADJI1F"
	$(_V)zip -9j "$(ZIP_PATH)" "$(BUILD)/ADJIROM.bin" "$(BUILD)/ADJIROM_debug.bin" "$(BUILD)/ADJIROM_1fire.bin" "$(BUILD)/ADJIROM_1fire_debug.bin" "$(SSD_PATH)"
	$(_V)echo ZIP file: $(ZIP_PATH)
