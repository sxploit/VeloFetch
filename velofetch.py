import getpass, socket, platform
import os, subprocess
from colorama import Fore

def getuptime():
    uptime_str = os.popen("uptime -p").read().strip()
    return uptime_str

def getresolutions():
    result = subprocess.run(['xrandr', '--current'], stdout=subprocess.PIPE)
    output = result.stdout.decode()

    for line in output.splitlines():
        if '*' in line:
            resolution = line.split()[0]
            return resolution

def checkmanagers(packagemgr):
  try:
    subprocess.run([packagemgr, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return True
  except FileNotFoundError:
    return False

def getinstalledmanagers():
  managers = []
  
  if checkmanagers("pacman"):
    managers.append("Pacman")
    
  if checkmanagers("apt"):
    managers.append("APT")
  
  if checkmanagers("flatpak"):
    managers.append("Flatpak")
  
  if checkmanagers("dnf"):
    managers.append("DNF")
  
  if checkmanagers("snap"):
    managers.append("Snap")
  
  if checkmanagers("yum"):
    managers.append("YUM")
    
  if checkmanagers("zypper"):
    managers.append("Zypper")
    
  if checkmanagers("emerge"):
    managers.append("Portage")
  
  if checkmanagers("nix"):
    managers.append("Nix")
    
  if checkmanagers("rpm"):
    managers.append("RPM")
    
  if checkmanagers("pkg"):
    managers.append("PKG")
  
  return managers


username = getpass.getuser()
hostname = socket.gethostname()
system = platform.system()
kernel = platform.release()
uptime = getuptime()
resolution = getresolutions()
shell = os.readlink('/proc/%d/exe' % os.getppid())
installed_managers = getinstalledmanagers()
if installed_managers:
  managers_list = ", ".join(installed_managers)
else:
  managers_list = "No Package Managers Found"
blu = Fore.BLUE
w = Fore.LIGHTWHITE_EX
lg = Fore.LIGHTGREEN_EX
ly = Fore.LIGHTYELLOW_EX

velofetch = f"""
{w}┌───────────────{lg}VeloFetch{w}────────────────┐
  {ly}USER{w}⋮ {username}                   
  {ly}OS{w}⋮ {system}                       
  {ly}HOST{w}⋮ {hostname}                   
  {ly}KERNEL{w}⋮ {kernel}                   
  {ly}UPTIME{w}⋮ {uptime}                   
  {ly}SHELL{w}⋮ {shell}  
  {ly}RESOLUTIONS{w}⋮ {resolution}
  {ly}PKG MANAGERS{w}⋮ {managers_list}                   
{w}└────────────────────────────────────────┘
"""
print(velofetch)