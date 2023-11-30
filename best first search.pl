% Define edges and their weights

edge(a, b, 4).

edge(a, c, 5).

edge(b, d, 2).

edge(c, d, 1).

edge(c, e, 3).

edge(d, e, 4).

edge(e, goal, 2).



% Best First Search algorithm

best_first_search(Start, Goal, Path) :-

    best_first_search([[(Start, 0)]], Goal, Path).



best_first_search([[Node|Path]|_], Goal, [Node|Path]) :-

    Node = (Goal, _).



best_first_search([CurrentPath|RestPaths], Goal, Path) :-

    extend_path(CurrentPath, NewPaths),

    append(RestPaths, NewPaths, CombinedPaths),

    sort_paths_by_heuristic(CombinedPaths, SortedPaths),

    best_first_search(SortedPaths, Goal, Path).



extend_path([Node|Path], NewPaths) :-

    findall([(NextNode, NewCost), Node|Path],

            (edge(Node, NextNode, EdgeCost), not(member(NextNode, [Node|Path])),

             NewCost is EdgeCost + PathCost,

             heuristic(NextNode, Heuristic),

             NewCostHeuristic is NewCost + Heuristic),

            NewPaths).



sort_paths_by_heuristic(Paths, SortedPaths) :-

    predsort(compare_path_heuristic, Paths, SortedPaths).



compare_path_heuristic(Result, Path1, Path2) :-

    path_cost_heuristic(Path1, Cost1, Heuristic1),

    path_cost_heuristic(Path2, Cost2, Heuristic2),

    TotalCost1 is Cost1 + Heuristic1,

    TotalCost2 is Cost2 + Heuristic2,

    compare(Result, TotalCost1, TotalCost2).



path_cost_heuristic([(_, Cost)|_], Cost, Heuristic) :-

    heuristic(_, Heuristic).



heuristic(Node, Heuristic) :-

    edge(Node, goal, Heuristic).

    

% Example query: best_first_search(a, goal, Path).
