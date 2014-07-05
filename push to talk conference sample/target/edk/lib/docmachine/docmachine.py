########################################################################
#                                                                      #
#               This software is part of the ECharts package           #
#                  Copyright (c) 2006 AT&T Corp.                       #
#                      and is licensed under the                       #
#                  Common Public License, Version 1.0                  #
#                            by AT&T Corp.                             #
#                                                                      #
########################################################################

# Translate an abstract ECharts machine to SVG.

from AbstractMachine import *
import dotmachine
import DotMachineFormatter

from xml.sax import saxutils, make_parser
import sys, re, string, os, xml.sax, thread

True = 1
False = 0

# global variable set in translate() and referenced in
# docmachinewindowhtml()
packageSubdirectory = ""

# global variable conditionally set by translation thread executing
# doctranslatesvg if an exception occurs during 'dot' execution or
# svg-to-svg translation - flag is unconditionally cleared by main
# thread immediately prior to spawning the translation thread
TRANSLATION_EXCEPTION = False

# write <machine>.html file
def docmachinehtml(compilationUnit, machine, targetDirectory, documentHeader):
	name = getMachineName(compilationUnit)
	package = getPackage(compilationUnit)
	# relative path from machine's html directory to root html
	# directory
	rootPath = string.joinfields(len(package) * [ ".." ], "/")
	htmlPath = targetDirectory + os.sep + name + ".html"
	htmlFile = file(htmlPath, 'w')
	htmlBody = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/strict.dtd">
<HTML>
<HEAD>
<LINK rel="stylesheet" type="text/css" href="%s/docmachine.css" />
<TITLE>%s</TITLE>
</HEAD>

<BODY>
<table width="100%%" height="100%%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td>
<div id="buttons_outer">
    <div id="buttons_inner">
	    <div id="buttons">
		    <ul id="mainlevel-nav">
			  <li><a href="%s/overview-summary.html" class="mainlevel-nav">Overview</a></li>
			  <li><a href="package-summary.html" class="mainlevel-nav">Package</a></li>
			</ul>						
		</div>
	</div>
</div></td></tr>
<tr><td class="outline">
<div class="header">
<span class="left">Machine</span>
<span class="right">%s</span>
</div>
</td></tr>
<tr><td>
<div id="package_name">%s</div>
<div class="contentheading">%s</div>
<div class="summary"></div>
</td></tr>
<tr><td height="100%%">
<input class="button" value="New Window" type="submit" onclick="window.open('%s')">
<div class="machine-svg">
<iframe src="%s" id="svg" name="svg" height="100%%" width="100%%"
		frameborder="0" marginwidth="0" marginheight="0"></iframe>
</div>
</td></tr>
</table>
</BODY>
</HTML>
''' % (rootPath, name, rootPath, documentHeader, string.joinfields(package, "."), name,
	   name + ".svg",
	   name + ".svg")
	htmlFile.write(htmlBody)
	htmlFile.close()

# dotmachine url formatter.
class URLFormatter(DotMachineFormatter.DotMachineFormatter):

	def doturl(self, compilationUnit, statePath):
		package = getPackage(compilationUnit)
		name = getMachineName(compilationUnit)
		return string.joinfields(package + [ name ], "/")

# Transforms dot's svg output to svg used for documentation. Add ecma
# script and update/add element attributes.
class TransformSVG(saxutils.XMLGenerator):

	def __init__(self, ecma, stream, fontsize, package):
		saxutils.XMLGenerator.__init__(self, stream)
		self.stream = stream
		self.inTitle = False
		self.inAnchor = False
		self.groupAttribs = {}
		self.title = ""
		self.groupCount = 0
		self.ecma = ecma
		self.fontsize = fontsize
		self.package = package

	def startElement(self, name, attribs):
		if name == "svg":
			self.stream.write("<svg ")
			for key in attribs.keys():
				if key == "viewBox":
					# remove "viewBox" attribute
					pass
				elif key == "width":
					# increase width to accommodate 80 character wide
					# tooltips
					self.stream.write('%s="%s" ' % (key, ("%spt" % (float(attribs[key][:-2]) + 50*self.fontsize))))
				elif key == "height":
					# increase height to accommodate 20 line tooltips
					self.stream.write('%s="%s" ' % (key, ("%spt" % (float(attribs[key][:-2]) + 20*self.fontsize))))
				else:
					self.stream.write('%s="%s" ' % (key, attribs[key]))
			self.stream.write(">")
			# add ecma script
			self.stream.write(self.defs % (len(self.package), self.ecma, self.fontsize))
		elif name == "title":
			# skip title element but save its value for use in group's
			# 'id' attribute
			self.inTitle = True
			self.title = ""
		elif name == "text":
			self.writeGroup()
			self.stream.write("<text ")
			for key in attribs.keys():
				if key == "style":
					# add "px" to font-size as workaround for
					# bug in mozilla v1.5 svg viewer
					style = attribs["style"]
					if "pt;" in style:
						# replace "pt" with "px" for windows
						newstyle = re.sub(r"font-size:(\d+\.\d+)pt;", r"font-size:\1px;", style)
					else:
						newstyle = re.sub(r"font-size:(\d+\.\d+);", r"font-size:\1px;", style)
					# add explicit "fill:black" to style to simplify
					# highlighting text
					newstyle = newstyle + "fill:black;"
					self.stream.write('style="%s" ' % newstyle)
				else:
					self.stream.write('%s="%s" ' % (key, attribs[key]))
			if not "style" in attribs.keys() and not "fill" in attribs.keys():
				# add explicit "fill:black" to style to simplify
				# highlighting text
				self.stream.write('fill="black" ')				
			self.stream.write(">")
		elif name == "polygon" and self.groupCount == 1:
			# ignore polygon element for top-level group
			pass
		elif name == "g":
			self.groupCount = self.groupCount + 1
			for key in attribs.keys():
				if key == "style":
					# add "px" to font-size as workaround for
					# bug in mozilla v1.5 svg viewer
					style = attribs["style"]
					newstyle = re.sub(r"font-size:(\d+\.\d+);", r"font-size:\1px;", style)
					self.groupAttribs[key] = newstyle
				else:
					self.groupAttribs[key] = attribs[key]
			if self.groupCount == 1:
				# add mouse handlers to top-level group
				self.groupAttribs['onmousemove'] = "delayShowTooltip(evt)"
				self.groupAttribs['onmouseout'] = "hideTooltip(evt)"
		elif name == "a":
			# change how anchor interaction handled (from <g ...> ...
			# <a ...  xlink:href="..." ...>... </a></g> to <a><g
			# onclick="..."> ... </g></a>)
			for key in attribs.keys():
				if key == "xlink:href":
					self.groupAttribs['onclick'] = "relocateWindow('%s')" % string.replace(attribs[key], os.sep, "/")
					self.inAnchor = True
					break
		else:
			self.writeGroup()
			saxutils.XMLGenerator.startElement(self, name, attribs)

	def characters(self, data):
		if self.inTitle:
			self.title += data
		else:
			saxutils.XMLGenerator.characters(self, data)

	def endElement(self, name):
		if name == "title":
			self.inTitle = False
			# overwrite enclosing group's "id" attribute with title
			# value
			self.groupAttribs['id'] = self.title
		elif name == "a":
			# skip it now and handle it when group ends
			pass
		elif name == "polygon" and self.groupCount == 1:
			# ignore polygon element for top-level group
			pass
		elif name == "g":
			if self.groupAttribs == {}:
				self.stream.write("</g>")
				if self.inAnchor:
					self.stream.write("</a>")
			else:
				# skip any groups that haven't been written yet since
				# they must be empty
				self.groupAttribs == {}
			self.inAnchor = False
		elif name == "svg":
			# add delimiter for outer group
			self.stream.write("</svg>")
		else:
			saxutils.XMLGenerator.endElement(self, name)
			
	def writeGroup(self):
		if self.groupAttribs == {}:
			return
		keys = self.groupAttribs.keys()
		if 'onclick' in keys:
			self.stream.write('<a>')
		self.stream.write('<g ')
		for key in self.groupAttribs.keys():
			self.stream.write('%s="%s" ' % (key, self.groupAttribs[key]))
		self.stream.write('>\n')
		self.groupAttribs = {}

	defs = '''
<defs>
	<script type="text/ecmascript"><![CDATA[

	    function relocateWindow(newLocation) {
		var dirname = '';
		var basename = newLocation;
		var lastDelimIndex = newLocation.lastIndexOf('/', newLocation.length);
		if (lastDelimIndex != -1) {
		    dirname = newLocation.substring(0, lastDelimIndex + 1);
		    basename = newLocation.substring(lastDelimIndex + 1, newLocation.length);
		}
		// href of current diagram
		var currentHref = window.location.href;
		var hrefComponents = currentHref.split("/");
		// # of levels above current diagram's directory the root directory is
		var rootLevel = %s;
		// construct href for root directory
		var rootHref = hrefComponents.slice(0, hrefComponents.length - (rootLevel + 2)).join("/") + "/";
		try {
		    // relocate window to referenced machine relative to root href
	            window.location.href = rootHref + dirname + "doc-files/" + basename + ".svg";
	        } catch (e) { alert(basename + " is not included in this documentation"); }
            }
%s

var fontsize = %s;

		function highlight(evt, newColor) {
		  var target = evt.target;
		  var SVGDoc;
		  if ((navigator.appName) == "Adobe SVG Viewer") 
		      SVGDoc = svgDocument;
		  else
		      SVGDoc = target.ownerDocument;
		  var parent = target.parentNode;
		  var parentClass = parent.getAttribute("class");
		  var siblings;
		  if (parentClass == "edge") {
		  	 // get id associated with path
		  	 var arc = parent.getAttribute("id");
			 // get arc's transition
			 var xn = arcTransitions[arc];
			 // get all transition's arcs
			 var arcs = transitionArcs[xn];
			 var group;
			 for (var i = 0; i < arcs.length; i++) {
			 	 group = SVGDoc.getElementById(arcs[i]);
				// get all nodes associated with the arc
				 siblings = group.childNodes;
				 for (var j = 0; j < siblings.length; j++)
			       replaceFill(siblings.item(j), parentClass, arcs[i], newColor);
			 }
		  } else if (parentClass == "cluster" || parentClass == "graph") {
		    siblings = parent.childNodes;
			var id = parent.getAttribute("id");
			for (var j = 0; j < siblings.length; j++) 
			  replaceFill(siblings.item(j), parentClass, id, newColor);
		  }
		}

        function replaceFill(element, nodeClass, id, newColor) {
          if (newColor == "default") newColor = getDefaultFill(element.nodeName, nodeClass, id);
          // replace fill for text and arrow heads on paths
          if (element.nodeName == 'text' || (element.nodeName == 'polygon' && nodeClass == 'edge')) {
            var styles = element.getAttribute('style')
            if (styles) {
                styles = styles.split(";");
                for (var i = 0; i < styles.length; i++) {
                    if ((styles[i].search(/fill:/i) > -1) && styles[i].search(/none/i) == -1)
                    styles[i] = styles[i].replace(/:.*/, ":" + newColor);
                }
                var attribute = styles.join(";");
                element.setAttribute('style', attribute);
            } else {
                element.setAttribute('fill', newColor)
            }
          }
          // in addition to above fill replacement, replace stroke for polygons 
          // (including arrow heads on paths) and paths
          if (element.nodeName == 'polygon' || element.nodeName == 'path') {
            var styles = element.getAttribute('style')
            if (styles) {
                styles = styles.split(";");
                for (var i = 0; i < styles.length; i++) {
                    if ((styles[i].search(/stroke:/i) > -1) && styles[i].search(/none/i) == -1)
                    styles[i] = styles[i].replace(/:.*/, ":" + newColor);
                }
                var attribute = styles.join(";");
                element.setAttribute('style', attribute);
            } else {
                element.setAttribute('stroke', newColor)
            }
          }
        }

		function getDefaultFill(nodeType, nodeClass, id) {
		  if (nodeClass == 'cluster' && nodeType == 'polygon') {
		    var state = nodeStates[id];
			var isExternal = 0;
			for (var i = 0; i < externalStates.length && !isExternal; i++)
			  if (externalStates[i] == state) isExternal = 1;
			if (isExternal)
			  return "lightgrey";
			else
			  return "black";
		  } else {
		    return "black";
		  }
		}

		var tooltipTimeout = undefined;
		var tooltipMouseX = undefined;
		var tooltipMouseY = undefined;
		var tooltipMouseTarget = undefined;

		function delayShowTooltip(evt) {
		  if (evt.target.parentNode.getAttribute("class") == "node") return;
		  if (evt.clientX == tooltipMouseX && evt.clientY == tooltipMouseY) return;
		  cancelTooltip(evt.target);
		  highlight(evt, "\#c64934");
		  tooltipMouseX = evt.clientX;
		  tooltipMouseY = evt.clientY;
		  tooltipMouseTarget = evt.target;
		  this.tooltipTimeout = setTimeout("showTooltip();", 1500);
		}

		function cancelTooltip(target) {
		  if (this.tooltipTimeout != undefined) {
		    clearTimeout(this.tooltipTimeout);
			this.tooltipTimeout = undefined;
		  }
		  var SVGDoc;
		  if ((navigator.appName) == "Adobe SVG Viewer") 
		    SVGDoc = svgDocument;
		  else
		    SVGDoc = target.ownerDocument;
		  var tooltipGroup = SVGDoc.getElementById("tooltip");
		  if (tooltipGroup != undefined) SVGDoc.documentElement.removeChild(tooltipGroup);
		}

		function showTooltip() {
		  var target = tooltipMouseTarget;
		  var SVGDoc;
		  if ((navigator.appName) == "Adobe SVG Viewer") 
		      SVGDoc = svgDocument;
		  else
		      SVGDoc = target.ownerDocument;
		  if (SVGDoc.getElementById("tooltip") != undefined) return;
		  var comment = getCommentString(target);
		  if (comment == "") return;
		  var mouseX = tooltipMouseX;
		  var mouseY = tooltipMouseY;
		  var scale = SVGDoc.documentElement.currentScale;     // scaling modified by zooming ..
		  var offset = SVGDoc.documentElement.currentTranslate; // offset modified by zooming ..
		  var x = ((mouseX - offset.x) / scale) + (0.25 * fontsize);
		  var y = ((mouseY - offset.y) / scale) - fontsize;
		  var tooltipGroup = SVGDoc.createElementNS("http://www.w3.org/2000/svg", "g");
		  var tooltipRect = SVGDoc.createElementNS("http://www.w3.org/2000/svg","rect");
		  tooltipGroup.appendChild(tooltipRect);
		  var textElement;
		  var textNode;
		  var maxWidth = 0;
		  var lineCount;
		  var strings = comment.split('\\n');
		  for (lineCount = 0; lineCount < strings.length; lineCount++) {
		    textElement = SVGDoc.createElementNS("http://www.w3.org/2000/svg", "text");
		    textElement.setAttribute("style", "font-family:Courier New Bold; font-size:" + fontsize + "px; fill:black;");
			textElement.setAttribute("y", lineCount * (1.25 * fontsize));
			textNode = SVGDoc.createTextNode(strings[lineCount]);
			textElement.appendChild(textNode);
			tooltipGroup.appendChild(textElement);
		  }
		  tooltipGroup.setAttribute("id", "tooltip");
		  tooltipGroup.setAttribute("transform",  "translate(" + (x + 5) + "," + y + ")");
		  SVGDoc.documentElement.appendChild(tooltipGroup);		  
		  // get tooltip bbox after adding to doc to determine max
		  // text line width 
		  maxWidth = tooltipGroup.getBBox().width;
		  tooltipRect.setAttribute("x", -0.25 * fontsize);
		  tooltipRect.setAttribute("y", -0.9 * fontsize);
		  tooltipRect.setAttribute("style", "stroke:#c64934; fill:white; stroke-width:1");
		  tooltipRect.setAttribute("width", maxWidth + (0.75 * fontsize));
		  tooltipRect.setAttribute("height", lineCount * (1.25 * fontsize));
		  tooltipGroup.setAttribute("visibility", "visible");
		}

		function getCommentString(target) {
		  var parent = target.parentNode;
		  var targetClass = parent.getAttribute("class");
		  var comment;
		  if (targetClass == "edge") {
		    // get id associated with path
		  	var arc = parent.getAttribute("id");
			// get arc's transition
			var xn = arcTransitions[arc];
			// get transition's commment
			comment = transitionComments[xn];
		  } else if (targetClass == "cluster") {
		    // get title id associated with node
		  	var node = parent.getAttribute("id");
			// get nodes's state
			var state = nodeStates[node];
			// get states's commment
			comment = stateComments[state];
		  } else if (targetClass == "graph") {
		    comment = machineComment;
		  }
		  return comment
		}

		function hideTooltip(evt) {
		  if (evt.target.parentNode.getAttribute("class") == "node") return;
		  highlight(evt, "default");
		  cancelTooltip(evt.target);
		}

		function debug(string){
		  var SVGDoc;
		  if ((navigator.appName) == "Adobe SVG Viewer") 
		      SVGDoc = svgDocument;
		  else
		      SVGDoc = window.document;
		  SVGDoc.getElementById("debug").firstChild.data = string;
		}

	]]></script>
</defs>

<!-- <text id="debug" x="0" y="10" >debug</text> -->
'''

# Generate ECMA script for svg files from global tables maintained by
# dotmachine.
def docecma():
	rv = "var transitionArcs = {};\n"
	for xn in dotmachine.TRANSITION_ARCS.keys():
		rv = rv + "transitionArcs[\"%s\"] = [ " % xn
		rv = rv + string.joinfields(map(lambda x: "\"%s\"" % x, dotmachine.TRANSITION_ARCS[xn].keys()), ", ")
		rv = rv + " ];\n"
	rv = rv + "\n"
	rv = rv + "var arcTransitions = {};\n"
	for arc in dotmachine.ARC_TRANSITIONS.keys():
		rv = rv + "arcTransitions[\"%s\"] = \"%s\";\n" % (arc, dotmachine.ARC_TRANSITIONS[arc])
	rv = rv + "\n"
	rv = rv + "var transitionNodes = {};\n"
	for xn in dotmachine.TRANSITION_NODES.keys():
		rv = rv + "transitionNodes[\"%s\"] = [ " % xn
		rv = rv + string.joinfields(map(lambda x: "\"%s\"" % x, dotmachine.TRANSITION_NODES[xn].keys()), ", ")
		rv = rv + " ];\n"
	rv = rv + "\n"
	rv = rv + "var nodeStates = {};\n"
	for node in dotmachine.NODE_STATES.keys():
		rv = rv + "nodeStates[\"%s\"] = \"%s\";\n" % ( node, dotmachine.NODE_STATES[node] ) 
	rv = rv + "\n"
	rv = rv + "var transitionComments = {};\n"
	for xn in dotmachine.TRANSITION_COMMENTS.keys():
		rv = rv + "transitionComments[\"%s\"] = \"%s\";\n" % ( xn, string.replace(dotmachine.TRANSITION_COMMENTS[xn], '"', r'\"' ) )
	rv = rv + "\n"
	rv = rv + "var stateComments = {};\n"
	for state in dotmachine.STATE_COMMENTS.keys():
		rv = rv + "stateComments[\"%s\"] = \"%s\";\n" % ( state, string.replace(dotmachine.STATE_COMMENTS[state], '"', r'\"' ) )
	rv = rv + "\n"
	rv = rv + "var machineComment = \"%s\";\n" % string.replace(dotmachine.MACHINE_COMMENT, '"', r'\"')
	rv = rv + "\n"
	rv = rv + "var externalStates = [ "
	rv = rv + string.joinfields(map(lambda x: "\"%s\"" % x, dotmachine.EXTERNAL_STATES), ", ")
	rv = rv + " ];\n"
	return rv

# Add/update elements and add ecma script to SVG translation.
def doctranslatesvg(dotout, svgin, fontsize, machineFilePath, package):
	try: 
		parser = make_parser()
		# disable DTD resolver in order to run this program without an
		# Internet connection
		parser.setFeature(xml.sax.handler.feature_external_ges, 0)
		parser.setFeature(xml.sax.handler.feature_external_pes, 0)
		parser.setContentHandler(TransformSVG(docecma(), svgin, fontsize, package))
		parser.parse(dotout)
		dotout.close()
		svgin.close()
	except:
		sys.stderr.write("Exception encountered in SVG-to-SVG translation of: %s\n" % machineFilePath)
		TRANSLATION_EXCEPTION = True
		dotout.close()
		svgin.close()
		raise

# return <machine>.svg string
def docsvg(compilationUnit, machine, targetDirectory, dotPath, fontsize):
	# obtain dot translation of the machine from dotmachine translator
	dotTranslation = dotmachine.translate(compilationUnit, machine, targetDirectory,
										  [("--url-formatter", "docmachine.URLFormatter"),
										    ("--tooltip-formatter", "DotMachineNullFormatter.DotMachineNullFormatter")])
	# create 'dot' program sub-process to convert dot to svg
	(dotin, dotout, doterr) = os.popen3(dotPath + (' -Tsvg -Gsize="" -Gratio="" -Nfontsize="%s" -Efontsize="%s" -Elabelfontsize="%s" -Gfontsize="%s"' %
										(fontsize, fontsize, fontsize, fontsize)))
	# redirect dot stderr to /dev/null (Unix) or NUL (Windows)
	if sys.platform == "win32":
		devnullpath = 'NUL'
	else:
		devnullpath = '/dev/null'
	devnull = open(devnullpath, 'a+', 0)
	os.dup2(devnull.fileno(), doterr.fileno())
	# write dot translation to dot input
	dotin.write(dotTranslation)
	dotin.close()
	# create pipe to obtain output from our svg-to-svg translator
	(svgr, svgw) = os.pipe()
	svgout = os.fdopen(svgr, 'r')
	svgin = os.fdopen(svgw, 'w')
	TRANSLATION_EXCEPTION = False
	# send svg translation from dot output to our svg-to-svg
	# translator - run as separate thread to avoid deadlock
	thread.start_new(doctranslatesvg, (dotout, svgin, fontsize, machine.absoluteMachineFilePath, getPackage(compilationUnit)))
	# read translated svg from translator output and return resulting
	# string
	rv = svgout.read()
	svgout.close()
	if TRANSLATION_EXCEPTION:
		raise "Exception encountered generating SVG machine diagram for %s" % machine.absoluteMachineFilePath
	else:
		return rv

# Translate an abstract machine to SVG.
def translate(compilationUnit, machine, targetDirectory, opts):
	global packageSubdirectory
	dotPath = "dot"
	fontsize = 8
	documentHeader = ""
	svgOnly = False
	packageSubdirectory = ""
	for arg, val in opts:
		if arg == '--dot-path':
			dotPath = val
		elif arg == "--header":
			documentHeader = val
		elif arg == "--svg-only":
			svgOnly = True
		elif arg == "--package-subdirectory":
			packageSubdirectory = val
		elif arg == "--svg-fontsize":
			fontsize = val
	if not svgOnly:
		# write <machine>.html file
		docmachinehtml(compilationUnit, machine, targetDirectory, documentHeader)
	# return <machine>.svg string
	return docsvg(compilationUnit, machine, targetDirectory, dotPath, fontsize)
