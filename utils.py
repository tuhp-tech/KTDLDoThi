import matplotlib.pyplot as plt
import networkx as nx
from os.path import join

from constant import SAVE_DEG_DIST_IMG


def cal_degree_distribution(graph):
	degs = {}
	for node in graph.nodes():
		deg = graph.degree(node)

		if deg not in degs:
			degs[deg] = 0
		degs[deg] += 1

	return sorted(degs.items())

def save_deg_dist_img_plt(
	data, 
	plot_tilte, 
	png_file_name
):

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot([k for (k, v) in data], [v for (k, v) in data])
	ax.set_xscale('log')
	ax.set_yscale('log')

	plt.title('Degree Distribution if ' + plot_tilte)
	fig.savefig(
		join(
			SAVE_DEG_DIST_IMG,
			png_file_name
		)
	)
	plt.clf()


def save_multi_format_graph_img(
	g, 
	save_path,
	suffix=""
):
	nx.draw(g, width=0.5)
	plt.savefig(
		join(
			save_path,
			suffix + '.png'
		)
	)
	plt.clf()

	nx.draw_random(g, width=0.5)
	plt.savefig(
		join(
			save_path,
			'draw_random_' + suffix + '.png'
		)
	)
	plt.clf()

	nx.draw_circular(g, width=0.5)
	plt.savefig(
		join(
			save_path,
			'draw_circular_' + suffix + '.png'
		)
	)
	plt.clf()

	nx.draw_spectral(g, width=0.5)
	plt.savefig(
		join(
			save_path,
			'draw_spectral_' + suffix + '.png'
		)
	)
	plt.clf()