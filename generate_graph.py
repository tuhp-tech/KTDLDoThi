import networkx as nx

from utils import save_deg_dist_img_plt, \
					save_multi_format_graph_img, \
					cal_degree_distribution


def gen_random_graph_fast_gnp(
	no_nodes=100, 
	connect_ratio=0.4
):
	from constant import RANDOM_FAST_GNP

	# generate graph
	fast_gnp = nx.fast_gnp_random_graph(
		no_nodes, 
		connect_ratio
	)

	deg_dist = cal_degree_distribution(fast_gnp)

	save_multi_format_graph_img(
		g=fast_gnp, 
		save_path=RANDOM_FAST_GNP,
		suffix='fast_gnp'
	)

	save_deg_dist_img_plt(
		deg_dist,
		'fast_gnp_random_graph',
		'fast_gnp_random_graph_deg_dist.png'
	)

def gen_classic_balance_tree(
	child_node=5, 
	height=10
):
	from constant import CLASSIC_BALANCE_TREE

	# generate graph
	balance_tree = nx.balanced_tree(
		child_node, 
		height
	)

	deg_dist = cal_degree_distribution(balance_tree)

	save_multi_format_graph_img(
		g=balance_tree, 
		save_path=CLASSIC_BALANCE_TREE,
		suffix='balance_tree'
	)

	save_deg_dist_img_plt(
		deg_dist,
		'classic_balance_tree',
		'classic_balance_tree_deg_dist.png'
	)

def gen_expanders_margulis_gabber_galil_graph(
	no_nodes=100
):
	from constant import EXPANDER_MARGULIS_GABBER

	# generate graph
	expanders = nx.margulis_gabber_galil_graph(
		no_nodes
	)

	deg_dist = cal_degree_distribution(expanders)

	save_multi_format_graph_img(
		g=expanders, 
		save_path=EXPANDER_MARGULIS_GABBER,
		suffix='expanders_margulis'
	)

	save_deg_dist_img_plt(
		deg_dist,
		'expander_margulis_gabber',
		'expander_margulis_gabber_deg_dist.png'
	)


def gen_hexagonal_lattice_graph(
	hexa_rows=2,
	hexa_cols=2
):
	from constant import HEXA_LATTICE

	# generate graph
	hexa_lattice = nx.hexagonal_lattice_graph(
		hexa_rows,
		hexa_cols
	)

	deg_dist = cal_degree_distribution(hexa_lattice)

	save_multi_format_graph_img(
		g=hexa_lattice, 
		save_path=HEXA_LATTICE,
		suffix='hexa_lattice'
	)

	save_deg_dist_img_plt(
		deg_dist,
		'hexa_lattice',
		'hexa_lattice_deg_dist.png'
	)


def gen_random_k_out_graph(
	no_nodes=50,
	out_degrees=10
):
	from constant import K_OUT_GRAPH

	# generate graph
	k_out = nx.hexagonal_lattice_graph(
		no_nodes,
		out_degrees
	)

	deg_dist = cal_degree_distribution(k_out)

	save_multi_format_graph_img(
		g=k_out, 
		save_path=K_OUT_GRAPH,
		suffix='k_out'
	)

	save_deg_dist_img_plt(
		deg_dist,
		'k_out',
		'k_out_deg_dist.png'
	)


def gen_waxman_graph(
	no_nodes=50,
	beta=0.4,
	alpha=0.1
):
	from constant import WAXMAN_GRAPH

	# generate graph
	waxman_graph = nx.waxman_graph(
		no_nodes,
		beta,
		alpha
	)

	deg_dist = cal_degree_distribution(waxman_graph)

	save_multi_format_graph_img(
		g=waxman_graph, 
		save_path=WAXMAN_GRAPH,
		suffix='waxman_graph'
	)

	save_deg_dist_img_plt(
		deg_dist,
		'waxman_graph',
		'waxman_graph_deg_dist.png'
	)


def gen_gn_graph(
	no_nodes=50,
):
	from constant import GN_GRAPH

	# generate graph
	gn_graph = nx.gn_graph(
		no_nodes,
	)

	deg_dist = cal_degree_distribution(gn_graph)

	save_multi_format_graph_img(
		g=gn_graph, 
		save_path=GN_GRAPH,
		suffix='gn_graph'
	)

	save_deg_dist_img_plt(
		deg_dist,
		'gn_graph',
		'gn_graph_deg_dist.png'
	)


def gen_random_internet_as_graph(
	no_nodes=50,
):
	from constant import RANDOM_INTERNET_AS_GRAPH

	# generate graph
	random_internet_as_graph = nx.random_internet_as_graph(
		no_nodes,
	)

	deg_dist = cal_degree_distribution(random_internet_as_graph)

	save_multi_format_graph_img(
		g=random_internet_as_graph, 
		save_path=RANDOM_INTERNET_AS_GRAPH,
		suffix='random_internet_as_graph'
	)

	save_deg_dist_img_plt(
		deg_dist,
		'random_internet_as_graph',
		'random_internet_as_graph_deg_dist.png'
	)


