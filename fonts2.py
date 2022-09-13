import sys, subprocess

_proc = subprocess.Popen(['powershell.exe', 'Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts"'], stdout=sys.stdout)
_proc.communicate()