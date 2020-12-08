

from generate_graph import gen_hexagonal_lattice_graph, \
							gen_random_graph_fast_gnp, \
							gen_classic_balance_tree, \
							gen_expanders_margulis_gabber_galil_graph, \
							gen_random_k_out_graph, \
							gen_waxman_graph, \
							gen_gn_graph, \
							gen_random_internet_as_graph


from constant import RANDOM_CONNECT_RATIO, \
						RANDOM_NO_NODES, \
						CLASSIC_NUM_CHILD, \
						CLASSIC_HEIGHT, \
						EXPANDER_NO_NODES, \
						HEXA_LATTICE_ROWS, \
						HEXA_LATTICE_COLUMNS, \
						K_OUT_DEGREES, \
						K_OUT_NODES, \
						WAXMAN_GRAPH_NODES, \
						GN_GRAPH_NODES, \
						RANDOM_INTERNET_AS_GRAPH_NODES


if __name__=='__main__':
	gen_random_graph_fast_gnp(
		no_nodes=RANDOM_NO_NODES,
		connect_ratio=RANDOM_CONNECT_RATIO
	)

	gen_classic_balance_tree(
		child_node=CLASSIC_NUM_CHILD,
		height=CLASSIC_HEIGHT
	)

	gen_expanders_margulis_gabber_galil_graph(
		no_nodes=EXPANDER_NO_NODES
	)

	gen_hexagonal_lattice_graph(
		hexa_rows=HEXA_LATTICE_ROWS,
		hexa_cols=HEXA_LATTICE_COLUMNS
	)

	gen_random_k_out_graph(
		no_nodes=K_OUT_NODES,
		out_degrees=K_OUT_DEGREES
	)

	gen_waxman_graph(
		no_nodes=WAXMAN_GRAPH_NODES
	)

	gen_gn_graph(
		no_nodes=GN_GRAPH_NODES
	)

	gen_random_internet_as_graph(
		no_nodes=RANDOM_INTERNET_AS_GRAPH_NODES
	)