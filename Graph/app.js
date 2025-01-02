// Import libraries
// D3.js can be included via CDN: <script src="https://d3js.org/d3.v7.min.js"></script>

// Cities and connections data
const cities = ["CityA", "CityB", "CityC", "CityD", "CityE"];
const connections = [
    ["CityA", "CityB", 5],
    ["CityA", "CityC", 10],
    ["CityB", "CityD", 2],
    ["CityC", "CityD", 1],
    ["CityD", "CityE", 7]
];

// Create the graph as an adjacency list
const graph = new Map();
connections.forEach(([city1, city2, distance]) => {
    if (!graph.has(city1)) graph.set(city1, []);
    if (!graph.has(city2)) graph.set(city2, []);
    graph.get(city1).push({ node: city2, weight: distance });
    graph.get(city2).push({ node: city1, weight: distance });
});

// Dijkstra's Algorithm
function dijkstra(graph, start, end) {
    const distances = {};
    const prevNodes = {};
    const pq = new Set([...graph.keys()]);

    graph.forEach((_, node) => {
        distances[node] = Infinity;
        prevNodes[node] = null;
    });
    distances[start] = 0;

    while (pq.size) {
        const currentNode = [...pq].reduce((minNode, node) =>
            distances[node] < distances[minNode] ? node : minNode
        );

        pq.delete(currentNode);

        if (currentNode === end) break;

        graph.get(currentNode).forEach(({ node: neighbor, weight }) => {
            const newDist = distances[currentNode] + weight;
            if (newDist < distances[neighbor]) {
                distances[neighbor] = newDist;
                prevNodes[neighbor] = currentNode;
            }
        });
    }

    const path = [];
    for (let at = end; at; at = prevNodes[at]) {
        path.push(at);
    }
    return path.reverse();
}

// Bellman-Ford Algorithm
function bellmanFord(graph, start, end) {
    const distances = {};
    const prevNodes = {};

    graph.forEach((_, node) => {
        distances[node] = Infinity;
        prevNodes[node] = null;
    });
    distances[start] = 0;

    for (let i = 0; i < graph.size - 1; i++) {
        connections.forEach(([city1, city2, weight]) => {
            if (distances[city1] + weight < distances[city2]) {
                distances[city2] = distances[city1] + weight;
                prevNodes[city2] = city1;
            }
            if (distances[city2] + weight < distances[city1]) {
                distances[city1] = distances[city2] + weight;
                prevNodes[city1] = city2;
            }
        });
    }

    const path = [];
    for (let at = end; at; at = prevNodes[at]) {
        path.push(at);
    }
    return path.reverse();
}

// Visualization using D3.js
function plotGraph(graph, shortestPath = []) {
    const nodes = Array.from(graph.keys()).map((node) => ({ id: node }));
    const links = connections.map(([source, target, weight]) => ({
        source,
        target,
        weight
    }));

    const width = 800;
    const height = 600;

    const svg = d3
        .select("body")
        .append("svg")
        .attr("width", width)
        .attr("height", height);

    const simulation = d3
        .forceSimulation(nodes)
        .force("link", d3.forceLink(links).id((d) => d.id).distance(100))
        .force("charge", d3.forceManyBody().strength(-500))
        .force("center", d3.forceCenter(width / 2, height / 2));

    const link = svg
        .selectAll("line")
        .data(links)
        .enter()
        .append("line")
        .attr("stroke", (d) =>
            shortestPath.includes(d.source.id) && shortestPath.includes(d.target.id)
                ? "red"
                : "gray"
        )
        .attr("stroke-width", 2);

    const node = svg
        .selectAll("circle")
        .data(nodes)
        .enter()
        .append("circle")
        .attr("r", 10)
        .attr("fill", "lightblue")
        .call(
            d3.drag()
                .on("start", (event) => {
                    if (!event.active) simulation.alphaTarget(0.3).restart();
                    event.subject.fx = event.subject.x;
                    event.subject.fy = event.subject.y;
                })
                .on("drag", (event) => {
                    event.subject.fx = event.x;
                    event.subject.fy = event.y;
                })
                .on("end", (event) => {
                    if (!event.active) simulation.alphaTarget(0);
                    event.subject.fx = null;
                    event.subject.fy = null;
                })
        );

    const labels = svg
        .selectAll("text")
        .data(nodes)
        .enter()
        .append("text")
        .text((d) => d.id)
        .attr("x", 15)
        .attr("y", 5);

    simulation.on("tick", () => {
        link
            .attr("x1", (d) => d.source.x)
            .attr("y1", (d) => d.source.y)
            .attr("x2", (d) => d.target.x)
            .attr("y2", (d) => d.target.y);

        node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);

        labels.attr("x", (d) => d.x).attr("y", (d) => d.y);
    });
}

// Menu-driven interface
function main() {
    const startCity = prompt("Enter start city:");
    const endCity = prompt("Enter end city:");
    const algoChoice = prompt("Choose algorithm:\n1. Dijkstra\n2. Bellman-Ford");

    let shortestPath = [];
    if (algoChoice === "1") {
        shortestPath = dijkstra(graph, startCity, endCity);
    } else if (algoChoice === "2") {
        shortestPath = bellmanFord(graph, startCity, endCity);
    } else {
        alert("Invalid choice!");
        return;
    }

    console.log(`Shortest Path: ${shortestPath.join(" -> ")}`);
    plotGraph(graph, shortestPath);
}

// Run the program
main();
