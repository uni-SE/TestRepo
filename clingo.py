import clingo

def main(prg):
	prg.add("p", ["t"], "q(t).")
	prg.gound([("p", [2])])
	prg.solve()

main("q(t)")
