# 3D-Tic-Tac-Toe

This project was developed as a final assignment for an Artificial Intelligence course at the University of Minnesota. 

## Original Source & Credits
The AI decision-making analysis in this repository builds upon the 3D Tic-Tac-Toe Java framework originally designed and implemented by **Adam Devigili/adamdevigili**.

I extend my sincere gratitude to the original author for sharing their work. Access to this functional codebase allowed me to build a robust testing pipeline and deeply analyze 3D search algorithms.

* **Original Source:** https://github.com/adamdevigili/3D-Tic-Tac-Toe/tree/master

### My Contributions
While the core game mechanics and baseline AI belong to the original creator, I extended and configured this repository as a comprehensive testing framework for academic evaluation. My work included:

* **Test Suite Development:** Developed a comprehensive test suite simulation for the 3D Tic-Tac-Toe Java game to isolate and analyze AI decision-making patterns.
* **Performance Benchmarking:** Benchmarked performance metrics of the AI algorithms, documenting structural architecture and algorithmic search constraints.
* **Heatmap & Strategy Analysis:** Utilized data-driven Heatmaps to evaluate the strong points of several adversarial and heuristic algorithms (including Random, Minimax, Alpha-Beta Pruning, and Greedy Heuristic).
* **Opening Move Evaluation:** Simulated and calculated the precise win-rates of all 27 possible opening moves in the 3D grid space to identify mathematically optimal first-move strategies.
* Writing an analysis report on heuristic search efficiency and optimal first-move strategies. (available in `/docs`).

Compilation/Execution
------------
```$ cd .../3DTTT/src```

```$ javac TTT3D.java```

```$ java TTT3D```


Simulations
------------
```$ cd .../3DTTT/src```

```$ javac TTT3D.java SimulationRunner.java```

```$ java SimulationRunner```
