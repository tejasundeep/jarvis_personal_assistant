import json

from neurons.waiting.wait import waitjarvis
# Greetings
from neurons.greetings.greeting import greeting
from neurons.concern.concern import concern
# Time Modules
from neurons.timeinfo.current_time import time
from neurons.timeinfo.current_date import date
from neurons.timeinfo.current_day import day
from neurons.timeinfo.current_month import month
from neurons.timeinfo.current_year import year
from neurons.timeinfo.current_weekday import weekday
# Location Module
from neurons.location.current_location import location
from neurons.location.distance_calculator import distance
# Weather Module
from neurons.weather.current_temprature import temperature
from neurons.weather.current_weather import weather
# OS Modules
from neurons.sysinfo.current_os_type import os_type
from neurons.sysinfo.current_os import operating_system
from neurons.sysinfo.current_processor import processor
from neurons.sysinfo.current_ram import ram
from neurons.sysinfo.current_pc_name import pcname
from neurons.sysinfo.current_ipaddress import ipaddress
from neurons.sysinfo.current_macadress import macaddress
from neurons.sysinfo.current_disk_used import diskused
from neurons.sysinfo.current_disk_total_size import disktotalsize
from neurons.sysinfo.current_free_disk import freedisk
from neurons.sysinfo.current_disk_info import diskinfo
from neurons.sysinfo.current_cpu_used import cpu_used
from neurons.sysinfo.current_ram_used import ram_used
# Search Modules
from neurons.search.website import website
from neurons.search.google import google
from neurons.search.youtube import youtube
from neurons.search.wikipedia import wikipedia
# System Functions
from neurons.sysfun.volumeup import volumeup
from neurons.sysfun.volumedown import volumedown
from neurons.sysfun.volumemute import volumemute
from neurons.sysfun.screenshot import screenshot
from neurons.sysfun.cut import cut
from neurons.sysfun.copy import copy
from neurons.sysfun.paste import paste
from neurons.sysfun.delete import delete
from neurons.sysfun.pageup import pageup
from neurons.sysfun.pagedown import pagedown
from neurons.sysfun.openfolder import openfolder
from neurons.sysfun.sendemail import sendemail
from neurons.sysfun.read_text import readtext
from neurons.sysfun.shutdown_windows import shutdownwindows
from neurons.sysfun.restart_windows import restartwindows
from neurons.sysfun.logout_windows import logoutwindows
# Open Programs
from neurons.programs.antivirus import programwindowsantivirus
from neurons.programs.available_networks import programwindowsnetworks
from neurons.programs.browser import programwindowsbrowser
from neurons.programs.calculator import programwindowscalculator
from neurons.programs.camera import programwindowscamera
from neurons.programs.clock import programwindowsclock
from neurons.programs.cmd import programwindowscmd
from neurons.programs.control_panel import programwindowscontrolpanel
from neurons.programs.notepad import programwindowsnotepad
from neurons.programs.paint import programwindowspaint
from neurons.programs.photos import programwindowsphotos
from neurons.programs.player import programwindowsplayer
from neurons.programs.settings import programwindowssettings
from neurons.programs.taskmgr import programwindowstaskmanager
from neurons.programs.windows_mail import programwindowsmail
from neurons.programs.windows_notifications import programwindowsnotifications
# Music
from neurons.music.playmusic import playmusic
from neurons.music.stopmusic import stopmusic
# Music
from neurons.joke.jokes import jokes
# Remember
from neurons.remember.remember import remember
from neurons.remember.recall_data import recalldata

neurons = {
    "neurons": [
        waitjarvis,
        greeting, 
        concern,
        time,
        date,
        day, 
        month, 
        year,
        weekday,
        distance,
        location,
        temperature,
        weather,
        os_type,
        operating_system,
        processor,
        ram,
        pcname,
        ipaddress,
        macaddress,
        diskused,
        disktotalsize,
        freedisk,
        diskinfo,
        cpu_used,
        ram_used,
        website,
        google,
        youtube,
        volumeup,
        volumedown,
        volumemute,
        screenshot,
        cut,
        copy,
        paste,
        delete,
        pageup,
        pagedown,
        openfolder,
        sendemail,
        readtext,
        shutdownwindows,
        restartwindows,
        logoutwindows,
        wikipedia,
        programwindowsantivirus,
        programwindowsnetworks,
        programwindowsbrowser,
        programwindowscalculator,
        programwindowscamera,
        programwindowsclock,
        programwindowscmd,
        programwindowscontrolpanel,
        programwindowsnotepad,
        programwindowspaint,
        programwindowsphotos,
        programwindowsplayer,
        programwindowssettings,
        programwindowstaskmanager,
        programwindowsmail,
        programwindowsnotifications,
        playmusic,
        stopmusic,
        jokes,
        remember,
        recalldata
    ]
}