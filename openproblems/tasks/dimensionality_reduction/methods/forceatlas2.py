from ....tools.decorators import method
from ....tools.utils import check_version

import scanpy as sc


@method(
    method_name="ForceAtlas2",
    paper_name="ForceAtlas2, a Continuous Graph Layout Algorithm for Handy Network"
    "Visualization Designed for the Gephi Software",
    paper_url="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0098679",
    paper_year=2014,
    code_url="https://scanpy.readthedocs.io/en/stable/api/scanpy.tl.draw_graph.html",
    code_version=check_version("fa2"),
    image="andrew-method-forceatlas2-dim-reduction-python-extras",
)
def forceatlas2(adata):
    sc.pp.pca(adata)
    sc.pp.neighbors(adata, use_rep="X_pca")
    sc.tl.draw_graph(adata)

    adata.obsm["X_forceatlas2"] = adata.obsm["X_draw_graph_fa"]
    adata.obsm["X_emb"] = adata.obsm["X_forceatlas2"]

    return adata
