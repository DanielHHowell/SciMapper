SciMapper is a way to visualize a scientific concept's linguistic space.
It takes a central search term and performs basic natural language processing on the abstracts of the most relevant articles, in order to identify likely related concepts.  
It then performs the same function on each of these terms to generate a network of connections between all concepts and the central search term.

Currently only the NCBI is being utilized, which focuses mainly on biological journal articles.

It is powered with Python and the [3D Force-Directed Graph](https://github.com/vasturiano/3d-force-graph) JavaScript library.   