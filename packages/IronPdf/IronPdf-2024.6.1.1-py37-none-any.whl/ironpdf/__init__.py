"""
ironpdf

IronPdf for Python
"""
# imports
import sys
import os
import platform
import subprocess
import shlex
# metadata
__version__ = "2024.6.1.1"
__author__ = 'Iron Software'
__credits__ = 'Iron Software'
# determine root path for IronPdf files
root = ""
# TODO 7/4/23: actually, we can just hard-code "native_package" to "IronPdf" for all platforms
native_package = ""
print('Attempting import of IronPdf ' + __version__)
if platform.system() == "Windows":
   native_package = "IronPdf.Native.Chrome.Windows"
   root = sys.prefix
   print('Checking directory "' + root +'"')
   if not os.path.exists(os.path.join(root, "IronPdf.Slim", "IronPdf.dll")):
      root = os.path.join(sys.prefix, "localcache", "local-packages")
      print('Checking directory "' + root +'"')
   if not os.path.exists(os.path.join(root, "IronPdf.Slim", "IronPdf.dll")):
      root = sys.prefix
      print('Checking directory "' + root +'"')
   if not os.path.exists(os.path.join(root, "IronPdf.Slim", "IronPdf.dll")):
      root = os.path.join(sys.prefix, "..", "..", "..")
      print('Checking directory "' + root +'"')
   # install .NET
   try:
      p = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "'+os.path.join(root, "IronPdf.Slim", "dotnet-install.ps1")+'" -Runtime dotnet -Version 6.0.0', stdout=sys.stdout)
      p.communicate()
   except:
      print('Warning! Failed to install .NET 6.0. Consider manually installing .NET 6.0 from https://dotnet.microsoft.com/en-us/download/dotnet/6.0')
elif platform.system() == "Linux":
   native_package = "IronPdf.Native.Chrome.Linux"
   root = os.path.join(os.path.expanduser('~'), ".local")
   print('Checking directory "' + root +'"')
   if not os.path.exists(os.path.join(root, "IronPdf.Slim", "IronPdf.dll")):
      root = "/usr/local"
      print('Checking directory "' + root +'"')
   if not os.path.exists(os.path.join(root, "IronPdf.Slim", "IronPdf.dll")):
      root = sys.prefix
      print('Checking directory "' + root +'"')
   if not os.path.exists(os.path.join(root, "IronPdf.Slim", "IronPdf.dll")):
      root = os.path.join(sys.prefix, "..", "..", "..")
      print('Checking directory "' + root +'"')
   # install .NET
   try:
      subprocess.call(shlex.split(os.path.join(root, "IronPdf.Slim", "dotnet-install.sh")+' -Runtime dotnet -Version 6.0.0'))
   except:
      print('Warning! Failed to install .NET 6.0. Consider manually installing .NET 6.0 from https://dotnet.microsoft.com/en-us/download/dotnet/6.0')
elif platform.system() == "Darwin":
   if "arm" in platform.processor().lower():
      native_package = "IronPdf.Native.Chrome.MacOS.ARM"
      root = sys.prefix
   else:
      native_package = "IronPdf.Native.Chrome.MacOS"
      root = sys.prefix
   print('Checking directory "' + root +'"')
   if not os.path.exists(os.path.join(root, "IronPdf.Slim", "IronPdf.dll")):
      root = "/opt/homebrew"
      print('Checking directory "' + root +'"')
   if not os.path.exists(os.path.join(root, "IronPdf.Slim", "IronPdf.dll")):
      root = "/usr/local"
      print('Checking directory "' + root +'"')
   if not os.path.exists(os.path.join(root, "IronPdf.Slim", "IronPdf.dll")):
      root = os.path.expanduser('~')+'/Library/Python/'+str(sys.version_info[0])+'.'+str(sys.version_info[1])
      print('Checking directory "' + root +'"')
   if not os.path.exists(os.path.join(root, "IronPdf.Slim", "IronPdf.dll")):
      root = os.path.expanduser('~')+'/Library/Python/3.9'
      print('Checking directory "' + root +'"')
   # install .NET
   try:
      subprocess.call(shlex.split(os.path.join(root, "IronPdf.Slim", "dotnet-install.sh")+' -Runtime dotnet -Version 6.0.0'))
   except:
      print('Warning! Failed to install .NET 6.0. Consider manually installing .NET 6.0 from https://dotnet.microsoft.com/en-us/download/dotnet/6.0')
if not os.path.exists(os.path.join(root, "IronPdf.Slim", "IronPdf.dll")):
   raise Exception("Failed to locate IronPdf.Slim.dll at '" + root +  "/IronPdf.Slim'. Please see https://ironpdf.com/troubleshooting/quick-ironpdf-troubleshooting/ for more information")
else:
   print('Succesfully located files in "' + root +'"')
print('IronPdf detected root Python package directory of ' + root + '/IronPdf.Slim')
# load .NET
from pythonnet import load
load("coreclr")
import clr
# import ironpdf .net assembly
sys.path.append(os.path.join(root, "IronPdf.Slim"))
clr.AddReference(os.path.join(root, "IronPdf.Slim", "IronPdf.dll"))
clr.AddReference(os.path.join(root, "IronPdf.Slim", "IronSoftware.Logger.dll"))
clr.AddReference(os.path.join(root, "IronPdf.Slim", "IronSoftware.Shared.dll"))
clr.AddReference(os.path.join(root, "IronPdf.Slim", "IronSoftware.Abstractions.dll"))
clr.AddReference("System.Collections")
# import .net types
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import List
from System import DateTime
from IronPdf import *
from IronPdf.Logging import *
from IronPdf.Engines.Chrome import *
from IronPdf.Rendering import *
from IronPdf.Annotations import *
from IronPdf.Editing import *
from IronPdf.Security import *
from IronPdf.Signing import *
from IronPdf.Extensions import *
from IronSoftware.Drawing import *
# configure ironpdf
root_pkg_dir = os.path.join(root, native_package, __version__)
Installation.LinuxAndDockerDependenciesAutoConfig = True
Installation.AutomaticallyDownloadNativeBinaries = True
Installation.CustomDeploymentDirectory = root_pkg_dir
Installation.ChromeGpuMode = ChromeGpuModes.Disabled
Installation.SetProgrammingLang("python")
if platform.system() == "Darwin":
   Installation.SingleProcess = True
# check for nuget packages
print('IronPdf will now download dependencies for ' + platform.system() + ' to ' + root_pkg_dir + '. If you encounter any issues launching IronPdf, please remove .nupkg files from this directory and try again. Visit https://ironpdf.com/python/docs/ for more information.')
print('Optionally you may set Installation.CustomDeploymentDirectory to a custom directory and manually download '+native_package+' NuGet package to this directory.')
try:
   Installation.Initialize()
except:
   print('Warning! Failed to initialize native dependencies. Please set Installation.CustomDeploymentDirectory to the directory containing IronPdf native dependencies.')
# HELPER METHODS
def ToPage(item):
   """
   Converts the specified integer into a page index for IronPdf
   """
   output = List[int]()
   output.Add(item)
   return output
   
def ToPageList(list):
   """
   Converts the specified list of integers into a list of page indices for IronPdf
   """
   output = List[int]()
   for i in range(len(list)):
      output.Add(list[i])
   return output
   
def ToPageRange(start,stop):
   """
   Creates a list of page indices for IronPdf using the specified start and stop index
   """
   output = List[int]()
   for i in range(start,stop):
      output.Add(i)
   return output

def Now():
   """
   Returns the current date and time
   """
   return DateTime.Now