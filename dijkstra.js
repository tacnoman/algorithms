const INFINITY = 999999999999;
const dijkstra = (graph, start) => {
  const shortestDistance = {};

  Object.keys(graph).forEach(key => {
    shortestDistance[key] = INFINITY;
  });

  shortestDistance[start] = 0;
  const unvisitedNodes = { ...graph };

  while (Object.keys(unvisitedNodes).length > 0) {
    const minimumDistanceKey = Object.keys(unvisitedNodes).reduce((prev, curr) => {
      if (!prev) return curr;
      return (shortestDistance[curr] < shortestDistance[prev]) ? curr : prev;
    }, null);

    const nodes = unvisitedNodes[minimumDistanceKey];
    const currentWeight = shortestDistance[minimumDistanceKey];

    Object.entries(nodes).forEach(([nodeKey, weight]) => {
      const newWeight = weight + currentWeight;
      shortestDistance[nodeKey] = Math.min(newWeight, shortestDistance[nodeKey]);
    });
    delete unvisitedNodes[minimumDistanceKey];
  }

  return shortestDistance;
};

const graph = {
  a: {b: 3, c: 4, d: 7},
  b: {c: 1, f: 5},
  c: {f: 6, d: 2},
  d: {e: 3, g: 6},
  e: {g: 3, h: 4},
  f: {e: 1, h: 8},
  g: {h: 2},
  h: {g: 2},
};

console.log(dijkstra(graph, 'a'));