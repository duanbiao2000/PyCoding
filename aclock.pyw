#coding:utf-8
import datetime
import pygame
import os
import time
import random
from pynput.keyboard import Key,Listener

all_songs=[]
all_songs_dict={}
for root,dirs,names in os.walk("d:/User/{}/Music".format(os.getlogin()))
    for filename in names:
        if os.path.join(root,filename)[-4:]==".mp3" or os.path.join(root,filename).replace("\\","/")

finding = open("alarm_list.txt","a")
finding.close()
finding = open("alarm_list.txt","r")
alarm_list_undone = findling.readlines()
finding.close()
alarm_list=[]
for i in alarm_list_undone:
    alarm_list.append(i.replace("\n",""))

finding= open("dates_one.txt","a")
finding.close()
finding = open("dates_one.txt","r")
dates_undone_one=finding.readlines()
finding.close()
alarm_list=[]
for i in alarm_list_undone:
    alarm_list.append(i.replace("\n",""))

finding=open("dates_one.txt","a")
finding.close()
finding = open("dates_one.txt","r")
dates_undone_one = finding.readlines()
finding.close()
finding=open("dates_two.txt","a")
finding.close()
finding = open("dates_two.txt","r")
dates_undone_two=finding.readlines()
finding.close()
dates={}
for i in range(len(dates_undone_one)):
    dates[dates_undone_one[i].replace("\n","")]=eval(dates_undone_two[i].replace("\n",""))


findling=open("songs_one.txt","a")
finding.close()
finding=open("song_one.txt","r")
songs_undone_one=finding.readlines()
finding.close()
finding=open("songs_two.txt","a")
finding.close()
finding=open("songs_two.txt","r")
songs_undone_two

