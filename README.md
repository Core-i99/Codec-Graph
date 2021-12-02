# Codec-Graph
Script to generate Graphviz graphs from HDA-Intel codec information

Credit to helllabs for making [the original Codec Graph](http://helllabs.org/codecgraph/)

# Usage
- Make sure python3 is installed!

- Download Codec Graph from the Relase page
- Open terminal
- cd `Codec_Graph_directory`
- python3 ./Codec_Graph.py

The output files will be generated in the output folder.


Node shape and colors:

- Amplifier:	triangle
- Audio input:	red ellipse
- Audio output:	blue ellipse
- Audio selector:	parallelogram
- Audio mixer:	hexagon
- Pin complex:	rectangle


# FAQ
### Error: "Couldn't find Graphviz."
- This means Graphviz isn't installed. Follow the [instructions](https://github.com/TheHackGuy/Codec-Graph/blob/V1/Graphviz%20Instructions.pdf) to install Graphviz.
