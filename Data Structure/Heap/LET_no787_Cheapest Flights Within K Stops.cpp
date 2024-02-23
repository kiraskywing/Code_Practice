class Solution {
public:
	int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
		unordered_map<int, vector<pair<int, int>>> graph;
		for (auto f : flights) {
			graph[f[0]].push_back({f[1], f[2]});
		}
        
		vector<int> costs(n, INT_MAX);
		costs[src] = 0;
		vector<int> stops(n, INT_MAX);
		stops[src] = 0;
		
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
		k++;
		pq.push({0, k, src});    //cost, stops, node
		
        while (!pq.empty()) {
			vector<int> v = pq.top();
			int cost = v[0];
			int stop = v[1];
			int node = v[2];
			pq.pop();
			
            if (dst == node) 
                return cost;
			if (stop > 0) {
				for (auto neighbor : graph[node]) {
					int neighbor_id = neighbor.first;
                    int next_cost = cost + neighbor.second;
					if (costs[neighbor_id] > next_cost || stops[neighbor_id] > k - stop + 1) {
						costs[neighbor_id] = next_cost;
						stops[neighbor_id] = k - stop + 1;
						pq.push({next_cost, stop - 1, neighbor_id});
					}

				}
			}
		}
		return -1;
	}
};