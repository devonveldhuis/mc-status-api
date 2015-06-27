import os
from flask import Flask
from flask import jsonify
from mcstatus import MinecraftServer

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/status/<hostname>')
@app.route('/status/<hostname>/<port>')
def status(hostname, port=25565):
	server = MinecraftServer.lookup("{0}:{1}".format(hostname, port))
	status = server.status()
	ping = server.ping()
	players = []

	if status.players.sample != None:
		players = [p.name for p in status.players.sample]

	return jsonify (
		hostname=hostname,
		port=port,
		description=status.description,
		version=status.version.name,
		players_online=status.players.online,
		players_max=status.players.max,
		players=','.join(players),
		ping=ping
	)