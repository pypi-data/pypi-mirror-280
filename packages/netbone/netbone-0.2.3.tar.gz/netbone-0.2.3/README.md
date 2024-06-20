
# NetBone

NetBone is a Python library for extracting network backbones from simple weighted networks.

## Features

- Extract network backbones from simple weighted networks
- Contains six statistical methods for extracting backbones
- Contains thirteen structural methods for extracting backbones
- Contains one hybrid method for extracting backbones
- Includes three filters for extracting the backbone: boolean filter, threshold filter, and fraction filter
- Built-in methods for comparing backbones with each other
- Option to use custom comparison methods
- Visualization tools to display the results of the comparison



## Installation
You should have Python version 3.10 or higher. Then you can install the latest version of NetBone:
```
pip install netbone
```
or
```
pip install git+https://gitlab.liris.cnrs.fr/coregraphie/netbone
```


## Usage/Examples
To see a more detailed example, please refer to the example notebook [here](https://gitlab.liris.cnrs.fr/coregraphie/netbone/-/blob/main/examples/example.ipynb). However, here is a simple example using a backbone extraction method and three filters that are available:
```
import netbone as nb
import networkx as nx
from netbone.filters import boolean_filter, threshold_filter, fraction_filter

# load the network
g = nx.les_miserables_graph()

# apply the choosen backbone extraction method
b = nb.high_salience_skeleton(g)

# extract the backbone based on the default threshold
backbone1 = boolean_filter(b)

# extract the backbone based on a threshold(0.7)
backbone2 = threshold_filter(b, 0.7)

# extract the backbone keeping a fraction of edges(0.15)
backbone3 = fraction_filter(b, 0.15)
```
![Les Misérables original network and the extracted backbones](https://gitlab.liris.cnrs.fr/coregraphie/netbone/-/raw/main/examples/images/toy.png)

## Citation
Ali Yassin, Abbas Haidar, Hocine Cherifi et al. An Evaluation Tool for Backbone Extraction Techniques in Weighted Complex Networks, 19 May 2023, PREPRINT (Version 1) available at Research Square [https://doi.org/10.21203/rs.3.rs-2935871/v1]
## Credits
This project includes code from the following sources:

[ECM filter](https://github.com/deklanw/maxent_graph ),
[Doubly Stochastic](https://www.michelecoscia.com/?page_id=287),
[Marginal Likelihood](https://github.com/naviddianati/GraphPruning),
[Metric Distance, Ultrametric Distance](https://github.com/rionbr/distanceclosure)
## Contributing

Contributions are always welcome!


## License

[MIT](https://choosealicense.com/licenses/mit/)

