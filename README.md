# Codec-Graph
Script to generate Graphviz graphs from HDA-Intel codec information

<a href="https://github.com/Core-i99/Codec-Graph/stargazers"><img src="https://img.shields.io/github/stars/Core-i99/Codec-Graph" alt="Stars Badge"/></a>
<a href="https://github.com/Core-i99/Codec-Graph/network/members"><img src="https://img.shields.io/github/forks/Core-i99/Codec-Graph" alt="Forks Badge"/></a>
<a href="https://github.com/Core-i99/Codec-Graph/pulls"><img src="https://img.shields.io/github/issues-pr/Core-i99/Codec-Graph" alt="Pull Requests Badge"/></a>
<a href="https://github.comCore-i99/Codec-Graph/issues"><img src="https://img.shields.io/github/issues/Core-i99/Codec-Graph" alt="Issues Badge"/></a>
<a href="https://github.com/Core-i99/Codec-Graph/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Core-i99/Codec-Graph?color=2b9348"></a>
<a href="https://github.com/Core-i99/Codec-Graph/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Core-i99/Codec-Graph?color=2b9348" alt="License Badge"/></a>

# Usage
- Make sure python3 is installed!

- Download Codec Graph from the Relase page
- Open terminal
- cd `Codec_Graph_directory`
- python3 ./Codec_Graph.py

The output files will be generated in the output folder.


# Node shape and colors
- Amplifier:	triangle
- Audio input:	red ellipse
- Audio output:	blue ellipse
- Audio selector:	parallelogram
- Audio mixer:	hexagon
- Pin complex:	rectangle


# FAQ
### Error: "Couldn't find Graphviz."
- This means Graphviz isn't installed. Follow the [instructions](https://github.com/Core-i99/Codec-Graph/blob/main/Graphviz%20Instructions.md) to install Graphviz.

# Credits
- [Helllabs](http://helllabs.org) for [the original Codec Graph](http://helllabs.org/codecgraph/)
