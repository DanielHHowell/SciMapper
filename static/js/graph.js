const Graph = ForceGraph3D()
  (document.getElementById('3d-graph'))
    .jsonUrl('network.json')
    .nodeAutoColorBy('group')
    .linkOpacity(0.5)
    .nodeThreeObject(node => {
      const sprite = new SpriteText(node.id);
      sprite.color = node.color;
      sprite.textHeight = 8;
      return sprite;
    });
// Spread nodes a little wider
Graph.d3Force('charge').strength(-500);