#!/usr/bin/python3
#
# Script to generate graphviz graphs from HDA-Intel codec information
#
# by Eduardo Habkost <ehabkost@mandriva.com>
# updated by Stijn Rombouts <stijnrombouts@outlook.com>
#
# Copyright (c) 2006,2007 Eduardo Habkost <ehabkost@mandriva.com>
# Copyright (c) 2006,2007 Mandriva Conectiva
# Copyright (c) 2021,2022 Stijn Rombouts <stijnrombouts@outlook.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

import re
import sys
import os
import platform
import webbrowser
import shutil
import subprocess
import logging
from logging import handlers
import tkinter
import tkinter.messagebox
from tkinter import filedialog

Version = "V1.4"
ALL_NODES = False
outputname = "codecdump"
outputfilename = outputname + ".svg"

# logging
if platform.system() == "Darwin":
    lib_logs = os.path.join(
        os.path.expanduser("~"),
        "Library",
        "Logs"
    )

elif platform.system() == "Windows":
    appdata_local = os.getenv("LOCALAPPDATA")
    lib_logs = os.path.join(appdata_local, 'Codec-Graph')
    if not os.path.exists(lib_logs):
        try:
            os.mkdir(lib_logs)
        except Exception:
            tkinter.messagebox.showerror("ERROR", "Failed to create log dir")
            sys.exit()

else:
    tkinter.messagebox.showerror("ERROR", "This OS is currently not supported")
    sys.exit()
logformat = "%(asctime)s - %(levelname)s - %(message)s"
date = "%m/%d/%Y %I:%M:%S %p"

# Adding the base log handlers.
handler = logging.getLogger()
rotating = handlers.RotatingFileHandler(os.path.join(
    lib_logs, "Codec-Graph.log"), mode="a", maxBytes=2 ** 13)
# Add the RotatingFileHandler to the default logger.
handler.addHandler(rotating)
rotating.setFormatter(
    logging.Formatter(
        logformat, datefmt=date
    )
)
handler.setLevel(logging.DEBUG)

root = tkinter.Tk()  # Creating instance of tkinter class
root.title("Codec Graph")
root.resizable(False, False)  # Disable rootwindow resizing

fm1 = tkinter.Frame(root)
fm2 = tkinter.Frame(root)
fm3 = tkinter.Frame(root)
fm4 = tkinter.Frame(root)


def centerwindow():
    app_height = 200
    app_width = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (app_width/2))
    y_cordinate = int((screen_height/2) - (app_height/2))
    root.geometry(f"{app_width}x{app_height}+{x_cordinate}+{y_cordinate}")


centerwindow()  # center the gui window on the screen


def showinfo():
    tkinter.messagebox.showinfo(
        "About", f"App to generate graphviz graphs from HDA-Intel codec information.\n\nCodec Graph version {Version}\n ")


def CheckGraphviz():
    checkGraphviz = subprocess.run(
        ['dot', '-V'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, check=False, shell=True)
    if checkGraphviz.returncode == 1:
        errormessage = tkinter.messagebox.showerror(
            "ERROR", "Couldn't find Graphviz Please follow the instructions to install Graphviz.\n\nClick OK to open instructions how to install GraphViz.")
        if errormessage == "ok":
            webbrowser.open(
                "https://github.com/Core-i99/Codec-Graph/blob/main/Graphviz%20Instructions.md")
            logging.info("Opened instructions")

    elif checkGraphviz.returncode == 0:
        tkinter.messagebox.showinfo(
            "Found graphviz", "Found graphviz installation")


def openFileClicked():
    filetypes = [
        ('txt files', '*.txt')
    ]
    inputfile = filedialog.askopenfilename(filetypes=filetypes)
    # if inputfile isn't an empty string (some file is selected)
    if inputfile != '':
        logging.info("Selected Codec Dump %s", inputfile)

        with open(inputfile, "r", encoding="utf-8") as f:
            ci = CodecInfo(f)
            ci.dump_graph()

        # running graphviz
        # usage of graphviz (dot): dot -T$extention -o$outfile.$extention $inputfile
        rungraphviz = os.system(
            "dot -Tsvg -o./output/" + outputfilename + " ./tmp/dotfile.txt")

        if rungraphviz == 0:
            logging.info("Running Graphviz succeed")

        if rungraphviz == 1:
            tkinter.messagebox.showerror(
                "Error", "Running graphviz failed!\nPlease check if graphviz is installed using the button for it.")

        removetmp()
        CreateDecDump()


def end():
    end_string = "Thanks for using Codec Graph\nWritten By Core i99 - © Stijn Rombouts 2022\n"
    tkinter.messagebox.showinfo("End", end_string)
    sys.exit()


# Buttons and labels
tkinter.Button(fm1, text='Select Codec Dump', command=openFileClicked).pack()
tkinter.Button(fm2, text="Check if Graphviz is installed",
               command=CheckGraphviz).pack()
tkinter.Button(fm3, text="About", command=showinfo).pack()
tkinter.Button(fm4, text='Exit', command=end).pack()

# pack the frames
fm1.pack(pady=10)
fm2.pack(pady=10)
fm3.pack(pady=10)
fm4.pack(pady=10)

# working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
working_dir = os.getcwd()
dotfile = working_dir + "/tmp/dotfile.txt"
logging.info("Current working directory: %s", working_dir)
logging.info("Dotfile path %s", dotfile)


def createtmp():  # create tmp folder
    createtmp = './tmp'
    if os.path.exists(createtmp):
        shutil.rmtree(createtmp)
        logging.info("Found an existing tmp directory")
    os.makedirs(createtmp)
    logging.info("Created tmp directory")


def removetmp():  # removing the temp folder
    shutil.rmtree('./tmp/')
    if os.path.exists("./tmp"):
        logging.error("Removing tmp directory failed")
    else:
        logging.info("Removing tmp directory succeed")


def createoutputdir():  # Create output folder
    createoutput = 'output'
    if os.path.exists(createoutput):
        shutil.rmtree(createoutput)  # Remove existing ouput folder
        logging.info("Found an existing output directory")
    os.makedirs(createoutput)
    logging.info("Created output directory")


def CreateDecDump():  # create decimal dump
    logging.info("Creating decimal dump")
    with open("./output/" + outputfilename, "r", encoding="utf-8") as f:
        data = f.readlines()
        for index, line in enumerate(data):
            hex_values = re.findall(r'0x[\dA-F]+', line)
            for hex_value in hex_values:
                dec_value = str(int(hex_value, 16))
                line = line.replace(hex_value, dec_value)
            data[index] = line
    with open("./output/" + outputname + "dec.svg", "w", encoding="utf-8") as f:
        f.writelines(data)
        logging.info("Created decimal svg")
    tkinter.messagebox.showinfo(
        "Finished", "Done! Look in the output folder.")


def indentlevel(line):
    """Return the indent level of a line"""
    m = re_indent.match(line)
    if not m:
        return 0
    return len(m.group(0))


def parse_item(level, lines):
    """Read a line and corresponding indented lines"""
    item = lines.pop(0).rstrip('\r\n').lstrip(' ')
    subitems = list(parse_items(level, lines))
    return item, subitems


def parse_items(level, lines):
    """Parse a list of indented lines"""
    while lines:
        line = lines[0]
        linelvl = indentlevel(line)
        if linelvl <= level:
            # end of list
            break
        yield parse_item(linelvl, lines)


def coloravg(a, b, v):
    r = tuple((int(a[i]*(1-v) + b[i]*v)) for i in (0, 1, 2))
    return r


def formatcolor(c):
    return f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}"


class Amplifier:
    def __init__(self, ofs, nsteps, stepsize, mute):
        self.ofs = int(ofs, 16)
        self.nsteps = int(nsteps, 16)
        self.stepsize = stepsize
        self.mute = mute

    def set_values(self, values):
        self.values = values
        self.gainvalues = [v & 0x7f for v in values]
        self.mutevalues = [(v & 0x80) != 0 for v in values]

    def color(self):
        if True in self.mutevalues:
            level = 0
        else:
            average = sum(self.gainvalues)/len(self.gainvalues)

            if self.nsteps == 0:
                level = 1
            else:
                # XXX: confirm if this formula is correct
                level = 1-float(average-self.ofs)/(self.nsteps)

        level = max(level, 0)
        level = min(level, 1)
        zerocolor = (200, 200, 200)
        fullcolor = (0, 0, 255)
        color = coloravg(zerocolor, fullcolor, level)

        return formatcolor(color)


class Node:
    node_info_re = re.compile(
        r'^Node (0x[0-9a-f]*) \[(.*?)\] wcaps 0x[0-9a-f]*?: (.*)$')
    final_hex_re = re.compile(' *(0x[0-9a-f]*)$')

    def __init__(self, codec, item, subitems):
        self.item = item
        self.subitems = subitems
        self.codec = codec

        fields = {}

        # split first line and get some fields
        m = self.node_info_re.match(item)
        self.nid = int(m.group(1), 16)
        self.type = m.group(2)
        wcapstr = m.group(3)

        self.wcaps = wcapstr.split()

        # parse all items on the node information
        for inner_item, innter_subitems in self.subitems:
            # Parse node fields
            if ':' in inner_item:
                f, v = inner_item.split(':', 1)
                v = v.lstrip()

                # strip hex number at the end.
                # some fields, such as Pincap & Pin Default,
                # have an hex number in the end
                m = self.final_hex_re.search(f)
                if m:
                    f = self.final_hex_re.sub('', f)

                    # store the hex value and the
                    # string, on different keys
                    fields[f+'-hex'] = m.group(1), innter_subitems
                    fields[f] = v, innter_subitems
                else:
                    fields[f] = v, innter_subitems
            else:
                sys.stderr.write(f"Unknown node item: {item}\n")

        self.fields = fields

        # parse connection info
        conn = fields.get('Connection', ('0', []))

        number, items = conn
        self.num_inputs = int(number)
        conns = []
        self.active_conn = None
        for i in items:
            for j in i[0].split():
                active = j.endswith('*')
                j = j.rstrip('*')
                nid = int(j, 16)
                conns.append(nid)
                if active:
                    self.active_conn = nid
        assert len(conns) == self.num_inputs
        self.inputs = conns

        if not self.active_conn and self.num_inputs == 1:
            self.active_conn = self.inputs[0]

        # parse amplifier info
        def parse_amps(name, count):
            capstr = fields[f'{name} caps'][0]

            if capstr == 'N/A':
                capstr = 'ofs=0x00, nsteps=0x00, stepsize=0x00, mute=0'

            capl = capstr.split(', ')

            caps = {}
            for cap in capl:
                cname, cval = cap.split('=', 1)
                caps[cname] = cval

            valstr = fields[f'{name} vals'][0]
            vals = re.findall(r'\[([^]]*)\]', valstr)

            # warn if Amp-In vals field is broken
            if count != len(vals):
                sys.stderr.write(
                    f"Node 0x{self.nid:02x}: Amp-In vals count is wrong: values found: {len(vals)}. expected: {count}\n")

            amps = []
            for i in range(count):
                amp = Amplifier(caps['ofs'], caps['nsteps'],
                                caps['stepsize'], caps['mute'])
                if len(vals) > i:
                    intvals = [int(v, 16) for v in vals[i].split(' ')]
                # just in case the "vals" field is
                # broken in our input file
                else:
                    intvals = [0, 0]
                amp.set_values(intvals)
                amps.append(amp)

            return amps

        inamps = self.num_inamps()
        if inamps > 0:
            self.inamps = parse_amps('Amp-In', inamps)
        if self.has_outamp():
            self.outamp, = parse_amps('Amp-Out', 1)

        self.outputs = []

    def new_output(self, nid):
        self.outputs.append(nid)

    def input_nodes(self):
        for c in self.inputs:
            yield self.codec.get_node(c)

    def is_divided(self):
        if self.type == 'Pin Complex':
            return True

        return False

    def idstring(self):
        return f'nid-{self.nid:02x}'

    def has_outamp(self):
        return 'Amp-Out' in self.wcaps

    def outamp_id(self):
        return f'"{self.idstring()}-ampout"'

    def out_id(self):
        if self.is_divided():
            return self.main_output_id()

        if self.has_outamp():
            return self.outamp_id()

        return self.outamp_next_id()

    def has_inamp(self):
        return 'Amp-In' in self.wcaps

    def many_ampins(self):
        types = ['Audio Mixer']
        return self.type in types

    def num_inamps(self):
        if not self.has_inamp():
            return 0
        if self.many_ampins():
            return self.num_inputs
        return 1

    def inamp_id(self, orignid):
        if self.many_ampins():
            return f'"{self.idstring()}-ampin-{orignid}"'
        return f'"{self.idstring()}-ampin"'

    def in_id(self, orignid):
        if self.is_divided():
            return self.main_input_id()

        if self.has_inamp():
            return self.inamp_id(orignid)

        return self.inamp_next_id()

    def main_id(self):
        assert not self.is_divided()
        return f'"{self.idstring()}"'

    def main_input_id(self):
        assert self.is_divided()
        return f'"{self.idstring()}-in"'

    def main_output_id(self):
        assert self.is_divided()
        return f'"{self.idstring()}-out"'

    def inamp_next_id(self):
        """ID of the node where the In-Amp would be connected"""
        if self.is_divided():
            return self.main_output_id()

        return self.main_id()

    def outamp_next_id(self):
        """ID of the node where the Out-Amp would be connected"""
        if self.is_divided():
            return self.main_input_id()

        return self.main_id()

    def wcaps_label(self):
        not_shown = ['Amp-In', 'Amp-Out']
        show = [cap for cap in self.wcaps if cap not in not_shown]
        return ' '.join(show)

    def label(self):
        r = f'{self.nid} (0x{self.nid:02x})'

        pdef = self.fields.get('Pin Default')
        if pdef:
            pdef, subdirs = pdef
            r += f'\\n{pdef}'

        r += f'\\n{self.wcaps_label()}'

        pincap = self.fields.get('Pincap')
        if pincap:
            pincap, subdirs = pincap
            r += f'\\n{pincap}'

        r = f'"{r}"'
        return r

    def show_input(self):
        return ALL_NODES or len(self.inputs) > 0

    def show_output(self):
        return ALL_NODES or len(self.outputs) > 0

    def additional_attrs(self):
        default_attrs = [('shape', 'box'), ('color', 'black')]
        shape_dict = {
            'Audio Input': [('color', 'red'),
                            ('shape', 'ellipse')],
            'Audio Output': [('color', 'blue'),
                             ('shape', 'ellipse')],
            'Pin Complex': [('color', 'green'),
                            ('shape', 'box')],
            'Audio Selector': [('shape', 'parallelogram'),
                               ('orientation', '0')],
            'Audio Mixer': [('shape', 'hexagon')],
            'Unknown Node': [('color', 'red'),
                             ('shape', 'Mdiamond')],
        }
        return shape_dict.get(self.type, default_attrs)

    def new_node(self, f, id, attrs):
        f.write(f' {id} ')
        if attrs:
            attrstr = ', '.join(f'{f}={v}' for f, v in attrs)
            f.write(f'[{attrstr}]')
        f.write('\n')

    def dump_main_input(self, f):
        if self.show_input():
            self.new_node(f, self.main_input_id(), self.get_attrs())

    def dump_main_output(self, f):
        if self.show_output():
            self.new_node(f, self.main_output_id(), self.get_attrs())

    def get_attrs(self):
        attrs = [('label', self.label())]
        attrs.extend(self.additional_attrs())
        return attrs

    def dump_main(self, f):
        if not self.is_divided():
            if self.show_input() or self.show_output():
                self.new_node(f, self.main_id(), self.get_attrs())
        else:
            self.dump_main_input()
            self.dump_main_output()

    def show_amp(self, f, id, type, frm, to, label='', color=None):
        if color is None:
            fill = ''
        else:
            fill = f' color="{color}"'
        f.write(
            f'  {id} [label = "{label}", shape=triangle orientation=-90{fill}];\n')
        f.write(
            f'  {frm} -> {to} [arrowsize=0.5, arrowtail=dot, weight=2.0{fill}];\n')

    def dump_out_amps(self, f):
        if self.show_output() and self.has_outamp():
            self.show_amp(f, self.outamp_id(), "Out", self.outamp_next_id(
            ), self.outamp_id(), '', self.outamp.color())

    def dump_in_amps(self, f):
        if self.show_input() and self.has_inamp():

            if self.many_ampins():
                amporigins = [(f"{n} (0x{self.inputs[n]:02x})",
                               self.inputs[n]) for n in range(len(self.inputs))]
            else:
                amporigins = [('', None)]

            for i, amporigin in enumerate(amporigins):
                label, origin = amporigin
                ampid = self.inamp_id(origin)
                self.show_amp(f, ampid, "In", ampid,
                              self.inamp_next_id(), label, self.inamps[i].color())

    def dump_amps(self, f):
        self.dump_out_amps(f)
        self.dump_in_amps(f)

    def is_conn_active(self, c):
        if self.type == 'Audio Mixer':
            return True
        if c == self.active_conn:
            return True
        return False

    def dump_graph(self, f):
        name = f"cluster-{self.idstring()}"
        if self.is_divided():
            f.write(f'subgraph "{name}-in" ' + '{\n')
            f.write('  pencolor="gray80"\n')
            self.dump_main_input(f)
            self.dump_out_amps(f)
            f.write('}\n')

            f.write(f'subgraph "{name}-out" ' + '{\n')
            f.write('  pencolor="gray80"\n')
            self.dump_main_output(f)
            self.dump_in_amps(f)
            f.write('}\n')
        else:
            f.write(f'subgraph "{name}" ' + '{\n')
            f.write('  pencolor="gray80"\n')
            self.dump_main(f)
            self.dump_amps(f)
            f.write('}\n')

        for origin in self.input_nodes():
            if self.is_conn_active(origin.nid):
                attrs = "[color=gray20]"
            else:
                attrs = "[color=gray style=dashed]"
            f.write(f'{origin.out_id()} -> {self.in_id(origin.nid)} {attrs};\n')


re_indent = re.compile("^ *")


class CodecInfo:
    def __init__(self, f):
        self.fields = {}
        self.nodes = {}
        lines = f.readlines()
        total_lines = len(lines)

        for item, subitems in parse_items(-1, lines):
            line = total_lines-len(lines)
            try:
                if ': ' not in item and item.endswith(':'):
                    # special case where there is no ": "
                    # but we want to treat it like a "key: value"
                    # line
                    # (e.g. "Default PCM:" line)
                    item += ' '

                if item.startswith('Node '):
                    n = Node(self, item, subitems)
                    self.nodes[n.nid] = n
                if item.startswith('No Modem Function Group found'):
                    # ignore those lines
                    pass
                elif ': ' in item:
                    f, v = item.split(': ', 1)
                    self.fields[f] = v
                elif item.strip() == '':
                    continue
                else:
                    sys.stderr.write(
                        f"Warning: line {line} ignored: {item}\n")

            except Exception:
                sys.stderr.write(f'Exception around line {line}\n')
                sys.stderr.write(f'item: {item}\n')
                sys.stderr.write(f'subitems: {subitems}\n)')
                raise

        self.create_out_lists()

    def get_node(self, nid):
        n = self.nodes.get(nid)
        if not n:
            # create a fake node
            n = Node(
                self, f'Node 0x{nid:02x} [Unknown Node] wcaps 0x0000: ', [])
            self.nodes[nid] = n
            n.label = lambda: (f'"Unknown Node 0x{nid:02x}"')
        return n

    def create_out_lists(self):
        for n in list(self.nodes.values()):
            for i in n.input_nodes():
                i.new_output(n.nid)

    def dump(self):
        print(f"Codec: {self.fields['Codec']}")
        print(f"Nodes: {len(self.nodes)}")
        for n in list(self.nodes.values()):
            print(f"Node: 0x{n.nid:02x}", end=' ')
            print(f" {n.num_inputs} conns")

    def dump_graph(self):
        createtmp()
        with open(dotfile, "w", encoding='utf-8') as file:
            file.write('digraph {\n')
            file.write("""rankdir=LR
            ranksep=3.0
            """)
            for n in list(self.nodes.values()):
                n.dump_graph(file)
            file.write('}\n')
            logging.info("Wrote dotfile")
        createoutputdir()


root.protocol("WM_DELETE_WINDOW", end)
root.mainloop()
