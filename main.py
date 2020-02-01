#!/usr/bin/env python3
import HeardItFunctions

credentials = HeardItFunctions.processCredentials('credentials.txt')

playlist = HeardItFunctions.preparePlaylist(length = 5,credentials = credentials) 

HeardItFunctions.emailMusic(playlist,credentials)