all: clean c mine
	@cp Makefile c/n
	@echo ---
	@make mine
	@echo ---
	@tree -asF c
c:     ; mkdir -p c/n ; touch c/n/genesis.yaml
mine:  ; @sh mine.sh
clean: ; rm -fr c *~
