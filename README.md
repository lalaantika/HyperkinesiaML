# HyperkinesiaML - 
Machine Learning Tool For Hyperkinesia
# Instructions - 
- Install all the software required First.
- Change the CellProfiler two directories in preferences Plugin 
- Directory with CP-Charm Modules and ImageJ Plugins to imagej plugin path Import pipeline of CP-charm from file menu.
- To specify classes name as “NegCtrl” and “PosCtrl” as for the classification and training part create folder of these name and place the data there for training 
- Edit extensions in metadata and in name and types according to image format. 
- Edit regular expression in meta data from (?P<Key>.*)-(?P<HoldOut>[A-Z])-.*.tif  and make it (?p&lt;Key&gt;.*).<image Format> and click update
- Change File Extension in Nameand type of Cellprofiler then click update. 
- Click Analyze Images and it will give output in CSV Format. 
- Then give output of CellProfiler as input for training testing algorithm. /n
