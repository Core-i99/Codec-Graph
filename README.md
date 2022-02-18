# Codec-Graph
Script to generate Graphviz graphs from HDA-Intel codec information

[![GitHub License](https://img.shields.io/github/license/Core-i99/Codec-Graph?color=informational)]("https://github.com/Core-i99/Codec-Graph/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/release/Core-i99/Codec-Graph)](https://GitHub.com/Core-i99/Codec-Graph/releases/)
[![GitHub stars](https://img.shields.io/github/stars/Core-i99/Codec-Graph)](https://GitHub.com/Core-i99/Codec-Graph/stargazers/)
[![GitHub Issues](https://img.shields.io/github/issues/Core-i99/Codec-Graph?color=informational)](https://github.comCore-i99/Codec-Graph/issues)
[![GitHub Pulls](https://img.shields.io/github/issues-pr/Core-i99/Codec-Graph?style=flat-square&color=informational)](https://GitHub.com/Core-i99/Codec-Graph/pull/)

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
