SHELL := /bin/bash
.PHONY: config
.DEFAULT_GOAL := config

CFGOUTDIR=.
EXCELDIR=.
EXCEL=$(notdir $(wildcard $(EXCELDIR)/*.xlsx))
CFG_ERL=$(patsubst %.xlsx, $(CFGOUTDIR)/cfg_%.erl,$(EXCEL))
CFG_CC=python gen_config.py 

config:$(CFG_ERL)

$(CFGOUTDIR)/cfg_%.erl:$(EXCELDIR)/%.xlsx
	$(CFG_CC) $^ $(CFGOUTDIR)
