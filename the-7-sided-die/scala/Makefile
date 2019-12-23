DIR=target

all: compile run

compile:
	@[ -d $(DIR) ] || mkdir $(DIR) 
	@scalac *.scala -d $(DIR)

run:
	@scala -classpath $(DIR) Die

clean:
	@[ ! -d $(DIR) ] || rm -r $(DIR)
